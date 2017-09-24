#!/bin/bash


# sage: reordertp [-i <RT priority>] [-t <ttl>] [-b <buffer length>] [-U] [-g <max gap>] [-j <max jitter>] [-r <# of clock ref>] [-n <max retx burst>] [-x <reorder/retx delay>] [-X <retx URL>] [-m <payload size>] [-R <RTP header>] <src host 1> ... [<src host N>] <dest host>
#     host format: [<connect addr>[:<connect port>]][@[<bind addr][:<bind port>]]
#     -U: strip RTP header
#     -b: buffer length in ms [default 400]
#     -g: max gap between two clock references in ms [default 300]
#     -j: max jitter in ms [default 150]
#     -r: number of clock references for low pass filter [default 500]
#     -n: max number of retx requests [default 15]
#     -x: delay in ms after which retransmission requests are sent [default 200]
#     -X: retransmission service host:port[/tcp]
#     -m: size of the payload chunk, excluding optional RTP header (default 1316)
#     -R: size of the optional RTP header (default 12)

reordertp -U -b500 -g600 -x1000 @:3000 10.0.10.5:4443 -X72.0.154.251