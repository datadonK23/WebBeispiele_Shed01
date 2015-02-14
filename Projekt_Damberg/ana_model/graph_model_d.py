# -*- coding: utf-8 -*-
"""
Graph Model without Culmination Point

@author: Thomas Treml (datadonk23@gmail.com)
Date: 14.02.2015
"""

#FIXME

import networkx as net
import matplotlib.pyplot as plt

# Gerichteter Graph
G = net.DiGraph()

# node A
G.add_edge("A", "H", side="w")
G.add_edge("A", "B", side="w")

# node B
G.add_edge("B", "G", side="w")
G.add_edge("B", "C", side="w")
G.add_edge("B", "A", side="w")

# node C
G.add_edge("C", "F", side="w")
G.add_edge("C", "D", side="w")
G.add_edge("C", "B", side="w")

# node D
G.add_edge("D", "E", side="w")
G.add_edge("D", "C", side="w")

# node E
G.add_edge("E", "D", side="e")
G.add_edge("E", "F", side="e")

# node F
G.add_edge("F", "C", side="e")
G.add_edge("F", "G", side="e")
G.add_edge("F", "E", side="e")

# node G
G.add_edge("G", "B", side="e")
G.add_edge("G", "H", side="e")
G.add_edge("G", "F", side="e")

# node H
G.add_edge("H", "A", side="e")
G.add_edge("H", "E", side="e")


# Drawing

plot1 = plt.figure()
ax1 = plot1.add_subplot(111)
pos = net.random_layout(G)
net.draw(G, pos=pos)
net.draw_networkx_labels(G, pos=pos)


# Routing Algorithm
def best_route(graph=G, start="A"):
    """Finds best combination (from most to least exhausting) of cyling 
       ascendends in given weighted graph and the starting node
    In: graph, start node
    Out: list of path tuples past by best track
    """
    route = []
    
    start = start    
    
    
    
    """nextN = sorted(graph.out_edges(start, data=True), key= lambda edge: edge[2],
                   reverse=True)    
    target = nextN[0][1]    
    path = net.dijkstra_path(graph, start, target)
    route.append(path)
    side = graph.get_edge_data(start, target)["side"]
    graph.remove_edge(path[0], path[1])
    
    for i in range(len(graph)-1):     
        nextN = sorted(graph.edges(data=True), key= lambda edge: edge[2],
                       reverse=True)
               
        if nextN[0][2]["side"] != side:
            if nextN[0][0] != target:
                start = nextN[0][0]
                target = nextN[0][1]
            else:
                start = nextN[1][0]
                target = nextN[1][1]
        else:
            for item in nextN:
                if item[2]["side"] == side:
                    continue
                else:
                    if item[0] != target:
                        start = item[0]
                        target = item[1]
                        break
                    else:
                        continue
        overpass = net.dijkstra_path(graph, path[1], start)
        route.append(overpass)
        path = net.dijkstra_path(graph, start, target)
        route.append(path)
        side = graph.get_edge_data(start, target)["side"]
        graph.remove_edge(path[0], path[1])
        i+=1
    
    route.append([path[1], "I"])
    route.append(["I", "S"])
"""
    
    return route
    
#route = best_route(start="C")
