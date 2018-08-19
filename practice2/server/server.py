#!/usr/bin/python3
# coding: UTF-8

import socket, json, select


class server:

	def __init__(self):
		return

	@staticmethod
	def open_connect():
		CONNECTION_LIST = []  # Mantém uma lista dos sockets ativos
		RECV_BUFFER = 4096  # tamanho do buffer arbitrário, especifica o máximo de dados a serem recebidos de uma só vez
		PORT = 8000  # porta a ser utilizada pelo servidor
		server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = ipv4 ||| SOCK_STREAM = TCP
		# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		server_socket.bind(('0.0.0.0', PORT))  # realiza a ligação
		server_socket.listen(10)  # aceita até 10 chamadas

		CONNECTION_LIST.append(server_socket)
		print('\tIP DO SERVIDOR: ' + str(socket.gethostbyname(socket.gethostname())) + ':' + str(PORT))
		print('\tNOME DO SERVIDOR: ' + str(socket.gethostname()))
		print('\nSERVIDOR DE CHAT INICIADO! :)')

		while True:
			read_sockets, write_sockets, error_sockets = select.select(CONNECTION_LIST, [], [])

			for sock in read_sockets:
				# nova conexão
				if sock == server_socket:
					sockfd, addr = server_socket.accept()
					CONNECTION_LIST.append(sockfd)
					print('Cliente (%s:%s) conectado' % addr)

					broadcast_data(sockfd, '[%s:%s] entrou na sala!\n' % addr)

				# mensagem recebida do cliente
				else:
					try:
						data = sock.recv(RECV_BUFFER)
						if data:
							broadcast_data(sock, '\r' + '<' + str(sock.getpeername()) + '> ' + data)
					except:
						broadcast_data(sock, 'Cliente (%s, %s) está offline' % addr)
						sock.close()
						CONNECTION_LIST.remove(sock)
						continue
						server_socket.close()  # fecha o servidor


	def broadcast_data(sock, message):
		for socket in CONNECTION_LIST:
			# se o soquete não for o servidor ou o cliente do qual a mensagem foi originada
			if socket != server_socket and socket != sock:
				try:
					socket.send(message)
				except:
					# caso a conexão do soquete estiver quebrada, fecha e remove
					socket.close()
					CONNECTION_LIST.remove(socket)