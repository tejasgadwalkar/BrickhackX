import nodes
from math import ceil

class Graph:
    def __init__(self):
        """
        Initializes an empty graph instance
        Node list represents all nodes in the graph
        Edge list has all edges, stored in a three element list
            - Stored as [Node1, Node2, weight]
        """
        self.nodes = []
        self.edges = []

    def add_node(self, name):
        """
        Adds a new node to the graph with the given name.

        Parameters:
            name (str): The name of the node to be added.
        """
        self.nodes.append(nodes.Node(name))

    def add_edge(self, name1, name2, weight):
        """
        Adds a weighted edge between two nodes in the graph.

        Parameters:
            name1 (str): The name of the first node.
            name2 (str): The name of the second node.
            weight (float): The weight of the edge between the nodes.
        """
        node1 = self.get_node(name1)
        node2 = self.get_node(name2)
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_neighbor(node2)
            self.edges.append([node1, node2, weight])

    def get_node(self, name):
        """
        Retrieves a node from the graph based on its name.

        Parameters:
            name (str): The name of the node to retrieve.

        Returns:
            Node: The node object with the specified name, if it exists in the graph.
        """
        tmp = nodes.Node(name)
        for node in self.nodes:
            if node == tmp:
                return node

    def update_weight(self, name1, name2, weight):
        """
        Updates the weight of an existing edge between two nodes.

        Parameters:
            name1 (str): The name of the first node.
            name2 (str): The name of the second node.
            weight (float): The new weight for the edge.
        """
        node1 = nodes.Node(name1)
        node2 = nodes.Node(name2)
        for edge in self.edges:
            if edge[0] == node1 and edge[1] == node2:
                edge[2] = weight

    def get_weight(self, name1, name2):
        """
        Retrieves the weight of the edge between two nodes.

        Parameters:
            name1 (str): The name of the first node.
            name2 (str): The name of the second node.

        Returns:
            float: The weight of the edge between the specified nodes,
                   or 0 if the nodes are the same.
        """
        if (name1 == name2):
            return 0
        node1 = nodes.Node(name1)
        node2 = nodes.Node(name2)
        for edge in self.edges:
            if edge[0] == node1 and edge[1] == node2:
                return edge[2]

    def shortest_path(self, start, end):
        """
        Finds the shortest path between two nodes in the graph using TODO ALGORITHM.

        Parameters:
            start (str): The name of the starting node.
            end (str): The name of the ending node.

        Returns:
            list or None: A list representing the shortest path from the `start` node to the `end` node,
                          or None if no path exists.
        """
        node_s = nodes.Node(start)
        node_e = nodes.Node(end)
        # TODO
        # TODO POTENTIALLY DONT NEED END NODE, DEPENDS ON IMPLEMENTATION
        return None

    def __str__(self):
        """
        Returns a string representation of the graph, showing nodes and their connections with weights.

        Returns:
            str: A string representation of the graph in an adjacency matrix format.
        """
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
                string += str(weight)
                string += ('\t' * ceil(length/4))
            string += '\n'
        return string
    
