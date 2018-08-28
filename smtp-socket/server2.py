#!/usr/bin/python3

# SERVER 2

# https://github.com/iguit0/Redes-De-Computadores

import socket
import json

serverhost2 = '127.0.0.1'

serverport2 = 8001 # porta do srv 2
clientport = 8003 # porta que o cliente 2 vai dar connect

# criado objeto de conexao para que server1(cliente) se conecte ao server 2
ServerSock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ServerSock2.bind(('', serverport2))
ServerSock2.listen(1)

# Server 2 age como servidor mesmo e abre (em outra porta) pro cliente conectar
ClientSock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ClientSock2.bind(('',clientport))
ClientSock2.listen(1)

print('(**) Servidor 2 iniciado em ('+str(serverhost2)+':'+str(serverport2)+')')
while True:
    (NewClientSock1, addr2) = ServerSock2.accept()
    print('(@) Cliente conectou ' + str(addr2))
    ClientMessage = NewClientSock1.recv(1000)
    if ClientMessage:
        (NewClientSock2, addrCli) = ClientSock2.accept()
        d = json.loads(ClientMessage)
        print('(OK) Mensagem recebida!')
        print('\tConteúdo da mensagem --> ' , d)
        NewClientSock2.send(ClientMessage) # manda pro cliente 2