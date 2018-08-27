#!/usr/bin/python3

# CLIENTE 1

import socket
import json

serverhost1 = '127.0.0.1'
serverport1 = 8000

ClientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ClientSock.connect((serverhost1, serverport1))
print('\t\t\t(@) Cliente 1')
msg = input('(#) Digite sua mensagem: ')

d = {
    "verb": "sendto",
    "payload": msg
}

j = json.dumps(d)

ClientSock.send(j.encode("utf-8"))
ServerMessage = ClientSock.recv(1000)
print('(OK) Mensagem enviada!')
print('\tConteúdo da mensagem --> '+ServerMessage.decode('utf-8'))
ClientSock.close()