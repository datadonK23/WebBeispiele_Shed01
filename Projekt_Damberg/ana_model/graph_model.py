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

# node I
#G.add_edge("I", "X", kind="asc", side="e")
#G.node["I"]["side"] = "e"

#node X
G.add_edge("X", "A", kind="dsc", side="w")
G.add_edge("X", "B", kind="dsc", side="w")
G.add_edge("X", "C", kind="dsc", side="w")
G.add_edge("X", "D", kind="dsc", side="w")
G.add_edge("X", "E", kind="dsc", side="e")
G.add_edge("X", "F", kind="dsc", side="e")
G.add_edge("X", "G", kind="dsc", side="e")
G.add_edge("X", "H", kind="dsc", side="e")

#G.add_edge("X", "I", kind="dsc", side="e")

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
    nodes_w = []
    nodes_e = []
    sym = False if (len(G) % 2 == 0) else True
    
    # list of possible nodes
    for node in graph.nodes(data=True):
        if node[1].get("side") == "w":
            nodes_w.append(node[0])
        elif node[1].get("side") == "e":
            nodes_e.append(node[0])
    
    start = start
    skip_last = 3 if sym else 4
    
    # main logic
    for i in range(len(graph) - skip_last):
        # ascents        
        asc = graph.out_edges(start, data=True)[0]
        asc_side = asc[2]["side"]
            
        route.append(asc)
        if asc[0] in nodes_w:
            nodes_w.remove(asc[0])
        elif asc[0] in nodes_e:
            nodes_e.remove(asc[0])
        graph.remove_edge(asc[0], asc[1])
    
        for edge in graph.out_edges("X", data=True):
            if edge[2]["side"] == asc_side:
                continue
            else:
                dsc = edge
        # descents
        dsc_side = dsc[2]["side"]
        route.append(dsc)
        graph.remove_edge(dsc[0], dsc[1])
        
        # find next start node
        if dsc_side == "w":
            for node in nodes_w:
                if node != asc[0] and node != dsc[1]:
                    start = node
        elif dsc_side == "e":
            for node in nodes_e:
                if node != asc[0] and node != dsc[1]:
                    start = node
        i+=1
    
    # pop last descent for connectivity
    route.pop()
    print nodes_w
    print nodes_e
    print list(graph.out_edges("X", data=True))

#FIXME    
    
    # logic for last ascent and descent
    # last before ascent (for symetrical graphs) or third last (asymmetrical)
    for edge in graph.out_edges("X", data=True):
        if edge[2].get("side") == dsc_side:
            route.append(edge)
            graph.remove_edge(edge[0], edge[1])
            if dsc_side == "w":
                node = nodes_w[0]
                nodes_w.pop()
            else:
                node = nodes_e[0]
                nodes_e.pop()            
            asc = graph.out_edges(node, data=True)[0]
            asc_side = asc[2].get("side")            
            route.append(asc)
            graph.remove_edge(asc[0], asc[1])
    """
    if sym:
        # last descent
        dsc = graph.out_edges("X", data=True)[0]
        dsc_side = dsc[2].get("side")
        route.append(dsc)
        graph.remove_edge(dsc[0], dsc[1])
        node = nodes_w[0] if dsc_side == "w" else nodes_e[0]
        # last ascent        
        asc = graph.out_edges(node, data=True)[0]
        asc_side = asc[2].get("side")            
        route.append(asc)
        graph.remove_edge(asc[0], asc[1])
    else:
        # last 2 descents
        dsc_last_before = graph.out_edges("X", data=True)[0]    
        #dsc_last = graph.out_edges("X", data=True)[1]
        dsc_side = dsc_last_before[2].get("side")
        route.append(dsc_last_before)
        graph.remove_edge(dsc_last_before[0], dsc_last_before[1])
        if dsc_side == "w":
            node = nodes_w[1]
            nodes_w.pop()
        else:
            node = nodes_e[1]
            nodes_e.pop()
        asc = graph.out_edges(node, data=True)[0]
        asc_side = asc[2].get("side")
        route.append(asc)
        graph.remove_edge(asc[0], asc[1])
        # last descent        
        dsc = graph.out_edges("X", data=True)[0]
        route.append(dsc)
        graph.remove_edge(dsc[0], dsc[1])
        # last ascvent
        node = nodes_w[0] if dsc_side == "w" else nodes_e[0]
        asc = graph.out_edges(node, data=True)[0]
        route.append(asc)
        graph.remove_edge(asc[0], asc[1])
    """  
    return route
    
route = find_route(start="F")
