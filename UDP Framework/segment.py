from enum import Enum
import struct

class SegmentType(Enum):
    SYN = 1
    ACK = 2
    SYNACK = 3
    DATA = 4
    FIN = 5

class Segment:
    @staticmethod
    def calculate_checksum(data):
        MOD_ADLER = 65521
        a = 1
        b = 0
        for byte in data:
            a = (a + byte) % MOD_ADLER
            b = (b + a) % MOD_ADLER
        return (b << 16) | a

    @staticmethod
    def encode(s_type, seq, ack, data):
        if type(data) == str:
            data = data.encode()
        data_size = len(data)
        packet = (s_type.value, seq, ack, data)
        checksum = Segment.calculate_checksum(struct.pack(f"!I I I {data_size}s", *packet))
        packet = struct.pack(f"!I I I {data_size}s Q", *packet, checksum)
        return packet
    
    @staticmethod
    def decode(segment):
        data_size = len(segment) - struct.calcsize("!I I I Q")
        type, seq, ack, data, checksum = struct.unpack(f"!I I I {data_size}s Q", segment)
        if checksum != Segment.calculate_checksum(struct.pack(f"!I I I {data_size}s", type, seq, ack, data)):
            return None, None, None, None, None
        return (SegmentType(type), seq, ack, data_size, data)
        
    @staticmethod
    def max_data_size(buffer_size):
        return buffer_size - struct.calcsize("!I I I Q")
    