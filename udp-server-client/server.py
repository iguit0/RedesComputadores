#!/usr/bin/env python3
"""
                udp-server-client
https://github.com/iguit0/Redes-De-Computadores
"""

__author__ = "Igor Alves"
__version__ = "0.0.1"
__license__ = "GPL-3.0"

import socket

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

msgFromServer = "SERVIDOR RECEBEU!" # msg do servidor

UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # criacao objeto UDP

UDPServerSocket.bind((localIP, localPort)) # liga o servidor com a porta

print('\t\t\t(*) Server UDP iniciado em ',(localIP,localPort))
while True:
    (message, address) = UDPServerSocket.recvfrom(bufferSize) # recebe do cliente
    if message:
        message = message.decode() # descodifica a msg recebida
        message = format(message).upper() # msg em caixa alta

        clientIP = "\t(@) Cliente conectou: {}".format(address)
        clientMsg = "\n(#) Mensagem do Cliente: {}".format(message)

        print(clientIP)
        print(clientMsg)

        UDPServerSocket.sendto(msgFromServer.encode(), address) # enviando uma resposta ao cliente