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
i=0

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

    if not message:
        break

    i+=1
    print("\n------------------------------------------")
    print("\tEnvio do", i, "º pacote")
    print("------------------------------------------")

    # Extraindo dados do pacote
	portaorigem = int(message[0:16],2)
	portadestino = int(message[16:32],2)
	comprimento = int(message[32:48],2)
	checksum = int(message[48:64],2)
	seq = int(message[64:65],2)
	dadoanterior = dado
	dado = int(message[65:97],2)

    soma = funcoes.checksum(portaorigem, portadestino, comprimento)

    if seq == 1:
        print("\nPacote ["+str(dadoanterior)+"] duplicado! Descartando e re-solicitando...")
        corrupted_data.append(dadoanterior)
    if soma != checksum:
        print("\nPacote [" + str(dado) + "] com erro de bits! Descartando e re-solicitando...")
        corrupted_data.append(dado)

    while seq == 1 or soma != checksum:
        if oncethru == 1:
            try:
            # Enviando mensagem ao cliente informando pacote duplicado/corrompido
                UDPServerSocket.sendto(message, address)
            except socket.error as msg:
                print("\nErro: " + str(msg) + "...")
                sys.exit()


    if message:
        message = message.decode() # descodifica a msg recebida
        message = format(message).upper() # msg em caixa alta

        clientIP = "\t(@) Cliente conectou: {}".format(address)
        clientMsg = "\n(#) Mensagem do Cliente: {}".format(message)

        print(clientIP)
        print(clientMsg)

        # enviando uma resposta ao cliente
        UDPServerSocket.sendto(msgFromServer.encode(), address)
