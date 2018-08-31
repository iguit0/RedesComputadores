#!/usr/bin/env python3

# https://github.com/iguit0/Redes-De-Computadores

import socket

msgFromClient = input('Digite a mensagem: ')

serverAddressPort = ("127.0.0.1", 20001)

bufferSize = 1024

UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

UDPClientSocket.sendto(msgFromClient.encode(), serverAddressPort)

(msgFromServer, address) = UDPClientSocket.recvfrom(bufferSize)

msgFromServer = msgFromServer.decode()
msgFromServer = format(msgFromServer).upper()

print("Mensagem do servidor: {}".format(msgFromServer))

#print(msg)