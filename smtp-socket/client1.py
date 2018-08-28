#!/usr/bin/python3

# CLIENTE 1

# https://github.com/iguit0/Redes-De-Computadores

import socket
import json
import datetime

serverhost1 = '127.0.0.1'
serverport1 = 8000

# criamos um objeto cliente para se conectar com o server 1
ClientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ClientSock.connect((serverhost1, serverport1)) # conecta com o servidor 1

print('\t\t\t(@) Cliente 1')
msg = input('(#) Digite sua mensagem: ')

d = {
    "verb": "sendto",
    "timestamp": str(datetime.datetime.now()),
    "payload": msg
}

j = json.dumps(d) # dumps() serializa o objeto

ClientSock.send(j.encode("utf-8"))
ServerMessage = ClientSock.recv(1000) # confirmacao do servidor (se chegou)
print('(OK) Mensagem enviada!')
print('\tConteúdo da mensagem --> '+ServerMessage.decode('utf-8'))

ClientSock.close()