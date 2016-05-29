import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from random import random


connections = []
dimension = random()*10

for i in range(int(dimension)):
    for j in range(int(dimension)):
        a = random()
        if a > 0.7:
            connections.append((i, j))

D = nx.DiGraph()
D.add_edges_from(connections)

nodes = len(D.nodes())

Matrix = [[0 for x in range(nodes)] for y in range(nodes)]
for (u, v, w) in D.edges(data=True):
    w['weight'] = round(np.random.random(), 2)
    Matrix[v][u] = w['weight']
    print('From {0} to {1}: {2}.'.format(u, v, w['weight']))

node_dict = {}
for (i, p) in D.nodes(data=True):
    p[i] = [np.random.random_integers(50), np.random.random_integers(50)]
    node_dict.update(p)
print("node_dict")
print(node_dict)


V = []
P = []
for i, j in node_dict.values():
    V.append(i)
    P.append(j)


print('P:', P)
print('Matrix : ', Matrix)
print('V :', V)


t = 30
W = [[0 for x in range(t)] for y in range(nodes)]
for i in range(t):
    for o in range(nodes):
        U = V[o]
        V[o] = V[o] + np.dot(P, Matrix[o])
        P[o] = V[o] - U
        W[o][i] = V[o]
    print(V)
    print(P)

plt.subplot(212)
pos = nx.spring_layout(D)

nx.draw(D, pos=pos, labels=node_dict, with_labels=True, node_size=1600, node_color='red', alpha=0.7, )

plt.figure(1)
plt.subplot(211)

for i in range(nodes):
    plt.plot(list(range(t)), W[i])

plt.show()
