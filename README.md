# Redes de Computadores :mag_right::computer:
<img align="left" width="200" height="200" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Gnome-preferences-system-network.svg/200px-Gnome-preferences-system-network.svg.png">
O assunto rede de computadores é bastante vasto e complexo, envolvendo muitos conceitos, protocolos e
tecnologias que se entrelaçam inextricavelmente. Neste repositório contém problemas propostos em sala (e laboratório) para o estudo de redes. Além de ter como base teórica (e prática) o livro "Redes de computadores e a internet uma abordagem top-down" por Jim Kurose e Keith Ross.

Chat-Server :bust_in_silhouette::speech_balloon:
------
Servidor/Cliente usando biblioteca *sockets* na qual recebe conexões de entrada (novos usuários) e dados (mensagens trocadas).
```
Como se conectar ao chat
$ python server.py
$ python client.py <IP_SERVER> <PORTA>
```

Simulador SMTP :mailbox_closed::mailbox_with_no_mail:
------
Simulando protocolo SMTP utilizando *sockets* e a ideia de cliente/servidor.
Cliente 1 conecta no server 1 e envia payload. Server 1 serve o cliente 1.
Server 2 serve o "cliente" do server 1 e depois serve para o cliente 2 se conectar a ele.
```
Rodar, respectivamente, nesta ordem: servidor 2, servidor 1, cliente 1 e cliente 2.
$ python server2.py
$ python server1.py
$ python cliente1.py
$ python cliente2.py
```
