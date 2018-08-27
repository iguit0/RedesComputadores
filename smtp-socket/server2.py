#!/usr/bin/python3

# SERVER 2

import socket
import json

serverhost1 = '127.0.0.1'
serverhost2 = '127.0.0.1'

serverport1 = 8000
serverport2 = 8001

ServerSock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#ServerSock2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ServerSock2.bind(('', serverport2))
ServerSock2.listen(1)

print('(**) Servidor 2 iniciado em ('+str(serverhost2)+':'+str(serverport2)+')')
while True:
    (NewClientSock1, addr) = ServerSock2.accept()
    print('(@) Cliente conectou ' + str(addr))
    ClientMessage = NewClientSock1.recv(1000)
    if ClientMessage != '':
        d = json.loads(ClientMessage)
        print('(OK) Mensagem recebida!')
        print('\tConteúdo da mensagem --> ' , d)
        NewClientSock1.send(ClientMessage) # enviando confirmacao pro server

NewClientSock1.close()
ServerSock2.close()