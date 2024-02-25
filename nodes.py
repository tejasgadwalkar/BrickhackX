class Node:
    def __init__(self, name):
        self.neighbors = []
        self.name = name
        self.status = ""
        self.number = ""

    def set_status(self, status):
        """
        Set the status to either "delivery" or "pickup"
        If invalid state was passed through as status, sets status to None

        For usage, first assert status is not None for node
        """
        if (status == "delivery" or status == "pickup"):
            self.status = status
        else:
            self.status = None

    def set_order_number(self, number):
        self.set_order_number = number

    def get_neighbors(self):
        return self.neighbors

    def add_neighbor(self, node):
        self.neighbors.append(node)

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return f"({self.name})"

