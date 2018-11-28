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
GranBuffer=10000
escribir=""
# Parámetros
buff = 1024
ACK = 0
seq_number_sv = random.randint(0, 100)
current_size = 0
percent = round(0,2)
can_recieve = True
bol=True
while bol:
    data, address = connection.recvfrom(buff)
    if data:
        (filename, size_file, SYN, seq_max, seq_number_cl) = data.split("|||")

        if str(SYN) == "1":
            sended_file = open("file_"+filename, "wb", )
            ACK_Flag = 1
            ACK = (int(seq_number_cl) + 1) % int(seq_max)
            data = str(SYN) + "|||" + str(ACK_Flag) + "|||" + str(ACK)
            tries=0
            while tries<=5: 
                connection.sendto(data, address)

                connection.settimeout(0.3)
                print("Connecting, waiting for response")
                try:
                    data=connection.recv(buff)
                    if data:
                        print(data)
                        bol=False
                        break
                except:
                    if tries==5:
                        print("imposibru")
                        sys.exit()
                    tries+=1

while True:
    data, address= connection.recvfrom(buff)
    if len(data)+len(escribir)>GranBuffer:
        sended_file.write(escribir)
        sended_file.write(data)
        escribir=""
    else:
        escribir=escribir+data
        


"""
seq_number_sv = (seq_number_sv + 1) % seq_max
try:
    data, address = connection.recvfrom(buff)

    if data:
"""

