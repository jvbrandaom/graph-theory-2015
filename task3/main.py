# -*- coding: utf-8 -*-

import networkx as nx
import random
import matplotlib.pyplot as plt
from dijkstra import *

def plot_weighted_graph(G, fig_index=1, fig_title="graph", sources=None, predecessors=None):
    """
    Description
    ---------
    Plots a weighted graph G.

    Parameters:
        :param G: a NetworkX graph
        :param fig_index: a integer to determine the window in which the graph is plotted
        :param fig_title: title of the figure that is going to be generated
        :param sources: list of sources used on Dijkstra algorithm
        :param predecessors: list of predecessors from Dijkstra algorithm
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
    i = 0
    '''
    Plotting each of the shortest-path trees with different colors is based on:
    https://github.com/Comp-UFSCar/graph-theory/blob/master/tasks/task4/src/plot_graph.py
    '''
    #Determine list of nodes linked to each of the sources
    if sources is not None:
        #dictionary where the key is a source node and the value is the list of nodes associated with this source node
        nodelist = {}
        #list with all the graph nodes
        Q = G.nodes()
        for s in sources:
            #put the source into its own list
            nodelist[s] = [s]
            #remove source from the list of nodes
            del Q[Q.index(s)]
        while Q:
            u = Q[0]
            temp = []
            #removes u from the list
            del Q[Q.index(u)]
            while u is not None:
                #insert u into a temporary list
                temp.append(u)
                #goes to u's predecessor
                u = predecessors[u]

            #last value of the list is the source
            #put nodes associated with the source into the dictionary
            for i in range(0, len(temp) - 1):
                    #avoid duplication of nodes
                    if temp[i] not in nodelist[temp[len(temp) - 1]]:
                        nodelist[temp[len(temp) - 1]].append(temp[i])
                    #removes node from the list
                    if temp[i] in Q:
                        del Q[Q.index(temp[i])]

        #plot nodes with different colors for each shortest-path tree
        for k, v in nodelist.items():
            nx.draw_networkx_nodes(G, pos, node_size=1000, node_color=colors[i], nodelist=v)
            i += 1

        plt.legend([names[i] for i in sources], title="Sources", fontsize='small', scatterpoints=1, markerscale=0.4)
    else:
        #plot nodes
        nx.draw_networkx_nodes(G, pos, node_size=1000, node_color=colors[i])
    # plot node labels
    nx.draw_networkx_labels(G, pos, names, font_size=6, font_family='sans-serif')
    # plot edges
    nx.draw_networkx_edges(G, pos);
    # get weight of the edges
    weights = {(u, v): data['weight'] for u, v, data in G.edges(data=True)}
    # plot weights of the edges
    nx.draw_networkx_edge_labels(
        G, pos, edge_labels=weights, font_size=12, font_family='sans-serif')

    #save G on img folder
    plt.savefig("img/" + fig_title + ".png")
    # plot G
    plt.show()
    # close window
    plt.close()

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
#choose 3 random source nodes
sources = random.sample(range(1, len(G)), 3)
I, predecessors = dijkstra(G, sources)
plot_weighted_graph(I, 3, 'three_sources', sources, predecessors)
#choose another 3 raomdon source nodes
sources = random.sample(range(1, len(G)), 3)
I, predecessors = dijkstra(G, sources)
plot_weighted_graph(I, 4, 'another_three_sources', sources, predecessors)