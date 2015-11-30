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
        #lambda represents the distance (or weight) between a node and a source node
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
        #find the node with smallest lambda and assign it to the u variable
        for v in G.nodes():
            if G.node[v]['lambda'] < smallest and G.node[v] in queue:
                smallest = G.node[v]['lambda']
                u = G.node[v]
        #delete su from the queue
        del queue[queue.index(u)]
        #checks all v neighbors of u
        for v in G.neighbors(u):
            #if v's lambda is greater than u's lamda plus the edge connecting u and v, update v's lambda
            #and make u the predecessor of v
            if G.node[v]['lambda'] > G.node[u]['lambda'] + G[u][v]['weight']:
                G.node[v]['lambda'] = G.node[u]['lambda'] + G[u][v]['weight']
                G.node[v]['predecessor'] = u
    #create a graph with the nodes of G
    new_graph = nx.create_empty_copy(G, with_nodes=True)
    #create the shortest-path trees using the predecessors
    for v, u, data in G.edges(data=True):
        if G.node[v]['predecessor'] is u or G.node[u]['predecessor'] is v:
            new_graph.add_edge(u, v, data)
    #create a list of predecessors
    predecessors = {}
    for v in G.nodes():
        predecessors[v] = G.node[v]['predecessor']
    #return the list of predecessors
    return new_graph, predecessors

