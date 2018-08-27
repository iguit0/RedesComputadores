#!/usr/bin/python3

# CLIENTE 2

import socket
import json

serverhost1 = '127.0.0.1'
serverhost2 = '127.0.0.1'

serverport1 = 8000
serverport2 = 8001

ClientSock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ClientSock2.connect((serverhost1, serverport1))
print('\t\t\t(@) Cliente 2')
'''
msg2 = input('(#) Digite sua mensagem: ')

d2 = {
    "verb": "sendto",
    "payload": msg2
}

j2 = json.dumps(d2)

ClientSock2.send(j2.encode("utf-8"))
'''
while 1:
    print('(WAIT) Esperando msg do cliente 1...')
    ServerMessage2 = ClientSock2.recv(1000)
    d2 = json.loads(ServerMessage2)
    print('(OK) Mensagem recebida!')
    print('\tConteúdo da mensagem --> ',d2)
#print('(OK) Mensagem enviada!')
#print('\tConteúdo da mensagem --> '+ServerMessage.decode('utf-8'))

ClientSock2.close()