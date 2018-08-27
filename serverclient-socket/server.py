#file:server.py
from jsonsocket import Server
from jsonsocket import Client
import json

host = 'localhost'
port = 8080
srv = 1

server = Server(host, port)

while True:
	#server.accept()
	#data = server.recv()
	data = server.accept().recv()
	print(data)
	server.send({'status': 'ok'})
	a = any(d['dist'] == 2 for d in data)
	if a:
		client = Client()
		print(data)
		response = client.connect(host, 8081).send(data).recv()
		print(response)
		client.close()
		time.sleep(10)
