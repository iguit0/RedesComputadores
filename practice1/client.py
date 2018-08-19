#!/usr/bin/python3
# coding: UTF-8

# Igor Alves (https://github.com/iguit0)

'''
    Cliente em Python usando biblioteca 'sockets'
    Como se conectar ao chat (no terminal):
    $ python client.py <IP_SERVER> <PORTA>
'''

import socket, sys, select, string

def prompt():
    sys.stdout.write('<Você> ')
    sys.stdout.flush()


if (len(sys.argv) < 3):
    print('\t\tERRO AO CONECTAR!')
    print('\t\tINSTRUÇÕES\n')
    print('\t$ python client.py <HOSTNAME> <PORT>\n')
    sys.exit()

host = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)

try:
    s.connect((host, port))
except:
    print('Erro de conexão!')
    sys.exit()

print('Conectado com o servidor!')
prompt()

while True:
    socket_list = [sys.stdin, s]

    read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

    for sock in read_sockets:
        # recebendo mensagens
        if sock == s:
            data = sock.recv(4096)
            if not data:
                print('\nErro de conexão!')
                sys.exit()
            else:
                sys.stdout.write(data)
                prompt()

        else:
            msg = sys.stdin.readline()
            s.send(msg)
            prompt()