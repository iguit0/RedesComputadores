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

emitterDomain = input('University:')
emitterUser = input('Sur Username:')
host = srvlist[emitterDomain]['ip']
port = srvlist[emitterDomain]['port']

while True:
	client = Client()
	print('Program Name\nType 1 for Send\nType 2 to Receive')
	menu = input('Option: ')
	if menu == '1':
		recipientUser = input('To:')
		recipientDomain = input('University: ')
		msg = input('Message:')
		data = {
			'act': 'send',
			'recipientDomain': recipientDomain,
			'recipientUser': recipientUser,
			'msg': msg
		}
		response = client.connect(host, port).send(data).recv()
		client.close()
		if response['status'] == '200':
			print('Mensagem Transmitida com Sucesso')
		else:
			print('Erro ao Transmitir Mensagem')

	if menu == '2':
		data = {
			'act': 'receive',
			'requesterUser': emitterUser
		}
		response = client.connect(host, port).send(data).recv()
		print(response)
		client.close()
