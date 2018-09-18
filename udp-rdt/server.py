#!/usr/bin/env python3
"""
                UDP-RDT
https://github.com/iguit0/Redes-De-Computadores
"""

__author__ = "Igor Alves"
__version__ = "0.0.1"
__license__ = "GPL-3.0"

import socket
import sys
import funcoes

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024 # tamanho do pacote

received_data = []
ordered_received_data = []
duplicated_data = []
corrupted_data = []

msgFromServer = "SERVIDOR RECEBEU!" # msg do servidor


#criando socket UDP
try:
    UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDPServerSocket.bind((localIP, localPort))
except socket.error:
    print("\nFalha ao criar o socket.")
    sys.exit()

print('\t\t\t(*) Servidor UDP iniciado em ',(localIP,localPort))

# para saber se é a primeira vez que passa pelo estado
oncethru = 0

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