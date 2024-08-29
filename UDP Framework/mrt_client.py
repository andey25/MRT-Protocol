# 
# Columbia University - CSEE 4119 Computer Networks
# Assignment 2 - Mini Reliable Transport Protocol
#
# mrt_client.py - defining client APIs of the mini reliable transport protocol
#

import socket # for UDP connection
import logging
from segment import Segment, SegmentType
from threading import Thread
import time

class Timer:
    def __init__(self, packet):
        self.packet = packet
        self.start_time = time.time()

class Client:
    def init(self, src_port, dst_addr, dst_port, segment_size):
        """
        initialize the client and create the client UDP channel

        arguments:
        src_port -- the port the client is using to send segments
        dst_addr -- the address of the server/network simulator
        dst_port -- the port of the server/network simulator
        segment_size -- the maximum size of a segment (including the header)
        """
        self.src_port = src_port
        self.dst_addr = dst_addr
        self.dst_port = dst_port
        self.segment_size = segment_size
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.settimeout(2)
        self.data_chunks = {}
        self.sent_chunks = {}
        self.finished = False
        logging.basicConfig(level=logging.INFO, filename=f"./log_{src_port}.txt", filemode="w", format="time=%(asctime)s %(message)s")

    def connect(self):
        """
        connect to the server
        blocking until the connection is established

        it should support protection against segment loss/corruption/reordering 
        """
        self.sock.bind(("", self.src_port))
        self.sock.sendto(Segment.encode(SegmentType.SYN, 0, 0, ""), (self.dst_addr, self.dst_port))
        while True:
            # try sending SYN every 2 seconds until SYNACK is received
            try:
                data, addr = self.sock.recvfrom(self.segment_size)
            except socket.timeout:
                self.sock.sendto(Segment.encode(SegmentType.SYN, 0, 0, ""), (self.dst_addr, self.dst_port))
                continue

            # If packet is from a different address, ignore it
            if addr != (self.dst_addr, self.dst_port):
                continue

            segment = Segment.decode(data)
            # If SYNACK is receive, reply with ACK and consider that connection is established
            if segment[0] == SegmentType.SYNACK:
                logging.info(f"ip={addr[0]} port={addr[1]} seq=0 ack=0 type={segment[0]} size=0")
                self.sock.sendto(Segment.encode(SegmentType.ACK, 0, 1, ""), addr)
                break 

    def send(self, data):
        """
        send a chunk of data of arbitrary size to the server
        blocking until all data is sent

        it should support protection against segment loss/corruption/reordering and flow control

        arguments:
        data -- the bytes to be sent to the server
        """
        Thread(target=self.ack_handler).start() # spawn a thread to handle ACKs

        max_data_size = Segment.max_data_size(self.segment_size)
        data_size = len(data)

        # Split data into chunks of max_data_size and serial them from 0
        for i in range(0, data_size, max_data_size):
            self.data_chunks[i // max_data_size] = data[i:i + max_data_size]
        
        
        # Send all the chunks and save them in the state for retransmission
        while self.data_chunks:
            seq, chunk = self.data_chunks.popitem()
            self.sock.sendto(Segment.encode(SegmentType.DATA, seq, 0, chunk), (self.dst_addr, self.dst_port))
            self.sent_chunks[seq] = Timer(chunk) # Timer to keep track of the time the packet was sent
        
        # Wait for all the chunks to be acknowledged
        while self.sent_chunks:
            rem = [(seq, timer) for seq, timer in self.sent_chunks.items()]
            for seq, timer in rem:
                if time.time() - timer.start_time > 2:
                    self.sock.sendto(Segment.encode(SegmentType.DATA, seq, 0, timer.packet), (self.dst_addr, self.dst_port))
                    timer.start_time = time.time()
            time.sleep(0.001)

        # self.finished is to close the child thread
        self.finished = True
        # Send FIN packet to close the connection
        self.sock.sendto(Segment.encode(SegmentType.FIN, 0, 0, ""), (self.dst_addr, self.dst_port))

        return data_size


    def ack_handler(self):
        """
        handle the ACKs from the server
        """
        while True:
            time.sleep(0.001) # Sleep for 1ms to avoid busy waiting
            try:
                data, addr = self.sock.recvfrom(self.segment_size)
            except socket.timeout:
                continue
            except OSError:
                # OSError is raised when the socket is closed
                break
            
            # If packet is from a different address, ignore it
            if addr != (self.dst_addr, self.dst_port):
                continue
            
            s_type, seq, ack, data_size, data = Segment.decode(data)

            
            if s_type is None:
                continue
            
            logging.info(f"ip={addr[0]} port={addr[1]} seq={seq} ack={ack} type={s_type} size={data_size}")

            # ack is seq + 1 so we need to calculate the correct seq
            if s_type == SegmentType.ACK and (ack - 1) in self.sent_chunks:
                self.sent_chunks.pop(ack - 1)
            
            if self.finished:
                break

    def close(self):
        """
        request to close the connection with the server
        blocking until the connection is closed
        """
        self.sock.close()
