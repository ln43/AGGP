#///////////////////////////////////////////////////////////////////////
#////////////////////////// GRAPHES ////////////////////////////////////
#///////////////////////////////////////////////////////////////////////



#//////////////////////// IMPORTS //////////////////////////////////////
#///////////////////////////////////////////////////////////////////////
import networkx as nx
import numpy as np

#///////////////////////// CLASSE //////////////////////////////////////
#///////////////////////////////////////////////////////////////////////
class Graphes:
  def __init__(self,n_,m_,x):
    self.n=n_ # Number of nodes
    self.m=m_ # Number of edges
    if x==1:
      self.G=nx.gnm_random_graph(n_, m_)
    else :
      self.G=nx.barabasi_albert_graph(n_, m_)
    print "Nb edges : ",nx.number_of_edges(self.G)
    self.Pk=self.calcul_Pk()
    self.Ck=self.calcul_Ck()
  
  def calcul_Pk(self):
    P=[0 for i in range(max(nx.degree(self.G).values())+1)]
    for i in nx.degree(self.G).values():
      P[i]+=1
    P=np.asarray(P)*1.0/nx.number_of_nodes(self.G)
    return P
  
  def calcul_Ck(self):
    clust=nx.clustering(self.G)
    C=[0 for i in range(max(nx.degree(self.G).values())+1)]
    for c,i in nx.degree(self.G).items():
      C[i]+=nx.clustering(self.G,c)
    C=np.asarray(C)*1.0/nx.number_of_nodes(self.G)
    return C
