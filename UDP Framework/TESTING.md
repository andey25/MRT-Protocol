# CSEE 4119 Spring 2024, Assignment 2 Testing File
## Your name: Anik Dey
## GitHub username: ad4215

The program was tested on the following test cases:
- No loss, no corruption
- Packet loss but no bit corruption
- Bit corruption but no packet loss
- Both packet loss and bit corruption
- Extreme packet loss and bit corruption

For each test case, number of valid packets received by the server and client were logged. Number of duplicate sends, and the difference of packets sent and acked is a good indicator
of network loss. Apart from that, the time taken to complete the transfer was also logged.

### Test case 1: No loss, no corruption
For this test case, `0 0 0` was used as lossfile settings. Segment size was `512`.
- Time taken: `2,326` seconds
- Data packets received by the server: 16
- ACK packets received by the client: 16

```text
>>> cat log_51000.txt
time=2024-03-25 04:59:27,144 ip=127.0.0.1 port=50000 seq=0 ack=0 type=SegmentType.SYNACK size=0
time=2024-03-25 04:59:27,192 ip=127.0.0.1 port=50000 seq=0 ack=17 type=SegmentType.ACK size=0
time=2024-03-25 04:59:27,194 ip=127.0.0.1 port=50000 seq=0 ack=16 type=SegmentType.ACK size=0
time=2024-03-25 04:59:27,195 ip=127.0.0.1 port=50000 seq=0 ack=15 type=SegmentType.ACK size=0
time=2024-03-25 04:59:27,196 ip=127.0.0.1 port=50000 seq=0 ack=14 type=SegmentType.ACK size=0
time=2024-03-25 04:59:27,197 ip=127.0.0.1 port=50000 seq=0 ack=13 type=SegmentType.ACK size=0
time=2024-03-25 04:59:27,199 ip=127.0.0.1 port=50000 seq=0 ack=12 type=SegmentType.ACK size=0
time=2024-03-25 04:59:27,200 ip=127.0.0.1 port=50000 seq=0 ack=11 type=SegmentType.ACK size=0
time=2024-03-25 04:59:27,201 ip=127.0.0.1 port=50000 seq=0 ack=10 type=SegmentType.ACK size=0
time=2024-03-25 04:59:27,203 ip=127.0.0.1 port=50000 seq=0 ack=9 type=SegmentType.ACK size=0
time=2024-03-25 04:59:27,205 ip=127.0.0.1 port=50000 seq=0 ack=8 type=SegmentType.ACK size=0
time=2024-03-25 04:59:27,206 ip=127.0.0.1 port=50000 seq=0 ack=7 type=SegmentType.ACK size=0
time=2024-03-25 04:59:27,208 ip=127.0.0.1 port=50000 seq=0 ack=6 type=SegmentType.ACK size=0
time=2024-03-25 04:59:27,210 ip=127.0.0.1 port=50000 seq=0 ack=5 type=SegmentType.ACK size=0
time=2024-03-25 04:59:27,211 ip=127.0.0.1 port=50000 seq=0 ack=4 type=SegmentType.ACK size=0
time=2024-03-25 04:59:27,213 ip=127.0.0.1 port=50000 seq=0 ack=3 type=SegmentType.ACK size=0
time=2024-03-25 04:59:27,214 ip=127.0.0.1 port=50000 seq=0 ack=2 type=SegmentType.ACK size=0
time=2024-03-25 04:59:27,216 ip=127.0.0.1 port=50000 seq=0 ack=1 type=SegmentType.ACK size=0
```
```text
>>> cat log_52000.txt
time=2024-03-25 04:59:27,143 ip=127.0.0.1 port=50000 seq=0 ack=0 type=SegmentType.SYN size=0
time=2024-03-25 04:59:27,146 ip=127.0.0.1 port=50000 seq=0 ack=1 type=SegmentType.ACK size=0
time=2024-03-25 04:59:27,148 ip=127.0.0.1 port=50000 seq=16 ack=0 type=SegmentType.DATA size=152
time=2024-03-25 04:59:27,152 ip=127.0.0.1 port=50000 seq=15 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 04:59:27,153 ip=127.0.0.1 port=50000 seq=14 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 04:59:27,156 ip=127.0.0.1 port=50000 seq=13 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 04:59:27,158 ip=127.0.0.1 port=50000 seq=12 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 04:59:27,160 ip=127.0.0.1 port=50000 seq=11 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 04:59:27,162 ip=127.0.0.1 port=50000 seq=10 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 04:59:27,164 ip=127.0.0.1 port=50000 seq=9 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 04:59:27,167 ip=127.0.0.1 port=50000 seq=8 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 04:59:27,171 ip=127.0.0.1 port=50000 seq=7 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 04:59:27,174 ip=127.0.0.1 port=50000 seq=6 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 04:59:27,177 ip=127.0.0.1 port=50000 seq=5 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 04:59:27,179 ip=127.0.0.1 port=50000 seq=4 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 04:59:27,182 ip=127.0.0.1 port=50000 seq=3 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 04:59:27,185 ip=127.0.0.1 port=50000 seq=2 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 04:59:27,188 ip=127.0.0.1 port=50000 seq=1 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 04:59:27,191 ip=127.0.0.1 port=50000 seq=0 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 04:59:27,219 ip=127.0.0.1 port=50000 seq=0 ack=0 type=SegmentType.FIN size=0
```

### Test case 2: Packet loss but no bit corruption
For this test case, `0 0.2 0` was used as lossfile settings. Segment size was `512`.
- Time taken: `10,223` seconds
- Data packets received by the server: 23
- ACK packets received by the client: 17

```text
>>> cat log_51000.txt
time=2024-03-25 05:01:30,108 ip=127.0.0.1 port=50000 seq=0 ack=0 type=SegmentType.SYNACK size=0
time=2024-03-25 05:01:30,142 ip=127.0.0.1 port=50000 seq=0 ack=17 type=SegmentType.ACK size=0
time=2024-03-25 05:01:30,146 ip=127.0.0.1 port=50000 seq=0 ack=16 type=SegmentType.ACK size=0
time=2024-03-25 05:01:30,165 ip=127.0.0.1 port=50000 seq=0 ack=15 type=SegmentType.ACK size=0
time=2024-03-25 05:01:30,170 ip=127.0.0.1 port=50000 seq=0 ack=13 type=SegmentType.ACK size=0
time=2024-03-25 05:01:30,172 ip=127.0.0.1 port=50000 seq=0 ack=12 type=SegmentType.ACK size=0
time=2024-03-25 05:01:30,173 ip=127.0.0.1 port=50000 seq=0 ack=9 type=SegmentType.ACK size=0
time=2024-03-25 05:01:30,175 ip=127.0.0.1 port=50000 seq=0 ack=6 type=SegmentType.ACK size=0
time=2024-03-25 05:01:30,177 ip=127.0.0.1 port=50000 seq=0 ack=5 type=SegmentType.ACK size=0
time=2024-03-25 05:01:30,178 ip=127.0.0.1 port=50000 seq=0 ack=4 type=SegmentType.ACK size=0
time=2024-03-25 05:01:30,181 ip=127.0.0.1 port=50000 seq=0 ack=2 type=SegmentType.ACK size=0
time=2024-03-25 05:01:30,182 ip=127.0.0.1 port=50000 seq=0 ack=1 type=SegmentType.ACK size=0
time=2024-03-25 05:01:32,140 ip=127.0.0.1 port=50000 seq=0 ack=11 type=SegmentType.ACK size=0
time=2024-03-25 05:01:32,143 ip=127.0.0.1 port=50000 seq=0 ack=10 type=SegmentType.ACK size=0
time=2024-03-25 05:01:32,146 ip=127.0.0.1 port=50000 seq=0 ack=7 type=SegmentType.ACK size=0
time=2024-03-25 05:01:34,128 ip=127.0.0.1 port=50000 seq=0 ack=8 type=SegmentType.ACK size=0
time=2024-03-25 05:01:36,122 ip=127.0.0.1 port=50000 seq=0 ack=14 type=SegmentType.ACK size=0
time=2024-03-25 05:01:38,139 ip=127.0.0.1 port=50000 seq=0 ack=3 type=SegmentType.ACK size=0
```

```text
>>> cat log_52000.txt
time=2024-03-25 05:01:28,103 ip=127.0.0.1 port=50000 seq=0 ack=0 type=SegmentType.SYN size=0
time=2024-03-25 05:01:30,105 ip=127.0.0.1 port=50000 seq=0 ack=0 type=SegmentType.SYN size=0
time=2024-03-25 05:01:30,114 ip=127.0.0.1 port=50000 seq=16 ack=0 type=SegmentType.DATA size=152
time=2024-03-25 05:01:30,118 ip=127.0.0.1 port=50000 seq=16 ack=0 type=SegmentType.DATA size=152
time=2024-03-25 05:01:30,121 ip=127.0.0.1 port=50000 seq=15 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 05:01:30,129 ip=127.0.0.1 port=50000 seq=14 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 05:01:30,133 ip=127.0.0.1 port=50000 seq=13 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 05:01:30,137 ip=127.0.0.1 port=50000 seq=12 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 05:01:30,141 ip=127.0.0.1 port=50000 seq=11 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 05:01:30,148 ip=127.0.0.1 port=50000 seq=8 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 05:01:30,152 ip=127.0.0.1 port=50000 seq=6 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 05:01:30,154 ip=127.0.0.1 port=50000 seq=5 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 05:01:30,157 ip=127.0.0.1 port=50000 seq=4 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 05:01:30,159 ip=127.0.0.1 port=50000 seq=3 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 05:01:30,162 ip=127.0.0.1 port=50000 seq=2 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 05:01:30,164 ip=127.0.0.1 port=50000 seq=1 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 05:01:30,168 ip=127.0.0.1 port=50000 seq=0 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 05:01:32,121 ip=127.0.0.1 port=50000 seq=13 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 05:01:32,127 ip=127.0.0.1 port=50000 seq=10 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 05:01:32,131 ip=127.0.0.1 port=50000 seq=9 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 05:01:32,135 ip=127.0.0.1 port=50000 seq=7 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 05:01:32,139 ip=127.0.0.1 port=50000 seq=6 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 05:01:34,127 ip=127.0.0.1 port=50000 seq=7 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 05:01:34,132 ip=127.0.0.1 port=50000 seq=2 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 05:01:36,121 ip=127.0.0.1 port=50000 seq=13 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 05:01:38,136 ip=127.0.0.1 port=50000 seq=2 ack=0 type=SegmentType.DATA size=492
time=2024-03-25 05:01:38,141 ip=127.0.0.1 port=50000 seq=0 ack=0 type=SegmentType.FIN size=0
```

### Test case 3: Bit corruption but no packet loss

For this test case, `0 0 0.001` was used as lossfile settings. Segment size was `256`. 
- Time taken: `50,237` seconds.
- Data packets received by the server: 43
- ACK packets received by the client: 34

One interesting thing about this is that since bit corruption rate is 0.1%, it is almost impossible that a packet with size 1024 bytes will not be corrupted.
Testing this theory with `python app_client.py 51000 127.0.0.1 50000 1024` and `python app_server.py 52000 1024` proved it right. No packet was logged as
received in 5 minutes by the server or client since checksum was failing. Hence, it was required to decrease the packet size. Testing with packet size `256`
produced the following logfiles-

```text
>>> cat log_51000.txt
time=2024-03-25 05:05:49,572 ip=127.0.0.1 port=50000 seq=0 ack=0 type=SegmentType.SYNACK size=0
time=2024-03-25 05:05:49,644 ip=127.0.0.1 port=50000 seq=0 ack=7 type=SegmentType.ACK size=0
time=2024-03-25 05:05:49,646 ip=127.0.0.1 port=50000 seq=0 ack=4 type=SegmentType.ACK size=0
time=2024-03-25 05:05:51,677 ip=127.0.0.1 port=50000 seq=0 ack=28 type=SegmentType.ACK size=0
time=2024-03-25 05:05:51,680 ip=127.0.0.1 port=50000 seq=0 ack=20 type=SegmentType.ACK size=0
time=2024-03-25 05:05:51,682 ip=127.0.0.1 port=50000 seq=0 ack=19 type=SegmentType.ACK size=0
time=2024-03-25 05:05:53,642 ip=127.0.0.1 port=50000 seq=0 ack=27 type=SegmentType.ACK size=0
time=2024-03-25 05:05:53,644 ip=127.0.0.1 port=50000 seq=0 ack=11 type=SegmentType.ACK size=0
time=2024-03-25 05:05:53,646 ip=127.0.0.1 port=50000 seq=0 ack=8 type=SegmentType.ACK size=0
time=2024-03-25 05:05:53,647 ip=127.0.0.1 port=50000 seq=0 ack=2 type=SegmentType.ACK size=0
time=2024-03-25 05:05:55,609 ip=127.0.0.1 port=50000 seq=0 ack=29 type=SegmentType.ACK size=0
time=2024-03-25 05:05:57,597 ip=127.0.0.1 port=50000 seq=0 ack=33 type=SegmentType.ACK size=0
time=2024-03-25 05:05:57,646 ip=127.0.0.1 port=50000 seq=0 ack=21 type=SegmentType.ACK size=0
time=2024-03-25 05:05:59,633 ip=127.0.0.1 port=50000 seq=0 ack=30 type=SegmentType.ACK size=0
time=2024-03-25 05:05:59,635 ip=127.0.0.1 port=50000 seq=0 ack=26 type=SegmentType.ACK size=0
time=2024-03-25 05:05:59,636 ip=127.0.0.1 port=50000 seq=0 ack=16 type=SegmentType.ACK size=0
time=2024-03-25 05:06:01,582 ip=127.0.0.1 port=50000 seq=0 ack=34 type=SegmentType.ACK size=0
time=2024-03-25 05:06:01,621 ip=127.0.0.1 port=50000 seq=0 ack=23 type=SegmentType.ACK size=0
time=2024-03-25 05:06:01,626 ip=127.0.0.1 port=50000 seq=0 ack=3 type=SegmentType.ACK size=0
time=2024-03-25 05:06:03,628 ip=127.0.0.1 port=50000 seq=0 ack=13 type=SegmentType.ACK size=0
time=2024-03-25 05:06:03,629 ip=127.0.0.1 port=50000 seq=0 ack=12 type=SegmentType.ACK size=0
time=2024-03-25 05:06:03,632 ip=127.0.0.1 port=50000 seq=0 ack=1 type=SegmentType.ACK size=0
time=2024-03-25 05:06:11,622 ip=127.0.0.1 port=50000 seq=0 ack=32 type=SegmentType.ACK size=0
time=2024-03-25 05:06:11,635 ip=127.0.0.1 port=50000 seq=0 ack=9 type=SegmentType.ACK size=0
time=2024-03-25 05:06:13,620 ip=127.0.0.1 port=50000 seq=0 ack=18 type=SegmentType.ACK size=0
time=2024-03-25 05:06:17,619 ip=127.0.0.1 port=50000 seq=0 ack=24 type=SegmentType.ACK size=0
time=2024-03-25 05:06:17,620 ip=127.0.0.1 port=50000 seq=0 ack=14 type=SegmentType.ACK size=0
time=2024-03-25 05:06:19,597 ip=127.0.0.1 port=50000 seq=0 ack=31 type=SegmentType.ACK size=0
time=2024-03-25 05:06:19,607 ip=127.0.0.1 port=50000 seq=0 ack=22 type=SegmentType.ACK size=0
time=2024-03-25 05:06:21,611 ip=127.0.0.1 port=50000 seq=0 ack=17 type=SegmentType.ACK size=0
time=2024-03-25 05:06:21,615 ip=127.0.0.1 port=50000 seq=0 ack=15 type=SegmentType.ACK size=0
time=2024-03-25 05:06:21,617 ip=127.0.0.1 port=50000 seq=0 ack=10 type=SegmentType.ACK size=0
time=2024-03-25 05:06:23,611 ip=127.0.0.1 port=50000 seq=0 ack=6 type=SegmentType.ACK size=0
time=2024-03-25 05:06:29,612 ip=127.0.0.1 port=50000 seq=0 ack=5 type=SegmentType.ACK size=0
time=2024-03-25 05:06:37,612 ip=127.0.0.1 port=50000 seq=0 ack=25 type=SegmentType.ACK size=0
```

```text
>>> cat log_52000.txt
time=2024-03-25 05:05:49,570 ip=127.0.0.1 port=50000 seq=0 ack=0 type=SegmentType.SYN size=0
time=2024-03-25 05:05:49,573 ip=127.0.0.1 port=50000 seq=0 ack=1 type=SegmentType.ACK size=0
time=2024-03-25 05:05:49,589 ip=127.0.0.1 port=50000 seq=28 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:05:49,632 ip=127.0.0.1 port=50000 seq=6 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:05:49,637 ip=127.0.0.1 port=50000 seq=3 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:05:51,595 ip=127.0.0.1 port=50000 seq=27 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:05:51,619 ip=127.0.0.1 port=50000 seq=19 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:05:51,622 ip=127.0.0.1 port=50000 seq=18 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:05:53,593 ip=127.0.0.1 port=50000 seq=26 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:05:53,624 ip=127.0.0.1 port=50000 seq=10 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:05:53,630 ip=127.0.0.1 port=50000 seq=7 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:05:53,639 ip=127.0.0.1 port=50000 seq=1 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:05:55,585 ip=127.0.0.1 port=50000 seq=28 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:05:55,599 ip=127.0.0.1 port=50000 seq=16 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:05:55,611 ip=127.0.0.1 port=50000 seq=11 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:05:57,581 ip=127.0.0.1 port=50000 seq=32 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:05:57,608 ip=127.0.0.1 port=50000 seq=20 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:05:59,581 ip=127.0.0.1 port=50000 seq=33 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:05:59,597 ip=127.0.0.1 port=50000 seq=29 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:05:59,603 ip=127.0.0.1 port=50000 seq=25 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:05:59,616 ip=127.0.0.1 port=50000 seq=15 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:05:59,629 ip=127.0.0.1 port=50000 seq=4 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:06:01,581 ip=127.0.0.1 port=50000 seq=33 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:06:01,594 ip=127.0.0.1 port=50000 seq=22 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:06:01,620 ip=127.0.0.1 port=50000 seq=2 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:06:03,599 ip=127.0.0.1 port=50000 seq=21 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:06:03,611 ip=127.0.0.1 port=50000 seq=12 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:06:03,614 ip=127.0.0.1 port=50000 seq=11 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:06:03,616 ip=127.0.0.1 port=50000 seq=9 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:06:03,625 ip=127.0.0.1 port=50000 seq=0 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:06:05,612 ip=127.0.0.1 port=50000 seq=13 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:06:11,594 ip=127.0.0.1 port=50000 seq=31 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:06:11,598 ip=127.0.0.1 port=50000 seq=30 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:06:11,628 ip=127.0.0.1 port=50000 seq=8 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:06:13,604 ip=127.0.0.1 port=50000 seq=17 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:06:13,618 ip=127.0.0.1 port=50000 seq=4 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:06:17,602 ip=127.0.0.1 port=50000 seq=23 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:06:17,611 ip=127.0.0.1 port=50000 seq=13 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:06:19,596 ip=127.0.0.1 port=50000 seq=30 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:06:19,601 ip=127.0.0.1 port=50000 seq=21 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:06:21,603 ip=127.0.0.1 port=50000 seq=16 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:06:21,605 ip=127.0.0.1 port=50000 seq=14 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:06:21,607 ip=127.0.0.1 port=50000 seq=9 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:06:23,606 ip=127.0.0.1 port=50000 seq=5 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:06:29,610 ip=127.0.0.1 port=50000 seq=4 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:06:37,610 ip=127.0.0.1 port=50000 seq=24 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:06:37,615 ip=127.0.0.1 port=50000 seq=0 ack=0 type=SegmentType.FIN size=0
```

### Test case 4: Both packet loss and bit corruption
For this test case, `0 0.2 0.001` was used as lossfile settings. Packet size was `256`.
- Time taken: `2:15` minutes
- Data packets received by the server: 52
- ACK packets received by the client: 34

```text
>>> cat log_51000.txt
time=2024-03-25 04:49:05,563 ip=127.0.0.1 port=50000 seq=0 ack=0 type=SegmentType.SYNACK size=0
time=2024-03-25 04:49:05,707 ip=127.0.0.1 port=50000 seq=0 ack=29 type=SegmentType.ACK size=0
time=2024-03-25 04:49:05,709 ip=127.0.0.1 port=50000 seq=0 ack=19 type=SegmentType.ACK size=0
time=2024-03-25 04:49:07,655 ip=127.0.0.1 port=50000 seq=0 ack=21 type=SegmentType.ACK size=0
time=2024-03-25 04:49:07,656 ip=127.0.0.1 port=50000 seq=0 ack=20 type=SegmentType.ACK size=0
time=2024-03-25 04:49:09,616 ip=127.0.0.1 port=50000 seq=0 ack=16 type=SegmentType.ACK size=0
time=2024-03-25 04:49:11,666 ip=127.0.0.1 port=50000 seq=0 ack=24 type=SegmentType.ACK size=0
time=2024-03-25 04:49:13,673 ip=127.0.0.1 port=50000 seq=0 ack=30 type=SegmentType.ACK size=0
time=2024-03-25 04:49:13,678 ip=127.0.0.1 port=50000 seq=0 ack=28 type=SegmentType.ACK size=0
time=2024-03-25 04:49:17,625 ip=127.0.0.1 port=50000 seq=0 ack=2 type=SegmentType.ACK size=0
time=2024-03-25 04:49:21,592 ip=127.0.0.1 port=50000 seq=0 ack=31 type=SegmentType.ACK size=0
time=2024-03-25 04:49:21,597 ip=127.0.0.1 port=50000 seq=0 ack=23 type=SegmentType.ACK size=0
time=2024-03-25 04:49:25,605 ip=127.0.0.1 port=50000 seq=0 ack=33 type=SegmentType.ACK size=0
time=2024-03-25 04:49:25,630 ip=127.0.0.1 port=50000 seq=0 ack=9 type=SegmentType.ACK size=0
time=2024-03-25 04:49:27,604 ip=127.0.0.1 port=50000 seq=0 ack=14 type=SegmentType.ACK size=0
time=2024-03-25 04:49:29,592 ip=127.0.0.1 port=50000 seq=0 ack=32 type=SegmentType.ACK size=0
time=2024-03-25 04:49:29,602 ip=127.0.0.1 port=50000 seq=0 ack=26 type=SegmentType.ACK size=0
time=2024-03-25 04:49:29,635 ip=127.0.0.1 port=50000 seq=0 ack=4 type=SegmentType.ACK size=0
time=2024-03-25 04:49:31,602 ip=127.0.0.1 port=50000 seq=0 ack=25 type=SegmentType.ACK size=0
time=2024-03-25 04:49:39,624 ip=127.0.0.1 port=50000 seq=0 ack=18 type=SegmentType.ACK size=0
time=2024-03-25 04:49:39,637 ip=127.0.0.1 port=50000 seq=0 ack=3 type=SegmentType.ACK size=0
time=2024-03-25 04:49:49,951 ip=127.0.0.1 port=50000 seq=0 ack=12 type=SegmentType.ACK size=0
time=2024-03-25 04:49:53,647 ip=127.0.0.1 port=50000 seq=0 ack=8 type=SegmentType.ACK size=0
time=2024-03-25 04:49:57,629 ip=127.0.0.1 port=50000 seq=0 ack=13 type=SegmentType.ACK size=0
time=2024-03-25 04:49:57,639 ip=127.0.0.1 port=50000 seq=0 ack=7 type=SegmentType.ACK size=0
time=2024-03-25 04:49:59,629 ip=127.0.0.1 port=50000 seq=0 ack=10 type=SegmentType.ACK size=0
time=2024-03-25 04:50:03,614 ip=127.0.0.1 port=50000 seq=0 ack=34 type=SegmentType.ACK size=0
time=2024-03-25 04:50:03,627 ip=127.0.0.1 port=50000 seq=0 ack=11 type=SegmentType.ACK size=0
time=2024-03-25 04:50:03,640 ip=127.0.0.1 port=50000 seq=0 ack=5 type=SegmentType.ACK size=0
time=2024-03-25 04:50:11,618 ip=127.0.0.1 port=50000 seq=0 ack=27 type=SegmentType.ACK size=0
time=2024-03-25 04:50:11,645 ip=127.0.0.1 port=50000 seq=0 ack=6 type=SegmentType.ACK size=0
time=2024-03-25 04:50:11,647 ip=127.0.0.1 port=50000 seq=0 ack=1 type=SegmentType.ACK size=0
time=2024-03-25 04:50:49,650 ip=127.0.0.1 port=50000 seq=0 ack=15 type=SegmentType.ACK size=0
time=2024-03-25 04:51:09,646 ip=127.0.0.1 port=50000 seq=0 ack=22 type=SegmentType.ACK size=0
time=2024-03-25 04:51:17,662 ip=127.0.0.1 port=50000 seq=0 ack=17 type=SegmentType.ACK size=0
```

```text
>>> cat log_52000.txt
time=2024-03-25 04:49:01,555 ip=127.0.0.1 port=50000 seq=0 ack=0 type=SegmentType.SYN size=0
time=2024-03-25 04:49:05,560 ip=127.0.0.1 port=50000 seq=0 ack=0 type=SegmentType.SYN size=0
time=2024-03-25 04:49:05,565 ip=127.0.0.1 port=50000 seq=0 ack=1 type=SegmentType.ACK size=0
time=2024-03-25 04:49:05,584 ip=127.0.0.1 port=50000 seq=28 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:05,623 ip=127.0.0.1 port=50000 seq=18 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:07,604 ip=127.0.0.1 port=50000 seq=20 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:07,607 ip=127.0.0.1 port=50000 seq=19 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:07,651 ip=127.0.0.1 port=50000 seq=1 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:09,570 ip=127.0.0.1 port=50000 seq=33 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:09,575 ip=127.0.0.1 port=50000 seq=30 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:09,592 ip=127.0.0.1 port=50000 seq=15 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:11,628 ip=127.0.0.1 port=50000 seq=23 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:11,634 ip=127.0.0.1 port=50000 seq=17 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:13,603 ip=127.0.0.1 port=50000 seq=29 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:13,609 ip=127.0.0.1 port=50000 seq=27 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:13,654 ip=127.0.0.1 port=50000 seq=12 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:17,622 ip=127.0.0.1 port=50000 seq=1 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:21,585 ip=127.0.0.1 port=50000 seq=30 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:21,593 ip=127.0.0.1 port=50000 seq=22 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:21,610 ip=127.0.0.1 port=50000 seq=8 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:25,588 ip=127.0.0.1 port=50000 seq=32 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:25,619 ip=127.0.0.1 port=50000 seq=8 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:27,589 ip=127.0.0.1 port=50000 seq=25 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:27,603 ip=127.0.0.1 port=50000 seq=13 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:27,616 ip=127.0.0.1 port=50000 seq=4 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:29,588 ip=127.0.0.1 port=50000 seq=31 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:29,596 ip=127.0.0.1 port=50000 seq=25 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:29,613 ip=127.0.0.1 port=50000 seq=12 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:29,630 ip=127.0.0.1 port=50000 seq=3 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:31,597 ip=127.0.0.1 port=50000 seq=24 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:35,600 ip=127.0.0.1 port=50000 seq=26 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:37,619 ip=127.0.0.1 port=50000 seq=10 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:39,611 ip=127.0.0.1 port=50000 seq=17 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:39,635 ip=127.0.0.1 port=50000 seq=2 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:43,626 ip=127.0.0.1 port=50000 seq=0 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:47,608 ip=127.0.0.1 port=50000 seq=21 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:49,615 ip=127.0.0.1 port=50000 seq=16 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:49,950 ip=127.0.0.1 port=50000 seq=11 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:51,634 ip=127.0.0.1 port=50000 seq=6 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:53,634 ip=127.0.0.1 port=50000 seq=7 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:53,638 ip=127.0.0.1 port=50000 seq=6 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:57,622 ip=127.0.0.1 port=50000 seq=12 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:57,632 ip=127.0.0.1 port=50000 seq=6 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:49:59,627 ip=127.0.0.1 port=50000 seq=9 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:50:03,610 ip=127.0.0.1 port=50000 seq=33 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:50:03,613 ip=127.0.0.1 port=50000 seq=21 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:50:03,626 ip=127.0.0.1 port=50000 seq=10 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:50:03,637 ip=127.0.0.1 port=50000 seq=4 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:50:05,612 ip=127.0.0.1 port=50000 seq=21 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:50:07,644 ip=127.0.0.1 port=50000 seq=0 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:50:11,614 ip=127.0.0.1 port=50000 seq=26 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:50:11,641 ip=127.0.0.1 port=50000 seq=5 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:50:11,644 ip=127.0.0.1 port=50000 seq=0 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:50:19,632 ip=127.0.0.1 port=50000 seq=14 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:50:49,649 ip=127.0.0.1 port=50000 seq=14 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:51:03,642 ip=127.0.0.1 port=50000 seq=21 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:51:09,644 ip=127.0.0.1 port=50000 seq=21 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 04:51:17,660 ip=127.0.0.1 port=50000 seq=16 ack=0 type=SegmentType.DATA size=236
```

### Test case 5: Extreme packet loss and bit corruption
For this test case, `0 0.4 0.002` was used as lossfile settings. Packet size was `256`.

- Time taken: `12:53` minutes
- Data packets received by the server: 71
- ACK packets received by the client: 32

```text
>>> cat log_51000.txt
time=2024-03-25 05:23:08,274 ip=127.0.0.1 port=50000 seq=0 ack=0 type=SegmentType.SYNACK size=0
time=2024-03-25 05:23:10,344 ip=127.0.0.1 port=50000 seq=0 ack=30 type=SegmentType.ACK size=0
time=2024-03-25 05:23:28,301 ip=127.0.0.1 port=50000 seq=0 ack=28 type=SegmentType.ACK size=0
time=2024-03-25 05:23:50,414 ip=127.0.0.1 port=50000 seq=0 ack=22 type=SegmentType.ACK size=0
time=2024-03-25 05:24:02,337 ip=127.0.0.1 port=50000 seq=0 ack=29 type=SegmentType.ACK size=0
time=2024-03-25 05:24:18,377 ip=127.0.0.1 port=50000 seq=0 ack=6 type=SegmentType.ACK size=0
time=2024-03-25 05:24:20,385 ip=127.0.0.1 port=50000 seq=0 ack=9 type=SegmentType.ACK size=0
time=2024-03-25 05:24:54,392 ip=127.0.0.1 port=50000 seq=0 ack=15 type=SegmentType.ACK size=0
time=2024-03-25 05:25:08,401 ip=127.0.0.1 port=50000 seq=0 ack=7 type=SegmentType.ACK size=0
time=2024-03-25 05:25:18,373 ip=127.0.0.1 port=50000 seq=0 ack=32 type=SegmentType.ACK size=0
time=2024-03-25 05:25:20,395 ip=127.0.0.1 port=50000 seq=0 ack=3 type=SegmentType.ACK size=0
time=2024-03-25 05:25:22,406 ip=127.0.0.1 port=50000 seq=0 ack=12 type=SegmentType.ACK size=0
time=2024-03-25 05:25:34,398 ip=127.0.0.1 port=50000 seq=0 ack=13 type=SegmentType.ACK size=0
time=2024-03-25 05:25:40,357 ip=127.0.0.1 port=50000 seq=0 ack=34 type=SegmentType.ACK size=0
time=2024-03-25 05:25:42,407 ip=127.0.0.1 port=50000 seq=0 ack=14 type=SegmentType.ACK size=0
time=2024-03-25 05:25:50,408 ip=127.0.0.1 port=50000 seq=0 ack=18 type=SegmentType.ACK size=0
time=2024-03-25 05:25:56,415 ip=127.0.0.1 port=50000 seq=0 ack=25 type=SegmentType.ACK size=0
time=2024-03-25 05:25:58,475 ip=127.0.0.1 port=50000 seq=0 ack=5 type=SegmentType.ACK size=0
time=2024-03-25 05:26:22,406 ip=127.0.0.1 port=50000 seq=0 ack=16 type=SegmentType.ACK size=0
time=2024-03-25 05:27:06,425 ip=127.0.0.1 port=50000 seq=0 ack=20 type=SegmentType.ACK size=0
time=2024-03-25 05:27:20,426 ip=127.0.0.1 port=50000 seq=0 ack=27 type=SegmentType.ACK size=0
time=2024-03-25 05:27:28,459 ip=127.0.0.1 port=50000 seq=0 ack=1 type=SegmentType.ACK size=0
time=2024-03-25 05:27:58,459 ip=127.0.0.1 port=50000 seq=0 ack=17 type=SegmentType.ACK size=0
time=2024-03-25 05:28:52,498 ip=127.0.0.1 port=50000 seq=0 ack=8 type=SegmentType.ACK size=0
time=2024-03-25 05:28:56,491 ip=127.0.0.1 port=50000 seq=0 ack=23 type=SegmentType.ACK size=0
time=2024-03-25 05:28:56,493 ip=127.0.0.1 port=50000 seq=0 ack=11 type=SegmentType.ACK size=0
time=2024-03-25 05:30:38,568 ip=127.0.0.1 port=50000 seq=0 ack=2 type=SegmentType.ACK size=0
time=2024-03-25 05:31:04,577 ip=127.0.0.1 port=50000 seq=0 ack=4 type=SegmentType.ACK size=0
time=2024-03-25 05:31:08,561 ip=127.0.0.1 port=50000 seq=0 ack=31 type=SegmentType.ACK size=0
time=2024-03-25 05:33:02,621 ip=127.0.0.1 port=50000 seq=0 ack=26 type=SegmentType.ACK size=0
time=2024-03-25 05:33:28,632 ip=127.0.0.1 port=50000 seq=0 ack=24 type=SegmentType.ACK size=0
time=2024-03-25 05:34:36,663 ip=127.0.0.1 port=50000 seq=0 ack=33 type=SegmentType.ACK size=0
time=2024-03-25 05:35:14,718 ip=127.0.0.1 port=50000 seq=0 ack=10 type=SegmentType.ACK size=0
```

```text
>>> cat log_52000.txt
time=2024-03-25 05:23:08,272 ip=127.0.0.1 port=50000 seq=0 ack=0 type=SegmentType.SYN size=0
time=2024-03-25 05:23:08,339 ip=127.0.0.1 port=50000 seq=3 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:23:08,342 ip=127.0.0.1 port=50000 seq=3 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:23:10,296 ip=127.0.0.1 port=50000 seq=29 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:23:20,329 ip=127.0.0.1 port=50000 seq=7 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:23:24,295 ip=127.0.0.1 port=50000 seq=32 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:23:26,315 ip=127.0.0.1 port=50000 seq=21 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:23:26,325 ip=127.0.0.1 port=50000 seq=16 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:23:28,297 ip=127.0.0.1 port=50000 seq=27 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:23:36,305 ip=127.0.0.1 port=50000 seq=24 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:23:46,360 ip=127.0.0.1 port=50000 seq=2 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:23:50,334 ip=127.0.0.1 port=50000 seq=21 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:24:02,319 ip=127.0.0.1 port=50000 seq=28 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:24:14,355 ip=127.0.0.1 port=50000 seq=13 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:24:18,367 ip=127.0.0.1 port=50000 seq=5 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:24:20,370 ip=127.0.0.1 port=50000 seq=8 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:24:22,330 ip=127.0.0.1 port=50000 seq=30 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:24:32,381 ip=127.0.0.1 port=50000 seq=9 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:24:34,354 ip=127.0.0.1 port=50000 seq=14 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:24:40,336 ip=127.0.0.1 port=50000 seq=30 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:24:54,376 ip=127.0.0.1 port=50000 seq=14 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:24:58,345 ip=127.0.0.1 port=50000 seq=32 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:25:02,383 ip=127.0.0.1 port=50000 seq=6 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:25:08,390 ip=127.0.0.1 port=50000 seq=6 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:25:16,353 ip=127.0.0.1 port=50000 seq=32 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:25:18,359 ip=127.0.0.1 port=50000 seq=31 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:25:20,392 ip=127.0.0.1 port=50000 seq=2 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:25:22,392 ip=127.0.0.1 port=50000 seq=11 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:25:34,388 ip=127.0.0.1 port=50000 seq=12 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:25:40,355 ip=127.0.0.1 port=50000 seq=33 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:25:42,396 ip=127.0.0.1 port=50000 seq=13 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:25:50,395 ip=127.0.0.1 port=50000 seq=17 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:25:56,390 ip=127.0.0.1 port=50000 seq=24 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:25:58,468 ip=127.0.0.1 port=50000 seq=4 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:26:12,400 ip=127.0.0.1 port=50000 seq=19 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:26:22,405 ip=127.0.0.1 port=50000 seq=15 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:26:28,426 ip=127.0.0.1 port=50000 seq=0 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:26:32,400 ip=127.0.0.1 port=50000 seq=30 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:26:34,418 ip=127.0.0.1 port=50000 seq=16 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:26:58,411 ip=127.0.0.1 port=50000 seq=30 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:27:00,409 ip=127.0.0.1 port=50000 seq=32 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:27:06,423 ip=127.0.0.1 port=50000 seq=19 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:27:18,426 ip=127.0.0.1 port=50000 seq=30 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:27:20,423 ip=127.0.0.1 port=50000 seq=26 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:27:22,435 ip=127.0.0.1 port=50000 seq=20 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:27:26,440 ip=127.0.0.1 port=50000 seq=16 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:27:28,458 ip=127.0.0.1 port=50000 seq=0 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:27:32,439 ip=127.0.0.1 port=50000 seq=18 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:27:58,456 ip=127.0.0.1 port=50000 seq=16 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:28:00,451 ip=127.0.0.1 port=50000 seq=18 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:28:04,476 ip=127.0.0.1 port=50000 seq=1 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:28:24,461 ip=127.0.0.1 port=50000 seq=23 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:28:36,477 ip=127.0.0.1 port=50000 seq=18 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:28:50,469 ip=127.0.0.1 port=50000 seq=32 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:28:52,495 ip=127.0.0.1 port=50000 seq=7 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:28:56,483 ip=127.0.0.1 port=50000 seq=22 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:28:56,490 ip=127.0.0.1 port=50000 seq=10 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:29:00,475 ip=127.0.0.1 port=50000 seq=32 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:29:16,487 ip=127.0.0.1 port=50000 seq=25 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:30:28,529 ip=127.0.0.1 port=50000 seq=30 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:30:36,538 ip=127.0.0.1 port=50000 seq=23 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:30:38,567 ip=127.0.0.1 port=50000 seq=1 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:31:04,576 ip=127.0.0.1 port=50000 seq=3 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:31:08,549 ip=127.0.0.1 port=50000 seq=30 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:31:42,585 ip=127.0.0.1 port=50000 seq=9 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:33:02,616 ip=127.0.0.1 port=50000 seq=25 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:33:10,609 ip=127.0.0.1 port=50000 seq=32 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:33:18,627 ip=127.0.0.1 port=50000 seq=18 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:33:28,629 ip=127.0.0.1 port=50000 seq=23 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:34:36,661 ip=127.0.0.1 port=50000 seq=32 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:35:08,714 ip=127.0.0.1 port=50000 seq=9 ack=0 type=SegmentType.DATA size=236
time=2024-03-25 05:35:14,716 ip=127.0.0.1 port=50000 seq=9 ack=0 type=SegmentType.DATA size=236
```
