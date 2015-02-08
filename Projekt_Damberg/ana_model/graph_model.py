# -*- coding: utf-8 -*-
"""
Graph Model

@author: Thomas Treml (datadonk23@gmail.com)
Date: 08.02.2015
"""

import networkx as net
import matplotlib.pyplot as plt

# Einfaches Modell 6 Auffahrten
simpleG6 = net.DiGraph()
simpleG5 = net.DiGraph()

# node A
simpleG6.add_edge("A", "D")
simpleG6.add_edge("A", "E")
simpleG6.add_edge("A", "F")

simpleG5.add_edge("A", "D")
simpleG5.add_edge("A", "E")

# node B
simpleG6.add_edge("B", "D")
simpleG6.add_edge("B", "E")
simpleG6.add_edge("B", "F")

simpleG5.add_edge("B", "D")
simpleG5.add_edge("B", "E")

# node C
simpleG6.add_edge("C", "D")
simpleG6.add_edge("C", "E")
simpleG6.add_edge("C", "F")

simpleG5.add_edge("C", "D")
simpleG5.add_edge("C", "E")

# node D
simpleG6.add_edge("D", "A")
simpleG6.add_edge("D", "B")
simpleG6.add_edge("D", "C")

simpleG5.add_edge("D", "A")
simpleG5.add_edge("D", "B")
simpleG5.add_edge("D", "C")

# node E
simpleG6.add_edge("E", "A")
simpleG6.add_edge("E", "B")
simpleG6.add_edge("E", "C")

simpleG5.add_edge("E", "A")
simpleG5.add_edge("E", "B")
simpleG5.add_edge("E", "C")

# node F
simpleG6.add_edge("F", "A")
simpleG6.add_edge("F", "B")
simpleG6.add_edge("F", "C")


# Drawing

plot1 = plt.figure()
ax1 = plot1.add_subplot(111)
net.draw(simpleG6, ax=ax1)

plot2 = plt.figure()
ax2 = plot2.add_subplot(111)
net.draw(simpleG5, ax=ax2)

# Analyse
if net.is_eulerian(simpleG6):
    print "6 Auffahrten: " + str(list(net.eulerian_circuit(simpleG6,
                                                           source="B")))
else:
    print "6: Kein Eulerweg"

if net.is_eulerian(simpleG5):
    print "5 Auffahrten: " + str(list(net.eulerian_circuit(simpleG5,
                                                           source="B")))
else:
    print "5: Kein Eulerweg"
