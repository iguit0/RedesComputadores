#file:client.py
from jsonsocket import Client, Server
import time

srvlist = {
	"ufv":
	{
		"id": 1,
		"ip": 'localhost',
		"port": 8888
	},
	"ufla":
	{
		"id": 2,
		"ip": 'localhost',
		"port": 8889
	}
}

srv = input('University:')
host = srvlist[srv]['ip']
port = srvlist[srv]['port']

while True:
	print('Program Name\nType 1 for Send\nType 2 to Receive')
	menu = input('Option: ')
	if menu == '1':
		client = Client()
		user = input('User:')
		domain = input('University: ')
		msg = input('Message:')
		data = {
			'act': 'send',
			'domain': domain,
			'user': user,
			'msg': msg
		}
		print(data)
		response = client.connect(host, port).send(data).recv()
		client.close()
		if response['status'] == '200':
			print('Mensagem Transmitida com Sucesso')
		else:
			print('Erro ao Transmitir Mensagem')

	if menu == '2':
		server = Server(host, port)
		data = server.accept().recv()
		print(data)
		server.send({'status': 'ok'})
		server.close()