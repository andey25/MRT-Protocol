# 
# Columbia University - CSEE 4119 Computer Networks
# Assignment 2 - Mini Reliable Transport Protocol
#
# mrt_server.py - defining server APIs of the mini reliable transport protocol
#

import socket # for UDP connection
from segment import Segment, SegmentType
from queue import Queue
from threading import Thread
import logging
from time import sleep

#
# Server
#
class Server:
    def init(self, src_port, receive_buffer_size):
        """
        initialize the server, create the UDP connection, and configure the receive buffer

        arguments:
        src_port -- the port the server is using to receive segments
        receive_buffer_size -- the maximum size of the receive buffer
        """
        self.src_port = src_port
        self.receive_buffer_size = receive_buffer_size
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.settimeout(5)
        self.packet_data = {} # contains seq number and data
        self.packet_queue = Queue() # Segments are put in this queue so that the child thread can handle them
        self.data_received = 0
        logging.basicConfig(level=logging.INFO, filename=f"./log_{self.src_port}.txt", filemode="w", format="time=%(asctime)s %(message)s")
        
    def accept(self):
        """
        accept a client request
        blocking until a client is accepted

        it should support protection against segment loss/corruption/reordering 

        return:
        the connection to the client 
        """
        self.sock.bind(("", self.src_port))
        
        # Server waits for SYN packet from client and loops until it receives one
        while True:
            try:
                data, addr = self.sock.recvfrom(self.receive_buffer_size)
                segment = Segment.decode(data)
                if segment[0] == SegmentType.SYN:
                    logging.info(f"ip={addr[0]} port={addr[1]} seq=0 ack=0 type={segment[0]} size=0")
                    # Server sends SYNACK packet to client
                    self.sock.sendto(Segment.encode(SegmentType.SYNACK, 0, 0, ""), addr)
                    break

            except socket.timeout:
                continue
        
        # Server waits for ACK packet from client and loops until it receives an ACK packet or a DATA packet
        while True:
            try:
                data, addr = self.sock.recvfrom(self.receive_buffer_size)
                data = Segment.decode(data)
                if data[0] == SegmentType.SYN:
                    # If SYN is received, it means that client didn't receive the SYNACK packet
                    # Server sends SYNACK packet to client
                    logging.info(f"ip={addr[0]} port={addr[1]} seq=0 ack=0 type={data[0]} size=0")
                    self.sock.sendto(Segment.encode(SegmentType.SYNACK, 0, 0, ""), addr)
                    continue
                if data[0] == SegmentType.ACK:
                    # If ACK is received, then the connection is established
                    logging.info(f"ip={addr[0]} port={addr[1]} seq=0 ack=1 type={data[0]} size=0")
                    break

                if data[0] == SegmentType.DATA:
                    # If DATA is received, then client received the SYNACK packet and tried to send ACK
                    # But the ACK packet was lost
                    # However, the server can continue to receive data from the client
                    logging.info(f"ip={addr[0]} port={addr[1]} seq={data[1]} ack={data[2]} type={data[0]} size={data[3]}")
                    self.packet_queue.put((addr, SegmentType.DATA, data[1], data[2], data[3], data[4]))
                    break
            except socket.timeout:
                # In case of a timeout, server sends SYNACK packet to client
                self.sock.sendto(Segment.encode(SegmentType.SYNACK, 0, 0, ""), addr)
        return addr
    
    def receive(self, conn, length):
        """
        receive data from the given client
        blocking until the requested amount of data is received
        
        it should support protection against segment loss/corruption/reordering 
        the client should never overwhelm the server given the receive buffer size

        arguments:
        conn -- the connection to the client
        length -- the number of bytes to receive

        return:
        data -- the bytes received from the client, guaranteed to be in its original order
        """
        # keep receiving until the requested amount of data is received
        Thread(target=self.packet_handler, daemon=True).start() # Spawn a child thread to handle the packets
        while True:
            sleep(0.001) # Sleep for 1ms to avoid busy waiting
            try:
                data, addr = self.sock.recvfrom(self.receive_buffer_size)
            except socket.timeout:
                # If we do not receive any data for a long time but we have received the necessary data
                # It probably means that the client's FIN packet was lost and the server should close the connection
                if self.data_received >= length:
                    self.packet_queue.put((("", self.src_port), SegmentType.FIN, 0, 0, 0, ""))
                    break

            if addr != conn:
                continue
            
            s_type, seq, ack, data_size, data = Segment.decode(data)

            if s_type is None:
                continue

            if s_type == SegmentType.FIN:
                self.packet_queue.put((conn, SegmentType.FIN, 0, 0, 0, ""))
                break
            
            if s_type == SegmentType.DATA:
                self.packet_queue.put((conn, s_type, seq, ack, data_size, data))

        # build the data from the received packets
        data = b""
        data_list = [(k, v) for k, v in self.packet_data.items()]
        data_list.sort(key=lambda x: x[0])
        for _, v in data_list:
            data += v

        return data[:length]
            

    def packet_handler(self):
        while True:
            sleep(0.001)
            # get the packet data tuple from the queue
            # (SegmentType(type), seq, ack, data_size, data.decode())
            addr, type, seq, ack, data_size, data = self.packet_queue.get()
            # if the packet is a FIN packet, break the loop
            if type == SegmentType.FIN:
                if addr[0] != "": # Don't log it since this is not a real packet
                    logging.info(f"ip={addr[0]} port={addr[1]} seq={seq} ack={ack} type={type} size={data_size}")
                break
            # check if the packet has already been received
            if seq not in self.packet_data:
                self.packet_data[seq] = data
                self.data_received += data_size

            logging.info(f"ip={addr[0]} port={addr[1]} seq={seq} ack={ack} type={type} size={data_size}")
            
            # send an ACK packet to the client
            self.sock.sendto(Segment.encode(SegmentType.ACK, 0, seq + 1, ""), addr)


    def close(self):
        """
        close the server and the client if it is still connected
        blocking until the connection is closed
        """
        self.sock.close()
