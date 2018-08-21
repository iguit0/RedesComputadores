#!/usr/bin/python3
# coding: UTF-8

# https://github.com/iguit0/Redes-De-Computadores

import socket

def start_server():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print('Socket criado')

    try:
        soc.bind(('', 8000))
        print('Socket ligado')
    except socket.error as msg:
        import sys
        print('Bind failed. Error : ' + str(sys.exc_info()))
        sys.exit()

    soc.listen(10)
    print('Socket escutando na porta 8000')

    from threading import Thread

    while True:
        conn, addr = soc.accept()
        ip, port = str(addr[0]), str(addr[1])
        print('Aceitou conexão de ' + ip + ':' + port)
        try:
            print('ok')
            #Thread(target=client_thread, args=(conn, ip, port)).start()
        except:
            import traceback
            print("Terrible error!")
            traceback.print_exc()
    soc.close()

start_server()
