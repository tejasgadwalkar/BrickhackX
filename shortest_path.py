import graph
import numpy as np

def permutations(array):
    if len(array) == 1:
        return [array]
    perms = []
    for i in range(len(array)):
        e = array[i]
        results = permutations(array[:i] + array[i+1:])
        for r in results:
            perms.append([e] + r)
    return perms


def path_weight(g, path):
    if len(path) == 1:
        return 0
    return g.get_weight(path[0], path[1]) + path_weight(g, path[1:])


def optimal_path(g, start, end):
    p = permutations(g.nodes)
    
    filtered = [i for i in filter(lambda x: x[0].name == start, p)]
    if (end is not None):
        filtered = [i for i in filtered if i[-1].name == end]

    delivery_filtered = []
    for j in filtered:
        pickupList = []
        if g.get_node(j).name == "pickup":
            pickupList.append(g.get_node(j).number)
        else:
            if g.get_node(j).number not in pickupList:
                continue
            else:
                delivery_filtered.append(j)

    mapped = [list(map(lambda x: x.name, i)) for i in delivery_filtered]
    path_lengths = [i for i in map(lambda x: path_weight(g, x), mapped)]
    return mapped[np.argmin(path_lengths)]


def path_helper(g, start, n_rest):
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


def init_path(g, start: str):
    """
    :param g: graph of Graph class
    :param start: name of starting node
    :return: path of names by always choosing the shortest weight
    """
    n_rest = [i for i in g.nodes]
    n_rest.remove(g.get_node(start))
    path = [start]
    while n_rest:
        next_node = path_helper(g, start, n_rest)
        path.append(next_node)
        start = next_node
        n_rest.remove(g.get_node(start))
    return path
