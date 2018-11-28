# -*- coding: utf-8 -*-
import socket
import sys
import random
import os

if len(sys.argv) != 2:
    print "python server.py PortNumber"
    sys.exit()

# Socket
ip = ""
port = int(sys.argv[1])
connection = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
connection.bind((ip, port))

# Parámetros
buff = 1024
ACK = 0
seq_number_sv = random.randint(0, 100)
current_size = 0
percent = round(0,2)
can_recieve = True

while True:
    packet, address = connection.recvfrom(buff)
    if packet:
        (filename, size_file, SYN, seq_max, seq_number_cl) = packet.split("|||")

        if str(SYS) == "1":
            sended_file = open("file_"+filename, "wb", )
            print("Connecting, waiting for response")
            ACK_Flag = 1
            ACK = (seq_number_cl + 1) % seq_max
            data = str(SYN) + "|||" + str(ACK_Flag) 
                    + "|||" + str(ACK) + "|||" + str(seq_number_sv)
                
            connection.sendto(data, address)
