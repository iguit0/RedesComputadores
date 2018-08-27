#file:server.py
import numpy as np
from jsonsocket import Server, Client
import time

host = ''
port = 8081
srv = 2

srvlist = {
	"server1":
	{
		"id": 1,
		"ip": 'localhost',
		"port": "8080"
	},
	"server2":
	{
		"id": 2,
		"ip": 'localhost',
		"port": "8081"
	}
}

server = Server(host, port)

storemail = []

while True:
	#print('\tNAME: ' + str(server.socket..gethostname()))
	#print('\tIP: ' + str(server.socket.gethostbyname(server.socket.gethostname())))
	#print('\tPORT:' + str(port))
	print('\tSERVER: ' + str(srv))
	#server.accept()
	data = server.accept().recv()
	#data = server.recv()
	print(data)
	server.send({'status': 'ok'})
	if data['act'] == 'transfer':
		storemail.append(data)
	print(storemail)
	if data['dest'] != srv:
		print('Enviando mensagem para server: ' + str(data['dest']))
		client = Client()
		data['act'] = 'transfer'
		response = client.connect(host, 8081).send(data).recv()
		client.close()
		if response['status'] == 'ok':
			print('Mensagem Transmitida com Sucesso')
		else:
			print('Erro ao Transmitir Mensagem')

