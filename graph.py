import networkx as nx


def build_weighted_graph(n, weights):
    assert len(weights) == n * (n - 1) / 2
    graph = nx.Graph()
    k = 0
    for i in range(n):
        for j in range(i, n):
            graph.add_edge(i, j, weight=weights[k])
            k += 1
    return graph
