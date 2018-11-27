# -*- coding: utf-8 -*-
import socket
import sys
import os

if len(sys.argv) != 4:
    print "python server.py IPaddress PortNumber Filename"
    sys.exit()

# Parámetros
ip_Server = sys.argv[1]
port_Server = int(sys.argv[2])
filename = sys.argv[3]

# Ventana y tamaño de paquete
buff = 1024
window_Size = 100
window = []
"""
i = 0
while i < window_Size:
    window[i] = i
    i += 1
"""
# Header
seq_number = 0
ACK_Flag = 0
header = str(seq_number) + "|||" + str(ACK_Flag)