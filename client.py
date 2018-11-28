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
seq_number = 2*window_Size 
seq_actual = random.randint(0, seq_number)
print("seq_actual: " + str(seq_actual))

"""
i = 0
while i < window_Size:
    window[i] = i
    i += 1
"""


# Header

SYN = 1
data = str(filename) + "|||" + str(size_file) + "|||" + str(SYN) + "|||" + str(seq_number) + "|||" + str(seq_actual) 


#   

try_connection = 0
print ("Establishing connection with " + str(address))
while try_connection < 5:
    connection.sendto(data, address)
    seq_actual = (int(seq_actual) + 1) % int(seq_number)
    connection.settimeout(0.5)
    try:
        if try_connection == 5:
            break

        received, adress = connection.recvfrom(buff)
        print(received)

        (SYN, ACK_Flag, ACK) = received.split("|||")
        if str(SYN) == "1" and str(ACK_Flag) == "1" and str(seq_actual) == str(ACK):
            file_toSend = open(filename, "rb")
            break
    except:
        print(try_connection)
        try_connection += 1
        print ("timed out")
        connection.sendto(received, address)

if try_connection == 5:
    print ("Couldnt establish connection")
    sys.exit()

# Confirmacion de recepcion 
data = str(ACK_Flag) + "|||" + str(ACK)
connection.sendto(data, address)
print ("Connection established")

# enviar archivo
print(ACK)
print(seq_actual)
try_counter = 0
last_added = 0
while True:
    while last_added < window_Size:
        data = file_toSend.read(buff-1)
        if not data:
            break

        data += "|||" + str(seq_actual)
        window.append(data)
        connection.sendto(data, address) 
        if last_added == 0:
            connection.settimeout(0.5)  
        seq_actual = (int(seq_actual) + 1) % int(seq_number)
        last_added += 1
    
    try:
        data, address = connection.recvfrom(buff)
        (ACK_Flag, ACK) = data.split("|||")
        if str(ACK_Flag) == "1":
            for data in window:
                seq_window = data.split("|||")[1]
                if int(seq_window) == int(ACK):
                    index_acked = window.index(data) + 1
                    window = window[index_acked:]
                    last_added = window_Size - index_acked
                    connection.settimeout(0.5)
                    break       
    except:
        for data in window:
            connection.sendto(data, address)

connection.close()
file_toSend.close()
"""
file_toSend = open(filename, "rb")
ACK = (ACK + 1) % seq_number
data = file_toSend.read(buff-1) + "|||" + str(ACK) + "|||" + 
        str(ACK_Flag) + "|||" str(seq_actual)
current_size += len(data)

try_connection = 0
while True:
    connection.sendto(data, address)
    seq_actual = (seq_actual + 1) % seq_number

    connection.settimeout(0.5)
"""

