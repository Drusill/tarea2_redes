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
address = (ip_Server, port_Server)

filename = sys.argv[3]
size_file = os.path.getsize(filename)
current_size = 0

# Ventana y tamaño de paquete
buff = 1024
window_Size = 10
window = []
seq_max = 2*window_Size 
seq_number = random.randint(0, seq_max)
print("seq_number: " + str(seq_number))

"""
i = 0
while i < window_Size:
    window[i] = i
    i += 1
"""


# Header

SYN = 1
data = str(filename) + "|||" + str(size_file) + "|||" + str(SYN) + "|||" + str(seq_max) + "|||" + str(seq_number) 


#   

try_connection = 0
print ("Establishing connection with " + str(address))
while try_connection < 5:
    connection.sendto(data, address)
    seq_number = (int(seq_number) + 1) % int(seq_max)
    connection.settimeout(0.5)
    try:
        if try_connection == 5:
            break

        data, adress = connection.recvfrom(buff)
        print(data)

        (SYN, ACK_Flag, ACK) = data.split("|||")
        if str(SYN) == "1" and str(ACK_Flag) == "1" and str(seq_number) == str(ACK):
            file_toSend = open(filename, "rb")
            print ("Connection established")
            break
    except:
        print(try_connection)
        try_connection += 1
        print ("timed out")
        connection.sendto(data, address)

if try_connection == 5:
    print ("Couldnt establish connection")
    sys.exit()


connection.close()
file_toSend.close()
"""
file_toSend = open(filename, "rb")
ACK = (ACK + 1) % seq_max
data = file_toSend.read(buff-1) + "|||" + str(ACK) + "|||" + 
        str(ACK_Flag) + "|||" str(seq_number)
current_size += len(data)

try_connection = 0
while True:
    connection.sendto(data, address)
    seq_number = (seq_number + 1) % seq_max
    connection.settimeout(0.5)
"""

