# -*- coding: utf-8 -*-
import socket
import sys
import random
import os

if len(sys.argv) != 4:
    print "python server.py IPaddress PortNumber Filename"
    sys.exit()

# Socket
connection = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# Parámetros
ip_Server = sys.argv[1]
port_Server = int(sys.argv[2])
filename = sys.argv[3]
size_file = os.path.getsize(filename)
address = (ip_Server, port_Server)

# Ventana y tamaño de paquete
buff = 1024
window_Size = 10
window = []
seq_max = 2*window_Size 
"""
i = 0
while i < window_Size:
    window[i] = i
    i += 1
"""


# Header
seq_number = random.randint(0, seq_max)
SYN = 1
data = str(filename) + "|||" + str(size_file) + "|||" + str(SYN) +
         "|||" + str(seq_max) + "|||" + str(seq_number) 


# file_toSend = open(filename, "rb")

try_connection = 0
while True:
    connection.sendto(data, address)
    seq_number = (seq_number + 1) % seq_max
    connection.settimeout(0.5)
    try:
        if try_connection == 5:
            print "Cannot establish connection"
            break

        data, adress = connection.recvfrom(buff)

        if not data:
            break

        (SYN, ACK_Flag, ACK, seq_number) = data.split("|||")
        if str(SYN) == "1" and STR(ACK_Flag) == str(seq_number) and str(seq_number) = str(ACK):
            file_toSend = open(filename, "rb")
            data = 