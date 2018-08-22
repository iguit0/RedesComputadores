#!/usr/bin/python3
# coding: UTF-8

# Igor Alves (https://github.com/iguit0)

import socket
import threading

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', 8000))
    sock.listen(10)

    connections = []

    def handler(c, a):
        global connections
        while True:
            data = c.recv(1024)
            for conn in connections:
                conn.send(bytes(data))
            if not data:
                connections.remove(c)
                c.close()
                break

    while True:
        c, a = sock.accept()
        cThread = threading.Thread(target=handler, args=(c,a))
        cThread.daemon = True
        cThread.start()
        connections.append(c)
        print(connections)