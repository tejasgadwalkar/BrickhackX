import nodes
from math import ceil


class Graph:

    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, name):
        self.nodes.append(nodes.Node(name))

    def add_edge(self, name1, name2, weight):
        node1 = self.get_node(name1)
        node2 = self.get_node(name2)
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_neighbor(node2)
            self.edges.append([node1, node2, weight])

    def get_node(self, name):
        tmp = nodes.Node(name)
        for node in self.nodes:
            if node == tmp:
                return node

    def update_weight(self, name1, name2, weight):
        node1 = nodes.Node(name1)
        node2 = nodes.Node(name2)
        for edge in self.edges:
            if edge[0] == node1 and edge[1] == node2:
                edge[2] = weight

    def get_weight(self, name1, name2):
        node1 = nodes.Node(name1)
        node2 = nodes.Node(name2)
        for edge in self.edges:
            if edge[0] == node1 and edge[1] == node2:
                return edge[2]

    def shortest_path(self, start, end):
        node_s = nodes.Node(start)
        node_e = nodes.Node(end)
        # TODO
        return None

    def __str__(self):
        max_len = max([len(node.__str__()) for node in self.nodes])
        indent = ceil(max_len / 4) + 1

        string = "\t" * indent
        string = string + '\t'.join(map(lambda x: x.__str__(), self.nodes)) + '\n'

        for node in self.nodes:
            name = node.__str__()
            string += name + ('\t' * (indent - len(name)//4))
            for node2 in self.nodes:
                length = len(node2.name)
                weight = self.get_weight(node.name, node2.name)
                string += str(weight) if weight is not None else '0'
                string += '\t' * ceil(length / 4)
            string += '\n'
        return string
