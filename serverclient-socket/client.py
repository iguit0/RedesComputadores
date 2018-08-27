#file:client.py
from jsonsocket import Client
import time

host = 'LOCALHOST'
port = 8080

data = {
	'act': 'send',
	'dest': 2,
	'msg': 'Bla bla bla bla bla'
}
while True:
	client = Client()
	print(data)
	response = client.connect(host, port).send(data).recv()
	print(response)
	if response == {'status': 'ok'}:
		print('Recebido com Sucesso')
	if response == {'status': 'error'}:
		print('eRRo')
	client.close()
	time.sleep(10)