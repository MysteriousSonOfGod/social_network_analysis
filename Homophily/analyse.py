import networkx as nx
import matplotlib.pyplot as plt


def plot_density():
	x=[]
	y=[]
	for i in range(0,11):
		G=nx.read_gml('evolution_'+str(i)+'.gml')
		x.append(i)
		y.append(nx.density(G))
	plt.xlabel('time')
	plt.ylabel('density of graph')
	plt.title('Density Variation')
	plt.plot(x,y)
	plt.show()

def get_people(G):
	p=[]
	for each in G.nodes():
		if(G.node[each]['type']=='person'):
			p.append(each)
	return p

def obesity(G):
	obese=0
	pnodes=get_people(G)
	for i in pnodes:
		if(G.node[i]['name']>=35):
			obese+=1
	return obese

def plot_obesity():
	x=[]
	y=[]
	for i in range(0,11):
		G=nx.read_gml('evolution_'+str(i)+'.gml')
		x.append(i)
		y.append(obesity(G))
	plt.xlabel('time')
	plt.ylabel('number of obese')
	plt.title('Obesity in a network')
	plt.plot(x,y)
	plt.show()


plot_density()
plot_obesity()
