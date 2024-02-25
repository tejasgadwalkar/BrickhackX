import address as addr
import graph as g

def build_graph(addresses):
	mapGraph = g.Graph()
	for address in addresses:
		mapGraph.add_node(address)
	
	for node1 in mapGraph.nodes:
		for node2 in mapGraph.nodes:
			if (node1 == node2):
				continue
			else:
				weight = addr.get_driving_time(node1.name, node2.name)
				mapGraph.add_edge(node1.name, node2.name, weight)
	return mapGraph