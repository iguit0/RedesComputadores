#file:client.py
from jsonsocket import Client, Server
import time

host = 'localhost'
port = 8080


while True:
	print('Program Name\nType 1 for Send\nType 2 to Receive')
	menu = input('Option: ')
	if menu == '1':
		client = Client()
		#dest = input('Destination: ')
		msg = input('Type your message:')
		data = {
			'act': 'send',
			'dest': 2,
			'msg': msg
		}
		print(data)
		response = client.connect(host, port).send(data).recv()
		client.close()
		if response['status'] == 'ok':
			print('Mensagem Transmitida com Sucesso')
		else:
			print('Erro ao Transmitir Mensagem')

	if menu == '2':
		server = Server(host, port)
		data = server.accept().recv()
		print(data)
		server.send({'status': 'ok'})
		server.close()