import networkx as nx


def dijkstra(G, source):
    '''

    :param G: a NetworkX graph
    :param source: source node of Dijkstra algorithm or list of source nodes
    :return: new_graph, predecessors
             shortest-path tree and list of predecessors
    '''
    queue = G.nodes() #priority queue

    #Init other nodes
    for v in G.nodes():
        G.node[v]['lambda'] = float('inf')
        G.node[v]['predecessor'] = None

    #Init sources with 0
    if (type(source) is int):
        G.node[source]['lambda'] = 0
    else:
        for v in source:
            G.node[v]['lambda'] = 0

    while queue:
        smallest = float('inf')
        u = queue[0]
        for v in G.nodes():
            if G.node[v]['lambda'] < smallest and G.node[v] in queue:
                smallest = G.node[v]['lambda']
                u = G.node[v]

        del queue[queue.index(u)]

        for v in G.neighbors(u):
            if G.node[v]['lambda'] > G.node[u]['lambda'] + G[u][v]['weight']:
                G.node[v]['lambda'] = G.node[u]['lambda'] + G[u][v]['weight']
                G.node[v]['predecessor'] = u

    new_graph = nx.create_empty_copy(G, with_nodes=True)

    for v, u, data in G.edges(data=True):
        if G.node[v]['predecessor'] is u or G.node[u]['predecessor'] is v:
            new_graph.add_edge(u, v, data)

    predecessors = {}
    for v in G.nodes():
        predecessors[v] = G.node[v]['predecessor']

    return new_graph, predecessors

