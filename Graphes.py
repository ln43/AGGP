# -*- coding: utf-8 -*-
#///////////////////////////////////////////////////////////////////////
#////////////////////////// GRAPHES ////////////////////////////////////
#///////////////////////////////////////////////////////////////////////



#//////////////////////// IMPORTS //////////////////////////////////////
#///////////////////////////////////////////////////////////////////////
import networkx as nx
import numpy as np
from math import log
#-----------------------------------------------------------------------

#///////////////////////// CLASSE //////////////////////////////////////
#///////////////////////////////////////////////////////////////////////
class Graphes:
  def __init__(self,n_,p_):
    self.n=n_ # Number of nodes
    #self.G=self.connected_Graph(nx.gnm_random_graph(self.n, self.m))
    self.G=self.connected_Graph(nx.barabasi_albert_graph(self.n, p_))
    #self.G=self.connected_Graph(nx.powerlaw_cluster_graph(self.n, 2,1))
    self.m=self.G.number_of_edges()			 # Number of edges
    self.Pk=self.calcul_Pk()
    self.Ck=self.calcul_Ck()
    self.Diam=self.calcul_Diam()#retourne diametre du graphe
  
  #///// P[k] = Nombre de noeuds de degre k / Nbr total de noeuds /////
  #///// Doit suivre une loi de puissance P(k) = k^(-gamma)       /////
  def calcul_Pk(self):
    P=[0 for i in range(max(nx.degree(self.G).values())+1)]
    for i in nx.degree(self.G).values():
      P[i]+=1
    P=np.asarray(P)*1.0/nx.number_of_nodes(self.G)
    return P
  
  #///// C[k] = Pour chaque degre k, moyenne sur les noeuds i de ce degre k                                                          /////
  #///// Moyenne sur i de (2*Nombre d’arêtes liant les nœuds adjacents de i entre eux / (degre du noeud k * (degre du noeud k - 1))) /////
  #///// Doit suivre une loi C(k) = k^(-1)                                                                                           /////
  def calcul_Ck(self):
    C=[0 for i in range(max(nx.degree(self.G).values())+1)]
    nb_noeud_deg_i=[0 for i in range(max(nx.degree(self.G).values())+1)]
    for c,i in nx.degree(self.G).items():
      C[i]+=nx.clustering(self.G,c)
      nb_noeud_deg_i[i]+=1 #nombre de noeud de degre i
    for i in range(len(C)):
      if nb_noeud_deg_i[i]!=0:
        C[i]=C[i]*1.0/nb_noeud_deg_i[i]
    return C


  #///// Calcul du Diametre /////
  # But : verifier propriete petit monde Diam doit etre egal a logN
  def calcul_Diam(self):
      Dm=nx.diameter(self.G)
      return Dm


  #///// Test statistique des Ck (modelise - theorique)**2 /////
  def stat_Ck(self):
    CKtheo=[0]*len(self.Ck)
    for i in range(1,len(self.Ck)):
      CKtheo[i]=i**(-1)
    X=[(self.Ck[i]-CKtheo[i])**2 for i in range(1,len(self.Ck))]
    Xsum=sum(X)
    return Xsum
  
  #///// Test statistique des Pk (modelise - theorique)**2 /////
  def stat_Pk(self,gamma):
    PKtheo=[0]*len(self.Pk)
    for i in range(1,len(self.Pk)):
      PKtheo[i]=i**(-gamma)
    X=[(self.Pk[i]-PKtheo[i])**2 for i in range(1,len(self.Pk))]
    Xsum=sum(X)
    return Xsum
  
  
  #///// Test statistique Diametre abs(logN -diam) /////
  def stat_Diam(self):
      N=self.n
      stat= abs(log(N)-self.Diam)
      return stat
  
  #///// Calcul du cout avec ponderation des 3 caracteristiques /////

  def calcul_cout(self,gamma, ponderation):
    statPk=self.stat_Pk(gamma)
    statCk=self.stat_Ck()
    statDiam=self.stat_Diam()
    return ponderation[0]*statPk+ponderation[1]*statCk+ ponderation[2]*statDiam
    
  def connected_Graph(self, Gr):
    if(nx.is_connected(Gr)):
      return Gr
    else :
      N=list(nx.connected_components(Gr))  
      for i in range(len(N)-1) :
								L1=len(list(N[i]))
								L2=len(list(N[i+1]))
								Gr.add_edge(list(N[i])[np.random.randint(0,L1)], list(N[i+1])[np.random.randint(0,L2)])
								self.m=Gr.number_of_edges()								
      return Gr
    
