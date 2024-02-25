import graph
import shortest_path as sp
import random

g = graph.Graph()

for i in range(1, 8):
    name = "node" + str(i)
    g.add_node(name)
    for j in range(1, i):
        name2 = "node" + str(j)
        g.add_edge(name, name2, random.randint(1, 10))
        g.add_edge(name2, name, random.randint(1, 10))

print(g)
name = "node4"
print(sp.init_path(g, name), sp.path_weight(g, sp.init_path(g, name)))

print(sp.optimal_path(g, name), sp.path_weight(g, sp.optimal_path(g, name)))

