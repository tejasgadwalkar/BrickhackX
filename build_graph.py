import address as addr
import graph as g

def build_graph(addresses, pickup, number):
	mapGraph = g.Graph()
	for i in range(len(addresses)):
		mapGraph.add_node(addresses[i], pickup[i], int(number[i]))
	
	for node1 in mapGraph.nodes:
		for node2 in mapGraph.nodes:
			if (node1 == node2):
				continue
			else:
				weight = addr.get_driving_time(node1.name, node2.name)
				mapGraph.add_edge(node1.name, node2.name, weight)
	return mapGraph