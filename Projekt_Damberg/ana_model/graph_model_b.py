# -*- coding: utf-8 -*-
"""
Graph Model

@author: Thomas Treml (datadonk23@gmail.com)
Date: 13.02.2015
"""

import networkx as net
import matplotlib.pyplot as plt

# Gerichteter Graph
G = net.DiGraph()

# node A
G.add_edge("A", "X", weight=5)
G.add_edge("A", "B", weight=100)

# node B
G.add_edge("B", "X", weight=9)
G.add_edge("B", "A", weight=100)
G.add_edge("B", "C", weight=100)

# node C
G.add_edge("C", "X", weight=1)
G.add_edge("C", "B", weight=100)
G.add_edge("C", "D", weight=100)

# node D
G.add_edge("D", "X", weight=8)
G.add_edge("D", "C", weight=100)
G.add_edge("D", "I", weight=100)

# node E
G.add_edge("E", "X", weight=2)
G.add_edge("E", "F", weight=100)

# node F
G.add_edge("F", "X", weight=7)
G.add_edge("F", "E", weight=100)
G.add_edge("F", "G", weight=100)

# node G
G.add_edge("G", "X", weight=4)
G.add_edge("G", "F", weight=100)
G.add_edge("G", "H", weight=100)

# node H
G.add_edge("H", "X", weight=3)
G.add_edge("H", "G", weight=100)
G.add_edge("H", "I", weight=100)

# node I
G.add_edge("I", "X", weight=6)
G.add_edge("I", "H", weight=100)
G.add_edge("I", "D", weight=100)

# node X
G.add_edge("X", "A", weight=10)
G.add_edge("X", "B", weight=10)
G.add_edge("X", "C", weight=10)
G.add_edge("X", "D", weight=10)
G.add_edge("X", "E", weight=10)
G.add_edge("X", "F", weight=10)
G.add_edge("X", "G", weight=10)
G.add_edge("X", "H", weight=10)
G.add_edge("X", "I", weight=10)


# Drawing

plot1 = plt.figure()
ax1 = plot1.add_subplot(111)
pos = net.spring_layout(G)
net.draw(G, pos=pos)
net.draw_networkx_labels(G, pos=pos)


# Routing Algorithm
def best_route(graph=G, culm="X"):
    """Finds best combination (from most to least exhausting) of cyling 
       ascendends in given weighted graph
    In: graph, culmination point
    Out: list of path tuples past by best track
    """
    route = []
    
    while (len(graph) > 1):
        nextN = sorted(graph.edges(data=True), key= lambda edge: edge[2])[0][0]
        asc = net.dijkstra_path(graph, nextN, culm)
        graph.remove_node(asc[0])
        route.append(asc)
        
        if (len(graph.edges()) > 1):
            nextN = sorted(graph.edges(data=True),
                           key= lambda edge: edge[2])[0][0]
            # FIXME anderer Knoten
            dsc = net.dijkstra_path(graph, culm, nextN)
            route.append(dsc)
    
    asc_top = ("X", "S")    
    route.append(asc_top)
    
    return route
    
route = best_route()

