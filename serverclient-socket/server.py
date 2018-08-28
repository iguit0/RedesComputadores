from jsonsocket import Server, Client


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

serverDomain = input('University:')
host = srvlist[serverDomain]['ip']
port = srvlist[serverDomain]['port']

server = Server(host, port)

msgList = []

while True:
	#print('\tNAME: ' + str(server.socket..gethostname()))
	#print('\tIP: ' + str(server.socket.gethostbyname(server.socket.gethostname())))
	#print('\tPORT:' + str(port))
	#print('\tSERVER: ' + str(emitterDomain))
	#server.accept()
	data = server.accept().recv()
	#data = server.recv()
	print(data)
	if data['act'] == 'send':
		server.send({'status': '200'})
		if data['recipientDomain'] == serverDomain:
			data['status'] = '202'
			msgList.append(data)
		print(msgList)
		if data['recipientDomain'] != serverDomain:
			print('Enviando mensagem para server: ' + str(data['recipientDomain']))
			client = Client()
			data['status'] = '201'
			response = client.connect(srvlist[data['recipientDomain']]['ip'], srvlist[data['recipientDomain']]['port']).send(data).recv()
			client.close()
			if response['status'] == '200':
				print('Mensagem Transmitida com Sucesso')
			else:
				print('Erro ao Transmitir Mensagem')
	if data['act'] == 'receive':
		requesterMsg = []
		for i in msgList:
			if i['recipientUser'] == data['requesterUser']:
				requesterMsg.append(i)
				msgList.remove(i)
		server.send(requesterMsg)


