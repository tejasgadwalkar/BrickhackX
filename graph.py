import nodes


class Graph:

    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, node1, node2, weight):
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
