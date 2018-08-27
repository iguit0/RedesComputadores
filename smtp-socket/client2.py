#!/usr/bin/python3

# CLIENTE 2

import socket
import json

serverhost2 = '127.0.0.1'
serverport2 = 8001

ClientSock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ClientSock2.connect((serverhost2, serverport2))
print('\t\t\t(@) Cliente 2')
msg2 = input('(#) Digite sua mensagem: ')

d2 = {
    "verb": "sendto",
    "payload": msg2
}

j2 = json.dumps(d2)

ClientSock2.send(j2.encode("utf-8"))
ServerMessage = ClientSock2.recv(1000)
print('(OK) Mensagem enviada!')
print('\tConteúdo da mensagem --> '+ServerMessage.decode('utf-8'))
ClientSock2.close()