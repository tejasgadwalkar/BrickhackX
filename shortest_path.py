import graph


def path_helper(g: graph.Graph, start, n_rest):
    """
    :param g: graph of Graph class
    :param start: starting node's name
    :param n_rest: list of nodes not in path already
    :return: the name of the node with the smallest weight
    """

    shortest = n_rest[0].name
    for node in n_rest:
        if g.get_weight(start, node.name) < g.get_weight(start, shortest):
            shortest = node.name
    return shortest


def init_path(g: graph.Graph, start):
    """
    :param g: graph of Graph class
    :param start: name of starting node
    :return: path of names by always choosing the shortest weight
    """
    n_rest = g.nodes
    n_rest.remove(start)
    path = [start]
    while n_rest:
        next_node = path_helper(g, start, n_rest)
        path += next_node
        start = next_node
        n_rest.remove(start)
    return path
