#!/usr/bin/env python3

# https://github.com/iguit0/Redes-De-Computadores

import socket

localIP = "127.0.0.1"

localPort = 20001

bufferSize = 1024

msgFromServer = "SERVIDOR RECEBEU"

UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #criacao objeto udp

UDPServerSocket.bind((localIP, localPort)) # liga o servidor com a porta

print('(*) Server UDP iniciado em ',(localIP,localPort))
while True:
    (message, address) = UDPServerSocket.recvfrom(bufferSize) # recebe do cliente

    message = message.decode()

    message = format(message).upper()
    clientMsg = "(#) Mensagem do Cliente: {}".format(message)
    clientIP = "(@) Cliente conectou: {}".format(address)

    print(clientIP)
    print(clientMsg)

    UDPServerSocket.sendto(msgFromServer.encode(), address) # enviando uma resposta ao cliente