import networkx as nx
import matplotlib.pyplot as plt
import random
import math
import time


def create_graph():
	G=nx.Graph()

	#G.add_nodes_from(range(1,101,1))
	for i in range(1,101,1):
		G.add_node(i)
	return G

##############################################################################
def visualize(G,t):
	labelDict=get_labels(G)
	nsize=get_size(G)
	color_array=get_colors(G)
	nx.draw(G,labels=labelDict,node_size=nsize,node_color=color_array)
	plt.savefig('evolution'+t+'.jpg')
	plt.clf()
	plt.cla()
	nx.write_gml(G,'evolution_'+str(t)+'.gml')

##############################################################################
def assign_bmi(G):
	for each in G.nodes():
		G.node[each]['name']=random.randint(10,50)
		G.node[each]['type']='person'

##############################################################################
def get_labels(G):
	dict1={}
	for each in G.nodes():
		dict1[each]=G.node[each]['name']
	return dict1

##############################################################################
def get_size(G):
	array1=[]
	for each in G.nodes():
		if(G.node[each]['type']=='person'):
			array1.append(G.node[each]['name']*20)
		else:
			array1.append(1000)
	return array1

##############################################################################	
def add_foci_nodes(G):
	n = G.number_of_nodes()
	i=n+1
	foci_nodes=['gym','eatout','movie_club','karate_club','yoga_club']
	for j in range(0,5):
		G.add_node(i)
		G.node[i]['name']=foci_nodes[j]
		G.node[i]['type']='foci'
		i+=1

##############################################################################
def get_colors(G):
	c=[]
	for each in G.nodes():
		if(G.node[each]['type']=='person'):
			if(G.node[each]['name']>=35):
				c.append('orange')
			elif(G.node[each]['name']<35 and G.node[each]['name']>=20):
				c.append('green')			
			else:
				c.append('yellow')
		else:
			c.append('blue')
	return c

##############################################################################
def get_foci(G):
	f=[]
	for each in G.nodes():
		if(G.node[each]['type']=='foci'):
			f.append(each)
	return f

##############################################################################
def get_people(G):
	p=[]
	for each in G.nodes():
		if(G.node[each]['type']=='person'):
			p.append(each)
	return p

##############################################################################
def add_foci_edges(G):
	f=get_foci(G)
	p=get_people(G)
	
	for each in p:
		r=random.choice(f)
		G.add_edge(each,r)

##############################################################################
def homophily(G):
	pnodes=get_people(G)
	for u in pnodes:
		for v in pnodes:
			if u!=v:
				diff=abs(G.node[u]['name']-G.node[v]['name'])
				p=float(1)/(diff+1000)
				r=random.uniform(0,1)
				if(r<p):
					G.add_edge(u,v)

##############################################################################
def cmn(u,v,G):
	un=set(G.neighbors(u))
	vn=set(G.neighbors(v))
	return len(un and vn)
	
##############################################################################
def closure(G):
	array1=[]
	for u in G.nodes():
		for v in G.nodes():
			if(u!=v and (G.node[u]['type']=='person' or G.node[v]['type']=='person')):
				k=cmn(u,v,G)
				p=1-math.pow((1-0.001),k)
				tmp=[]
				tmp.append(u)
				tmp.append(v)
				tmp.append(p)
				array1.append(tmp)

	for each in array1:
		u=each[0]
		v=each[1]
		p=each[2]
		r=random.uniform(0,1)
		if(r<p):
			G.add_edge(u,v)

##############################################################################
def change_bmi(G):
	fnodes=get_foci(G)
	for each in fnodes:
		if(G.node[each]['name']=='eatout'):
			for each1 in G.neighbors(each):
				if(G.node[each1]['name']!=50):
					G.node[each1]['name']+=1
		if(G.node[each]['name']=='gym'):
			for each1 in G.neighbors(each):
				if(G.node[each1]['name']!=10):
					G.node[each1]['name']-=1


G=create_graph()
assign_bmi(G)
add_foci_nodes(G)
add_foci_edges(G)
visualize(G,'0')

for t in range(0,10):
	homophily(G)
	closure(G)
	change_bmi(G)
	visualize(G,str(t+1))
