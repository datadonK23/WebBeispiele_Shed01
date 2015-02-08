# -*- coding: utf-8 -*-
"""
Graph Model

@author: Thomas Treml (datadonk23@gmail.com)
Date: 08.02.2015
"""

import networkx as net

# Einfaches Modell 5 Auffahrten
simpleG = net.Graph()

# node A
simpleG.add_edge("A", "B")
simpleG.add_edge("A", "C")
simpleG.add_edge("A", "D")
simpleG.add_edge("A", "E")


# node B
simpleG.add_edge("B", "A")
simpleG.add_edge("B", "C")
simpleG.add_edge("B", "D")
simpleG.add_edge("B", "E")

# node C
simpleG.add_edge("C", "A")
simpleG.add_edge("C", "B")
simpleG.add_edge("C", "D")
simpleG.add_edge("C", "E")

# node D
simpleG.add_edge("D", "A")
simpleG.add_edge("D", "B")
simpleG.add_edge("D", "C")
simpleG.add_edge("D", "E")

# node E
simpleG.add_edge("E", "A")
simpleG.add_edge("E", "B")
simpleG.add_edge("E", "C")
simpleG.add_edge("E", "D")


# Drawing
net.draw(simpleG)

# Analyse
if net.is_eulerian(simpleG):
    print list(net.eulerian_circuit(simpleG, source="B"))

