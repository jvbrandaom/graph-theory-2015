# -*- coding: utf-8 -*-

import networkx as nx
import random
import matplotlib.pyplot as plt
from dijkstra import *

def plot_weighted_graph(G, fig_index=1, fig_title='', sources=None, predecessors=None):
    """
    Description
    ---------
    Plots a weighted graph G.
    """
    colors = ['r', 'b', 'g']
    plt.figure(fig_index)
    plt.title(fig_title)
    #removes axis labels
    frame = plt.gca()
    frame.axes.get_xaxis().set_visible(False)
    frame.axes.get_yaxis().set_visible(False)

    names={}
    #reads file with names
    f = open("data/southern_women_names.txt")
    i = 1
    for line in f:
        names[i] = line.rstrip().replace('\"','')
        i += 1
    # get position of the nodes
    pos = nx.spring_layout(G);
    # plot nodes
    i = 0
    if sources is not None:
        nodelist = {}
        Q = G.nodes()
        for s in sources:
            nodelist[s] = [s]
            del Q[Q.index(s)]
        while Q:
            u = Q[0]
            temp = []
            del Q[Q.index(u)]
            while u is not None:
                temp.append(u)
                u = predecessors[u]

            for i in range(0, len(temp) - 1):
                    if temp[i] not in nodelist[temp[len(temp) - 1]]:
                        nodelist[temp[len(temp) - 1]].append(temp[i])
                    if temp[i] in Q:
                        del Q[Q.index(temp[i])]

        for k, v in nodelist.items():
            nx.draw_networkx_nodes(G, pos, node_size=1000, node_color=colors[i], nodelist=v)
            i += 1

        plt.legend([names[i] for i in sources], title="Sources", fontsize='small', scatterpoints = 1, markerscale=0.4)
    else:
        nx.draw_networkx_nodes(G, pos, node_size=1000, node_color=colors[i])
    # plot node labels
    nx.draw_networkx_labels(G, pos, names, font_size=6, font_family='sans-serif')
    # plot edges
    nx.draw_networkx_edges(G, pos);
    # get weight of the edges
    weights = { (u, v): data['weight'] for u, v, data in G.edges(data=True) }
    # plot weights of the edges
    nx.draw_networkx_edge_labels(
        G, pos, edge_labels=weights, font_size=12, font_family='sans-serif');

    #save G on img folder
    plt.savefig("img/" + fig_title + ".png")
    # plot G
    plt.show();
    # close window
    plt.close();

#init random number generator
random.seed()
#reads graph
G = nx.read_edgelist('data/southern_women_club.txt', nodetype=int, data=(('weight',float),));
plot_weighted_graph(G, 1, 'complete_graph')
#choose two distant source nodes. We are going to take nodes from the graph periphery
periphery = nx.periphery(G)
sources = random.sample(range(1, len(periphery)), 2)
H, predecessors = dijkstra(G, sources)
plot_weighted_graph(H, 2, 'two_sources', sources, predecessors)

sources = random.sample(range(1, len(G)), 3)
I, predecessors = dijkstra(G, sources)
plot_weighted_graph(I, 3, 'three_sources', sources, predecessors)

sources = random.sample(range(1, len(G)), 3)
I, predecessors = dijkstra(G, sources)
plot_weighted_graph(I, 4, 'another_three_sources', sources, predecessors)
#G = nx.read_gml('/home/joaovitor/astro-ph.gml')
#nx.draw_networkx(G)
#plot_weighted_graph(G);
