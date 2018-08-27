#!/usr/bin/python3

# SERVER 2

import socket

'''
json = {
    'statuscode': '',
    'timestamp': '',
    'message': ''
}
'''

serverhost1 = '127.0.0.1'
serverhost2 = '127.0.0.1'

serverport1 = 8000
serverport2 = 8001

ServerSock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ServerSock2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ServerSock2.bind(('', serverport2))
ServerSock2.listen(1)

print('(*) Servidor 2 iniciado em ('+str(serverhost2)+':'+str(serverport2)+')')

while True:
    (NewClientSock2, addr) = ServerSock2.accept()
    print('(@) Cliente conectou ' + str(addr))
    ClientMessage2 = NewClientSock2.recv(1000)
    if ClientMessage2 != '':
        print('(#) Mensagem recebida do cliente --> ' + ClientMessage2.decode("utf-8"))
        NewClientSock2.send(ClientMessage2)

NewClientSock2.close()