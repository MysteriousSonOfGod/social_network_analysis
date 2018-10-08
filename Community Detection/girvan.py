import networkx as nx
import random
import matplotlib.pyplot as plt

def addEdges(G):
	i=0
	while(i<55):
		v1=random.randrange(15)
		v2=random.randrange(15)
		if(v1!=v2):
			G.add_edge(v1,v2)
			i+=1

def edge_to_remove(G):
	dict1 = nx.edge_betweenness_centrality(G)
	list_of_tuples = list(dict1.items())
	list_of_tuples.sort(key = lambda x:x[1], reverse=True)
	return list_of_tuples[0][0]


def girvan(G):
	c = list(nx.connected_component_subgraphs(G))
	l = len(c)
	print('The number of connected components are ',l)
	
	while(l==1):
		G.remove_edge(*edge_to_remove(G))
		c = list(nx.connected_component_subgraphs(G))
		l = len(c)
		print('The number of connected components are ',l)
	
	nx.draw(G)
	plt.show()
	
	for i in c:
		print(tuple(i))
	
	return c

G=nx.Graph()
G.add_nodes_from(list(range(0,15,1)))
addEdges(G)
c = girvan(G)
