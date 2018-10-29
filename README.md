# Redes de Computadores :mag_right::globe_with_meridians::computer:
<img align="left" width="200" height="200" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Gnome-preferences-system-network.svg/200px-Gnome-preferences-system-network.svg.png">

O assunto **redes de computadores** é bastante vasto e complexo, envolvendo muitos conceitos, protocolos e tecnologias que se entrelaçam inextricavelmente. Neste repositório contém problemas propostos em sala para o estudo de redes. Baseado no livro [Redes de computadores e a internet uma abordagem *top-down*](https://www.amazon.com.br/Redes-Computadores-Internet-Abordagem-Top-Down/dp/8581436773) por [Jim Kurose](https://en.wikipedia.org/wiki/Jim_Kurose) e [Keith Ross](https://en.wikipedia.org/wiki/Keith_W._Ross).

Chat-Server :bust_in_silhouette::speech_balloon:
------
Servidor/Cliente usando biblioteca [*sockets*](https://pt.wikipedia.org/wiki/Soquete_de_rede) na qual recebe conexões de entrada (novos usuários) e dados (mensagens trocadas).
```
Como se conectar ao chat
$ python server.py
$ python client.py <IP_SERVER> <PORTA>
```

Simulador SMTP :mailbox_closed::inbox_tray:
------
Neste problema replicamos o [protocolo SMTP](https://pt.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol) utilizando [*sockets*](https://pt.wikipedia.org/wiki/Soquete_de_rede). Entenda o fluxo:<br/>
1. **[Client 1](./smtp-socket/client1.py) (Alice)** conecta no **[Server 1](./smtp-socket/server1.py)** (Servidor de correio de Alice) e envia *payload* (ou seja, sua mensagem).
2. **Server 1** age como "cliente" e se conecta no **Server 2** (Servidor de correio do Bob) e envia a mensagem de Alice.
3. **[Client 2](./smtp-socket/client2.py) (Bob)** se conecta no **[Server 2](./smtp-socket/server2.py)**, e então o mesmo envia a mensagem para Bob.
<br/>
<img align="center" src="http://imagem.b2s-space.com/upimg/60505/0/e235c8edfb.jpeg"><br/>

```
Rodar, respectivamente, nesta ordem: servidor 2, servidor 1, cliente 1 e cliente 2.
$ python server2.py
$ python server1.py
$ python cliente1.py
$ python cliente2.py
```

UDP RDT (Reliable Data Transfer) :package::thumbsup:
------
Com um canal confiável, nenhum dos dados transferidos é corrompido ou perdido, e todos são entregues na ordem em que foram enviados. É responsabilidade de um protocolo de transferência confiável de dados implementar essa abstração de serviço. A aplicação cliente-servidor implementada provê a transferência confiável baseado no protocolo rdt 2.2. Nesta versão do protocolo, não se usa implementa a detecção de perda de pacotes (tanto de dados quanto ACKs) por meio de um temporizador. Adicionando-se essa funcionalidade, teria-se o protocolo rdt 3.0 implementado

Caminho Mínimo de Roteamento (Dijkstra) :arrows_counterclockwise::soon:
------
O **[Caminho Mínimo de Roteamento](./CaminhoMinimoRoteamento/codigo.py)** é executado por cada nó de comutação na rede (isto é, nós preparados para encaminhar pacotes; na Internet, esses são chamados de roteadores). O conceito básico é que cada nó constrói um mapa da conectividade com a rede, na forma de um grafo, mostrando quais nós estão conectados a quais outros nós. Cada nó calcula, de forma independente, o melhor caminho lógico seguinte para cada destino possível na rede. Cada coleção de melhores caminhos formará a tabela de roteamento de cada nó. Sua essência é o algoritmo de Dijkstra.

```
Para executar, rode:
$ python codigo.py
```
