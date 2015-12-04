#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Daniel Nobusada, João Vitor Brandão e Pedro Padoveze'
""" A Task 4 é a implementação do Twice Around the Tree.
"""

import networkx as nx
from prim import mst_prim
import numpy as np
import random


def twice_around(G):
    mst = mst_prim(G)
    di_mst = mst.to_directed()
    euler = nx.eulerian_circuit(di_mst,random.randint(0, len(G.nodes())-1)) # o problema está aqui
    edges = list(euler)

    weight = 0
    for i in edges:
        weight += G.edge[i[0]][i[1]]['weight']

    path = []
    for i in list(edges):
        if i[0] not in path:
            path.append(i[0])
        if i[1] not in path:
            path.append(i[1])
    return weight, path


if __name__ == "__main__":

    path = np.loadtxt('data/ha30_dist.txt')
    # Obtem as coordenadas em que o peso eh nao-nulo (diagonal principal)
    rows, cols= np.where(path > 0)
    # Obtem o peso de cada uma das arestas
    weight = [path[rows[i],cols[i]] for i in range(0, len(rows))]
    # Cria lista de arestas com e sem peso
    edges_with_weight = zip(rows.tolist(), cols.tolist(), weight)
    # Cria um grafo vazio usando a biblioteca NetworkX
    G = nx.Graph()
    # Insert nodes from an edge and it's weight
    for i in range(0, len(rows)):
        G.add_edge(edges_with_weight[i][0], edges_with_weight[i][1], weight=edges_with_weight[i][2])

    f = open('paths.txt','w')
    for i in range(10):
        weight, path = twice_around(G)
        string = "Caminho: " + str(path) + "\nPeso: " + str(weight) + "\n"
        f.write(string)
    f.close()
