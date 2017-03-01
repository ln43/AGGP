# -*- coding: utf-8 -*-
#///////////////////////////////////////////////////////////////////////
#////////////////////////// GRAPHES ////////////////////////////////////
#///////////////////////////////////////////////////////////////////////



#//////////////////////// IMPORTS //////////////////////////////////////
#///////////////////////////////////////////////////////////////////////
import networkx as nx
import numpy as np
#-----------------------------------------------------------------------

#///////////////////////// CLASSE //////////////////////////////////////
#///////////////////////////////////////////////////////////////////////
class Graphes:
  def __init__(self,n_,m_):
    self.n=n_ # Number of nodes
    self.m=m_ # Number of edges
    self.G=nx.gnm_random_graph(n_, m_)
    self.Pk=self.calcul_Pk()
    self.Ck=self.calcul_Ck()
    self.Dmin=self.calcul_Dmin()#retourne matrice avec min distance entre deux noeuds
  
  #///// P[k] = Nombre de noeuds de degre k / Nbr total de noeuds /////
  #///// Doit suivre une loi de puissance P(k) = k^(-gamma)       /////
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
    clust=nx.clustering(self.G)
    C=[0 for i in range(max(nx.degree(self.G).values())+1)]
    for c,i in nx.degree(self.G).items():
      C[i]+=nx.clustering(self.G,c)
    C=np.asarray(C)*1.0/nx.number_of_nodes(self.G)
    return C


  #///// Calcul du Dmin /////
  def calcul_Dmin(self):
			Dm=nx.shortest_path_length(self.G)
			#L=len(Dm)
			#l=len(Dm[1])
			#matrixMin=np.zeros((L,l))
			#for i in range(0,L):
			#	for j in range(0,l):
			#		matrixMin[i,j]=Dm[i][j] 
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
  
  #///// Calcul du cout /////
  def calcul_cout(self,gamma):
    statPk=self.stat_Pk(gamma)
    statCk=self.stat_Ck()
    #statchemin
    return statPk+statCk
    

