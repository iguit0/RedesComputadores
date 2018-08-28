#!/usr/bin/python3

# CLIENTE 2

# https://github.com/iguit0/Redes-De-Computadores

import socket
import json

serverhost2 = '127.0.0.1'

clientport = 8003

ClientSock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ClientSock2.connect((serverhost2, clientport)) #conecta na porta criada dedicada do "cliente" do server 2
print('\t\t\t(@) Cliente 2')

print('(WAIT) Esperando msg do cliente 1...')
ServerMessage2 = ClientSock2.recv(1000)
ClientSock2.send(ServerMessage2)
d2 = json.loads(ServerMessage2) # .loads() carrega e "descodifica" o objeto json
print('(OK) Mensagem recebida!')
print('\tConteúdo da mensagem --> ',d2)