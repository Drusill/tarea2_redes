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
    data, address = connection.recvfrom(buff)
    if data:
        (filename, size_file, SYN, seq_max, seq_number_cl) = data.split("|||")

        if str(SYN) == "1":
            sended_file = open("file_"+filename, "wb", )
            ACK_Flag = 1
            ACK = (int(seq_number_cl) + 1) % int(seq_max)
            data = str(SYN) + "|||" + str(ACK_Flag) + "|||" + str(ACK)
            connection.sendto(data, address)
            print("Connecting, waiting for response")
            break

"""
seq_number_sv = (seq_number_sv + 1) % seq_max
try:
    data, address = connection.recvfrom(buff)

    if data:
"""

