# -*- coding: utf-8 -*-
"""
Graph Model with Routing Algorithm

@author: Thomas Treml (datadonk23@gmail.com)
Date: 16.02.2015
"""

import networkx as net
import matplotlib.pyplot as plt

# Directed graph model
G = net.DiGraph()

# node A
G.add_edge("A", "X", kind="asc", side="w")
G.node["A"]["side"] = "w"
# node B
G.add_edge("B", "X", kind="asc", side="w")
G.node["B"]["side"] = "w"
# node C
G.add_edge("C", "X", kind="asc", side="w")
G.node["C"]["side"] = "w"
# node D
G.add_edge("D", "X", kind="asc", side="w")
G.node["D"]["side"] = "w"
# node E
G.add_edge("E", "X", kind="asc", side="e")
G.node["E"]["side"] = "e"
# node F
G.add_edge("F", "X", kind="asc", side="e")
G.node["F"]["side"] = "e"
# node G
G.add_edge("G", "X", kind="asc", side="e")
G.node["G"]["side"] = "e"
# node H
G.add_edge("H", "X", kind="asc", side="e")
G.node["H"]["side"] = "e"
# node I
G.add_edge("I", "X", kind="asc", side="w")
G.node["I"]["side"] = "w"
#node X
G.add_edge("X", "A", kind="dsc", side="w")
G.add_edge("X", "B", kind="dsc", side="w")
G.add_edge("X", "C", kind="dsc", side="w")
G.add_edge("X", "D", kind="dsc", side="w")
G.add_edge("X", "E", kind="dsc", side="e")
G.add_edge("X", "F", kind="dsc", side="e")
G.add_edge("X", "G", kind="dsc", side="e")
G.add_edge("X", "H", kind="dsc", side="e")
G.add_edge("X", "I", kind="dsc", side="w")
G.node["X"]["side"] = "c"

# Drawing
plot1 = plt.figure()
ax1 = plot1.add_subplot(111)
pos = net.random_layout(G)
net.draw(G, pos=pos)
net.draw_networkx_labels(G, pos=pos)

# Routing algorithm
def find_route(graph=G, start="A"):
    """Finds best combination of cyling ascents in Damberg graph
    In: graph, start node
    Out: list of ascents and descents in best order
    """
    route = []
    nodes_w = []
    nodes_e = []
    start = start    
    
    # list of possible nodes for each side
    for node in graph.nodes(data=True):
        if node[1].get("side") == "w":
            nodes_w.append(node[0])
        elif node[1].get("side") == "e":
            nodes_e.append(node[0])
    
    # main logic: alterating between asc and desc on each side
    while (len(nodes_w) > 0 and len(nodes_e) > 0):
        # ascents                
        if len(graph.out_edges(start)) > 0:
            asc = graph.out_edges(start, data=True)[0]
            asc_side = asc[2]["side"]
        else:
            break
            
        route.append(asc)
        if asc[0] in nodes_w:
            nodes_w.remove(asc[0])
        elif asc[0] in nodes_e:
            nodes_e.remove(asc[0])
        graph.remove_edge(asc[0], asc[1])
    
        # descents        
        for edge in graph.out_edges("X", data=True):
            if edge[2]["side"] == asc_side:
                continue
            else:
                dsc = edge
        
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
    
    # last tracks when starting on west side
    if len(nodes_e) == 0 and len(nodes_w) == 1:
        asc = graph.out_edges(start, data=True)[0]
        asc_side = asc[2].get("side")            
        route.append(asc)
        graph.remove_edge(asc[0], asc[1])
    # last tracks logic when starting on east side
    elif len(nodes_w) > 0 and len(nodes_e) == 0:
        asc = graph.out_edges(start, data=True)[0]
        asc_side = asc[2].get("side")            
        route.append(asc)
        graph.remove_edge(asc[0], asc[1])
        nodes_w.pop()
        for edge in graph.out_edges("X", data=True):
            if edge[1] != nodes_w[0]:
                dsc = edge
                break
        route.append(dsc)
        graph.remove_edge(dsc[0], dsc[1])
        asc = graph.out_edges(nodes_w[0], data=True)[0]
        route.append(asc)
        graph.remove_edge(asc[0], asc[1])
        
    # exception for E
    else:
        start = nodes_e[0]        
        route.pop()
        for edge in graph.out_edges("X", data=True):
            if edge[2].get("side") == dsc_side:
                dsc = edge
        route.append(dsc)
        graph.remove_edge(dsc[0], dsc[1])
          
        asc = graph.out_edges(start, data=True)[0]
        asc_side = asc[2].get("side")            
        route.append(asc)
        graph.remove_edge(asc[0], asc[1])
        
        nodes_e.pop()
        for edge in graph.out_edges("X", data=True):
            if edge[1] != nodes_w[0]:
                dsc = edge
                break
        route.append(dsc)
        
        asc = graph.out_edges(nodes_w[1], data=True)[0]
        route.append(asc)
        graph.remove_edge(asc[0], asc[1])
        nodes_w.remove(asc[0])
        
        for edge in graph.out_edges("X", data=True):
            if edge[1] != nodes_w[0]:
                dsc = edge
                break
        route.append(dsc)
        
        asc = graph.out_edges(nodes_w[0], data=True)[0]
        route.append(asc)
    
    # ascent to top
    graph.add_edge("X", "S", kind="asc", side="c")
    for edge in graph.out_edges("X", data=True): 
        if edge[2].get("side") == "c":
            asc = edge
    route.append(asc)
           
    return route
    
route = find_route(start="C")

print "Route:"
for sector in route:
    print "from %s to %s" % (str(sector[0]), str(sector[1]))
