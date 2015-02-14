# -*- coding: utf-8 -*-
"""
Graph Model

@author: Thomas Treml (datadonk23@gmail.com)
Date: 14.02.2015
"""

import networkx as net
import matplotlib.pyplot as plt

# Directed graph model
G = net.DiGraph()

# node A
G.add_edge("A", "X", kind="asc", side="w")
G.node["A"]["side"] = "w"
#G.add_edge("A", "B", kind="over", side="w")

# node B
G.add_edge("B", "X", kind="asc", side="w")
G.node["B"]["side"] = "w"
#G.add_edge("B", "C", kind="over", side="w")
#G.add_edge("B", "A", kind="over", side="w")

# node C
G.add_edge("C", "X", kind="asc", side="w")
G.node["C"]["side"] = "w"
#G.add_edge("C", "D", kind="over", side="w")
#G.add_edge("C", "B", kind="over", side="w")

# node D
G.add_edge("D", "X", kind="asc", side="w")
G.node["D"]["side"] = "w"
#G.add_edge("D", "C", kind="over", side="w")

# node E
G.add_edge("E", "X", kind="asc", side="e")
G.node["E"]["side"] = "e"
#G.add_edge("E", "F", kind="over", side="e")

# node F
G.add_edge("F", "X", kind="asc", side="e")
G.node["F"]["side"] = "e"
#G.add_edge("F", "G", kind="over", side="e")
#G.add_edge("F", "E", kind="over", side="e")

# node G
G.add_edge("G", "X", kind="asc", side="e")
G.node["G"]["side"] = "e"
#G.add_edge("G", "H", kind="over", side="e")
#G.add_edge("G", "F", kind="over", side="e")

# node H
G.add_edge("H", "X", kind="asc", side="e")
G.node["H"]["side"] = "e"
#G.add_edge("H", "E", kind="over", side="e")

#node X
G.add_edge("X", "A", kind="dsc", side="w")
G.add_edge("X", "B", kind="dsc", side="w")
G.add_edge("X", "C", kind="dsc", side="w")
G.add_edge("X", "D", kind="dsc", side="w")
G.add_edge("X", "E", kind="dsc", side="e")
G.add_edge("X", "F", kind="dsc", side="e")
G.add_edge("X", "G", kind="dsc", side="e")
G.add_edge("X", "H", kind="dsc", side="e")
G.node["X"]["side"] = "c"

# Drawing

plot1 = plt.figure()
ax1 = plot1.add_subplot(111)
pos = net.random_layout(G)
net.draw(G, pos=pos)
net.draw_networkx_labels(G, pos=pos)

# Routing Algorithm
def find_route(graph=G, start="A"):
    """Finds best combination (from most to least exhausting) of cyling 
       ascendends in given weighted graph and the starting node
    In: graph, start node
    Out: list of ascendents and descendents in best order
    """
    route = []
    
    start = start    
    
    for i in range(2):
        asc = graph.out_edges(start, data=True)[0]
        asc_side = asc[2]["side"]
            
        route.append(asc)
        graph.remove_edge(asc[0], asc[1])
    
        for edge in graph.out_edges("X", data=True):
            if edge[2]["side"] == asc_side:
                continue
            else:
                dsc = edge
    
        dsc_side = dsc[2]["side"]
        route.append(dsc)
        graph.remove_edge(dsc[0], dsc[1])
    
        for node in graph.nodes(data=True):
            if (dsc_side == node[1].get("side")) and (node[0] != dsc[1]):
                start = node[0]
                break
        #FIXME 2.loop
        i+=1
    
    route.append(start)
    return route
    
route = find_route()
