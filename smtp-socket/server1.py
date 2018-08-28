#!/usr/bin/python3

# SERVER 1

# https://github.com/iguit0/Redes-De-Computadores

import socket

serverhost1 = '127.0.0.1'
serverhost2 = '127.0.0.1'

serverport1 = 8000 # porta para cliente 1
serverport2 = 8001 # porta pro servidor 2

# O servidor 1 deve servir pro cliente 1
ServerSock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # cria um objeto socket
ServerSock1.bind(('', serverport1)) # liga o server 1 com a porta 1
ServerSock1.listen(1) # começa a escutar conexões

ServerSock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ServerSock2.connect((serverhost2, serverport2))

print('(*) Servidor 1 iniciado em ('+str(serverhost1)+':'+str(serverport1)+')')
while True:
    (NewClientSock1, addr1) = ServerSock1.accept()
    print('(@) Cliente conectou ' + str(addr1))
    ClientMessage = NewClientSock1.recv(1000)
    if ClientMessage:
        print('(#) Mensagem recebida do cliente --> '+ClientMessage.decode("utf-8"))
        NewClientSock1.send(ClientMessage)
    #server 1 conecta com server 2
    #server 1 agora se comporta como "cliente" para se conectar ao server 2
    print('\n(**) Enviando msg para server 2...')
    print('(OK) Mensagem enviada!')
    ServerSock2.send(ClientMessage) # mandou pro server 2

    NewClientSock1.close()
