#!/usr/bin/python3
# coding: UTF-8

# https://github.com/iguit0/Redes-De-Computadoress

import socket
import json
import sys

HOST = '200.18.132.6'
PORT = 8000

m = '{"id": 2, "name": "abc"}'

data = json.load(m)
type(data)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((HOST, PORT))
    sock.sendall(jsonObj)
    received = sock.recv(1024)
finally:
    sock.close()

print('Sent: {}'.format(data))
print('Received: {}'.format(received))


print('deu certo')
