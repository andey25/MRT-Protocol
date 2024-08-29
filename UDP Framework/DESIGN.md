# CSEE 4119 Spring 2024, Assignment 2 Design File
## Your name: Anik Dey
## GitHub username: ad4215

Below is an overview of how the codes are addressing the given challenges and the mechanisms like threading which has been implemented.

### Message Types:

SYN: Initiates a connection.

SYNACK: Acknowledges connection initiation.

ACK: Acknowledges receipt of a segment.

DATA: Carries the application data.

FIN: Initiates termination of a connection.


The fundamnetal idea is the client initiates by sending a SYN to server, then the server starts sending SYNACK, if the client acknowledges SYNACK, then it sends ACK and starts sending data. Even if the ACK gets lost, it does not matter cause server will eventually start receiving the data and understand that the client received SYNACK and sent ACK which might have gotten lost. The client sends a FIN after sending the final segment. But there is a timer mechanism, the server will stop if it gets a timeout error (which can be modified in the init method in the server, currently set to 5 seconds). In case, the server stops for very bad network, the client needs to be stopped manually. 

### 3-Way Handshake Mechanism

Connection Establishment: The MRT protocol implements a 3-way handshake to establish a reliable connection between the client and server. 

SYN: Initiated by the client, sending a SYN segment to the server indicating a request to establish a connection.

SYNACK: Upon receiving the SYN, the server responds with a SYNACK segment, acknowledging the connection request.

ACK: Finally, the client sends an ACK segment back to the server, completing the handshake and establishing the connection.

### Threading Architecture

Asynchronous Packet Handling: Both the client and server utilize threading to manage packet sending, receiving, and processing asynchronously. This design allows the main execution flow to remain responsive and perform other tasks (such as accepting new connections on the server side or managing user input on the client side) without being blocked by network I/O operations.

Server: Uses a dedicated thread (packet_handler) to process incoming packets from the queue (packet_queue). This architecture decouples the network I/O operations from the logic of packet processing, including reordering and ACK generation, thus enhancing efficiency and responsiveness.

Client: Employs a separate thread (ack_handler) to listen for and process ACKs from the server. This enables the client to continuously send data segments while asynchronously monitoring for acknowledgments, facilitating fast retransmission in case of packet loss.

The server uses its main thread to receive and child thread to send messages, and the client's main thread sends data and messages, and its child thread receives messages. 

### Data Transmission

Segmentation: Data is segmented into manageable sizes, respecting the maximum segment size (defined during the client initialization). Each segment includes a header with seq and ack numbers, data size, and a checksum for integrity verification.

Sending and Receiving: The client sends data segments sequentially to the server. Each segment's seq number is used to track the order.
The server processes segments in sequence, buffering out-of-order segments until missing pieces arrive, ensuring data integrity and order.
Acknowledgments:

Upon receiving a segment, the server sends an ACK back to the client, acknowledging the next expected seq number.
If an ACK is not received within a predefined timeout, the client retransmits the segment, addressing potential packet loss.

### Timing Mechanisms

Retransmission and Timeouts: The protocol employs timing mechanisms to handle retransmissions effectively, addressing challenges such as packet loss and high latency.

Client Retransmission: The client maintains a timer for each data segment sent. If an ACK for a segment is not received within a specified timeout interval, the segment is retransmitted. This timing mechanism ensures that data is eventually delivered even in the face of packet loss or delays.

Server Response Timing: The server, upon processing received data segments, promptly sends ACK segments back to the client. This timely acknowledgment aids in the client's decision-making regarding segment retransmission and flow control.





