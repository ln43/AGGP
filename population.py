# -*- coding: utf-8 -*-
#///////////////////////////////////////////////////////////////////////
#////////////////////////// POPULATION /////////////////////////////////
#///////////////////////////////////////////////////////////////////////

#///// IMPORTS /////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////
from Graphes import Graphes
import numpy as np
import networkx as nx

#///// LA CLASSE ET SES METHODES ///////////////////////////////////////
#///////////////////////////////////////////////////////////////////////

class population :   
    def __init__(self, listGraph_, gamma_,seuilSelection_,pCrois_,pMut_) :
        self.pop = listGraph_ # Number of nodes
        self.pCrois = pCrois_
        self.pMut = pMut_
        self.Npop=len(self.pop)
        self.gamma=gamma_
        self.seuilSelection = seuilSelection_  #Seuil de selection

     
    def calculFitness(self, ponderation):
        fitnessPop = []
        for i in xrange(len(self.pop)) :
            fitnessPop.append(self.pop[i].calcul_cout(self.gamma, ponderation))
        return fitnessPop
    
    #///// Tri des fitness de la population ///// 
    def triFitness(self, ponderation):
        fitnessPop = self.calculFitness(ponderation)
        index = np.argsort(fitnessPop) #Indices des genomes dans ordre croissant
        popTriee = []                              #Tableau des genomes de la population triee, TxN
        for j in xrange(len(self.pop)) :
            popTriee.append(self.pop[index[j]])
        return popTriee                           #Classes dans ordre croissant de cout


    #///// Selection des plus mauvaises fitness de la population pour les ameliorer ///// 
    def selectionPiresFitness(self,ponderation):
        popSelectionnee = []      #Tableau des genomes de la population selectionnee TxNs
        for i in range(self.seuilSelection) :
            popSelectionnee.append(self.pop[self.Npop-1-i])   #Selectionne les cout les plus eleves
        return popSelectionnee
            
    def croisement(self,ponderation):
        print "Croisement"
        popSelectionnee = self.selectionPiresFitness(ponderation)
        for g in popSelectionnee:
          proba=np.random.random()
          if proba<self.pCrois:
            i=np.random.randint(0,len(popSelectionnee))
            while (popSelectionnee[i]==g):
              i=np.random.randint(0,len(popSelectionnee))
            g2=popSelectionnee[i]
            noeuds1=np.random.choice(g.G.nodes(),int(g.n/2),replace=False)
            noeudsopp1=filter(lambda x: x not in noeuds1, g.G.nodes())
            m1=g.m-nx.number_of_edges(g.G.subgraph(noeuds1))
            
            mapping={}
            for i in range(g2.n):
              mapping[i]=i+g.n
            g2.G=nx.relabel_nodes(g2.G,mapping)
            
            noeuds2=np.random.choice(g2.G.nodes(),int(g2.n/2),replace=False)
            noeudsopp2=filter(lambda x: x not in noeuds2, g2.G.nodes())
            m2=g2.m-nx.number_of_edges(g2.G.subgraph(noeuds2))
            
            newg1=nx.compose(g.G.subgraph(noeuds1),g2.G.subgraph(noeudsopp2))
            newg2=nx.compose(g2.G.subgraph(noeuds2),g.G.subgraph(noeudsopp1))
            
            i=0
            while i<m1 and nx.number_of_edges(newg1)<(nx.number_of_nodes(newg1)*(nx.number_of_nodes(newg1)-1)/2):
              e=(np.random.choice(noeuds1,1),np.random.choice(noeudsopp2,1))
              if e not in newg1.edges():
                newg1.add_edge(int(e[0]),int(e[1]))
                i=i+1    
            g.G=nx.convert_node_labels_to_integers(newg1)
            g.G=g.connected_Graph(g.G)
            g.n,g.m=nx.number_of_nodes(g.G),nx.number_of_edges(g.G)
            
            i=0
            while i<m2 and nx.number_of_edges(newg2)<(nx.number_of_nodes(newg2)*(nx.number_of_nodes(newg2)-1)/2):
              e=(np.random.choice(noeuds2,1),np.random.choice(noeudsopp1,1))
              if e not in newg2.edges():
                newg2.add_edge(int(e[0]),int(e[1]))
                i=i+1     
            g2.G=nx.convert_node_labels_to_integers(newg2)
            g2.G=g2.connected_Graph(g2.G)
            g2.n,g2.m=nx.number_of_nodes(g2.G),nx.number_of_edges(g2.G)
        return popSelectionnee
        
    def mutation(self,popCroisee,k):
      print "Mutation"
      for ind in popCroisee:            #Pour chaque individu selectionne
        if np.random.random()<self.pMut: #Tirage de la probabilite de muter
          ind.G.add_node(ind.n)
          Deg=0
          for d in ind.G.degree().values():
            Deg=Deg+d
          ind.G.add_node(ind.n)
          ind.n=ind.n+1
          for n in ind.G.nodes():
            if np.random.random()<(k*ind.G.degree(n)*1.0/Deg):
              ind.G.add_edge(n,ind.n-1)
              Deg+=1
          ind.G=ind.connected_Graph(ind.G)    
          ind.m=nx.number_of_edges(ind.G)      
      return popCroisee
    
    #///// Mise a jour de la population /////
    def majPopulation(self,popMutee):
      print "Mise a jour pop"
      #popTriee = self.triFitness()
      #popCroisee = self.croisement()
      #popMutee = self.mutation(popCroisee)
      for i in range(self.seuilSelection) :
          self.pop[self.Npop-1-i].Pk = popMutee[i].calcul_Pk()
          self.pop[self.Npop-1-i].Ck = popMutee[i].calcul_Ck()
          self.pop[self.Npop-1-i].Diam = popMutee[i].calcul_Diam()
          self.pop[self.Npop-1-i] = popMutee[i]


#    def comparaison statisques de chaque test au seuil pour le reseau de meilleure fitness
