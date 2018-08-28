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

srv = input('University:')
host = srvlist[srv]['ip']
port = srvlist[srv]['port']

server = Server(host, port)

storemail = []

while True:
	#print('\tNAME: ' + str(server.socket..gethostname()))
	#print('\tIP: ' + str(server.socket.gethostbyname(server.socket.gethostname())))
	#print('\tPORT:' + str(port))
	#print('\tSERVER: ' + str(srv))
	#server.accept()
	data = server.accept().recv()
	#data = server.recv()
	print(data)
	server.send({'status': '200'})
	if data['domain'] == srv:
		data['status'] = '202'
		storemail.append(data)
	print(storemail)
	if data['domain'] != srv:
		print('Enviando mensagem para server: ' + str(data['domain']))
		client = Client()
		data['status'] = '201'
		hostDomain = data['domain']
		response = client.connect(srvlist[hostDomain]['ip'], srvlist[hostDomain]['port']).send(data).recv()
		client.close()
		if response['status'] == '200':
			print('Mensagem Transmitida com Sucesso')
		else:
			print('Erro ao Transmitir Mensagem')

