#file:server.py
from jsonsocket import Server, Client
import time

host = 'localhost'
port = 8080
srv = '1'

server = Server(host, port)

while True:

	#server.accept()
	data = server.accept().recv()
	#data = server.recv()
	print(data)
	server.send({'status': 'ok'})
	dest = filter(lambda data: data['dest'] == srv, data)
	if dest:
		client = Client()
		data = data.update({'act': 'transfer'})
		response = client.connect(host, 8081).send(data).recv()
		print(response)
		client.close()
		time.sleep(10)
		server.close()
