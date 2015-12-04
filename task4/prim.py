#!/usr/bin/env python
# -*- coding: utf-8 -*-

import networkx as nx
import random

__author__ = 'Daniel Nobusada, João Vitor Brandão e Pedro Padoveze'

def mst_prim(g):
    """
        O algoritmo de Prim inicia em um nó aleatório e adiciona arestas de menor custo que sai do conjunto de nós
            visitados e chega no conjunto de nós não visitados.
    :param g: Um grafo com peso nas arestas
    :return mst: Uma árvore geradora mínima (MST)
    """
    mst = nx.Graph()
    nodes = g.nodes()
    visited_node = []
    selected_node = nodes[random.randint(0, len(nodes)-1)]
    mst.add_node(selected_node)
    neighbors = nx.DiGraph()

    while len(mst.nodes()) < len(g.nodes()):
        visited_node.append(selected_node)

        neighbors.add_node(selected_node)
        new_edges = [edge for edge in g.edges(selected_node, 'weight') if edge[1] not in visited_node]
        neighbors.add_weighted_edges_from(new_edges)

        # Processo para obtenção da aresta de menor peso
        lightest = neighbors.edges(data='weight')[0]
        for edge in neighbors.edges(data='weight'):
            if edge[2] < lightest[2]:
                lightest = edge

        mst.add_weighted_edges_from([lightest])
        selected_node = lightest[1]

        remove_edges = [i for i in neighbors.edges() if i[1] == selected_node]
        neighbors.remove_edges_from(remove_edges)

    return mst