#!/usr/bin/python3

# SERVER 1

import socket

serverhost1 = '127.0.0.1'
serverhost2 = '127.0.0.1'

serverport1 = 8000
serverport2 = 8001

ServerSock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ServerSock1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ServerSock1.bind(('', serverport1))
ServerSock1.listen(1)
print('(*) Servidor 1 iniciado em ('+str(serverhost1)+':'+str(serverport1)+')')

while True:
    (NewClientSock1, addr) = ServerSock1.accept()
    print('(@) Cliente conectou ' + str(addr))
    ClientMessage = NewClientSock1.recv(1000)
    if ClientMessage != '':
        print('(#) Mensagem recebida do cliente --> '+ClientMessage.decode("utf-8"))
        NewClientSock1.send(ClientMessage)
    #server 1 conecta com server 2
    #server 1 agora se comporta como "cliente" para se conectar ao server 2
    print('\nEnviando msg para server 2...')
    ServerClientSock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ServerClientSock1.connect((serverhost2, serverport2))
    ServerClientSock1.send(ClientMessage)
    ServerMessage = ServerClientSock1.recv(1000)
    print('(OK) Mensagem enviada!')
    print('\tConteúdo da mensagem --> ' + ServerMessage.decode('utf-8'))

NewClientSock1.close()
ServerClientSock1.close()
