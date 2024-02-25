class Node:
    def __init__(self, name):
        self.neighbors = []
        self.name = name

    def get_neighbors(self):
        return self.neighbors

    def add_neighbor(self, node):
        self.neighbors.append(node)

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return f"({self.name})"

