#!/usr/bin/python3



import networkx as nx
import matplotlib.pyplot as plt

graph = { "s":{"y": 5, "t": 10},
          "t":{"y": 2, "x": 1},
          "y":{"t": 3, "z": 2, "x": 9},
          "z":{"s": 7, "x": 6},
          "x":{"z": 4}
        }

# plotando grafo original
G = nx.Graph(graph)
#pos = nx.spring_layout(G)
nx.draw(G, with_labels=True, node_size=450)
plt.show()

c_mini = {}
g_aux = {}
adj = {}
for i in graph:
    g_aux[i] = 99
    c_mini[i] = 99
p_ini = input('\tAresta de origem: ')
g_aux[p_ini] = 0
c_mini[p_ini] = 0
adj[p_ini] = 'None'
while g_aux:
    mini = list(min(zip(g_aux.values(), g_aux.keys())))
    mini_aresta = mini[1]
    adjs = [i for i in graph[mini_aresta].keys()]
    for i in adjs:
        if i in g_aux.keys():
            dist = c_mini[mini_aresta] + graph[mini_aresta][i]
            if dist < c_mini[i]:
                g_aux[i] = dist
                c_mini[i] = dist
                adj[i] = mini_aresta
    g_aux.pop(mini_aresta)
p_fin = input('\tAresta de destino: ')
path = []
path.append(p_fin)
p_aux = adj[p_fin]
while adj[p_aux] != 'None':
    path.append(p_aux)
    p_aux = adj[p_aux]
path.append(p_ini)
path.reverse()
print('--> Caminho mínimo: ',path)
print('--> Custo do caminho: ', c_mini[p_fin])
