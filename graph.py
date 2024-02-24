import networkx as nx
import address as addr

def build_weighted_graph(graph: nx.Graph):
    # nodes = graph.nodes()
    # for name in [nodes[node]['name'] for node in nodes]:
    #     for neighbor in graph.neighbors(graph, name):
    #         weight = addr.get_driving_time(name, neighbor['name'])
    #        graph.add_edge(name, neighbor, weight = weight)

    nodes = graph.nodes()
    for node in nodes:
        neighbors = node

    return graph



def build_nodes(graph, addresses):
    for address in addresses:
        graph.add_nodes(address)



def build_graph(addresses):
    graph = nx.Graph()
    build_nodes(graph, addresses)



    return graph