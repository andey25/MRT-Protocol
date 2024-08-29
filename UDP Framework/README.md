[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/KQFw0QXH)
# CSEE 4119 Spring 2024, Assignment 2
## Your name: Anik Dey
## GitHub username: ad4215

### Code Compilation and Usage Instructions:

1. Clone the repository to your local machine.
2. To test without loss, run the following commands in 2 different terminal windows:
    - `python3 app_server.py <source_ip> <max_chunk_size>`
    - `python3 app_client.py <client_port> <server_ip> <server_port> <max_chunk_size>`
3. To test with loss, in 3 different terminal windows, run the following commands:
    - `python3 network.py <network_port> <client_ip> <client_port> <server_ip> <server_port> <loss_file>`
    - `python3 app_server.py <source_ip> <max_chunk_size>`
    - `python3 app_client.py <client_port> <network_ip> <network_port> <max_chunk_size>`
4. Example-
    - Without loss:
        - `python3 app_server.py 52000 256` (please be mindful of the chunk size and bit error rate parameter in the loss, the chunk size should be low in case the bit error rate is too high, more details in testme file.)
        - `python3 app_client.py 51000 127.0.0.1 50000 256` 
    - With loss:
        - `python3 network.py 50000 127.0.0.1 51000 127.0.0.1 52000 loss.txt`
        - `python3 app_server.py 52000 256`
        - `python3 app_client.py 51000 127.0.0.1 50000 256`
     
### Code Structure and Functionality:

### mrt_server.py

Server class: Implements the server-side functionalities of the MRT protocol.
Methods:
init: Initializes the server, setting up the UDP socket and configuring the receive buffer.
accept: Waits for and accepts a connection request from a client through a 3-way handshake process. It handles SYN, SYNACK, and ACK packets to establish a connection.
receive: Receives data from a connected client. It ensures data integrity and order through a combination of segment acknowledgment and sequencing.
packet_handler: A separate thread for handling incoming packets, updating the receive buffer, and sending acknowledgments.
close: Closes the server and its UDP socket, terminating any existing connections.

### mrt_client.py

Client class: Implements the client-side functionalities of the MRT protocol.
Methods:
init: Initializes the client, creating a UDP channel to communicate with the server.
connect: Establishes a connection to the server using the SYN, SYNACK, and ACK sequence.
send: Splits the data into segments and sends them to the server, handling retransmissions for lost or corrupted segments.
ack_handler: A separate thread for handling ACKs from the server, ensuring that data segments are acknowledged before proceeding.
close: Closes the connection and the UDP socket.

### Segment.py

SegmentType Enum: Defines the types of messages used in the MRT protocol, like SYN, ACK, SYNACK, DATA, and FIN.
Segment class: Provides static methods for encoding and decoding segments, calculating checksums for data integrity, and determining the maximum data size for segments.
Methods:
encode: Encodes a message into a segment, with the type, sequence number, acknowledgment number, and a checksum for error detection.
decode: Extracts a segment's contents and verifies the checksum.
calculate_checksum: Calculates a checksum for a given segment to detect error.


### Overview of MRT Protocol


Connection Establishment: 
A 3-way handshake process has been implemented to establish a reliable connection between the client and server, so that both parties are synchronized and ready for data transfer.

Handling Segment Loss:
Both the client and server implement retransmission mechanisms. If an ACK for a segment is not received within a certain timeframe, the segment is resent.

Data Corruption:
A checksum is calculated for each segment. If the checksum verification fails upon receipt, the segment is discarded, and retransmission is expected.

Out-of-Order Delivery:
The client and server maintain sequence numbers for segments. Out-of-order segments are stored until missing segments arrive.

High Link Latency:
ACKs have been used to confirm the receipt of segments which allow the sender to adjust the rate of transmission according to the network conditions to avoid the impact of high latency.

Data Transfer:
Before sending data, it is segmented into a defined segment size. Each segment is individually sent and acknowledged.

Flow Control:
The receiver specifies a buffer size, preventing the sender from overwhelming the receiver’s capacity to process incoming data.

Connection Termination: 
The server can automatically close itself should there be a timeout error, but the client never stops automatically, in case the server gets disconnected itself for really bad network, the client needs to be stopped manually.

