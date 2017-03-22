# -*- coding: utf-8 -*-
#///////////////////////////////////////////////////////////////////////
#////////////////////////// POPULATION /////////////////////////////////
#///////////////////////////////////////////////////////////////////////

#///// IMPORTS /////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////
from Graphes import Graphes
import numpy as np
import networkx as nx
import random
import matplotlib.pyplot as plt

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
          
    def new_subgraph(self,g,nodes):
      subG1=nx.Graph()
      subG1.add_nodes_from(nodes)
      Edges=[]
      for e in g.G.edges():
        if e[0] in nodes and e[1] in nodes:
          Edges.append(e)
      subG1.add_edges_from(Edges)
      return subG1
          
    def croisement(self,ponderation):
        print "Croisement"
        popSelectionnee = self.selectionPiresFitness(ponderation)
        gcrois=[]
        while len(popSelectionnee)>1:
          proba=np.random.random()
          g=popSelectionnee.pop(0)
          if proba<self.pCrois:
            g2=random.choice(popSelectionnee)
            popSelectionnee.remove(g2)
            M=g.m+g2.m
            #Scinder les noeuds de g en deux groupes
            noeuds1=np.random.choice(g.G.nodes(),int(g.n/2),replace=False)
            noeudsopp1=filter(lambda x: x not in noeuds1, g.G.nodes())
            subG1=g.G.subgraph(noeuds1)
            subGopp1=g.G.subgraph(noeudsopp1)
            if len(subG1.nodes())==0:
              subG1=self.new_subgraph(g,noeuds1)
            if len(subGopp1.nodes())==0:
              subGopp1=self.new_subgraph(g,noeudsopp1)
            m1=g.m-nx.number_of_edges(subG1)-nx.number_of_edges(subGopp1)           
            
            #Renommer noeud de g2
            mapping={}
            for i in range(g2.G.number_of_nodes()):
              mapping[i]=i+2*g.G.number_of_nodes()
            g2.G=nx.relabel_nodes(g2.G,mapping)
            
            #Scinder les noeuds de g2 en deux groupes
            noeuds2=np.random.choice(g2.G.nodes(),int(g2.n/2),replace=False)
            noeudsopp2=filter(lambda x: x not in noeuds2, g2.G.nodes())
            subG2=g2.G.subgraph(noeuds2)
            subGopp2=g2.G.subgraph(noeudsopp2)
            if len(subG2.nodes())==0:
              subG2=self.new_subgraph(g2,noeuds2)
            if len(subGopp2.nodes())==0:
              subGopp1=self.new_subgraph(g2,noeudsopp2)
            m2=g2.m-nx.number_of_edges(subG2)-nx.number_of_edges(subGopp2)               
            
            #Creation de deux nouveaux graphes
            newg1=nx.compose(subG1,subGopp2)
            newg2=nx.compose(subG2,subGopp1)

            #Ajout des aretes manquantes a newg1
            i=0
            while i<=min(m1,len(noeuds1)*len(noeudsopp2)):
              e=(np.random.choice(noeuds1,1),np.random.choice(noeudsopp2,1))
              if e not in newg1.edges():
                newg1.add_edge(int(e[0]),int(e[1]))
                i=i+1
            g.G=nx.convert_node_labels_to_integers(newg1) #renommer les noeuds
            g.G=g.connected_Graph(g.G) # verifier qu'il est connecte
            g.n,g.m=nx.number_of_nodes(g.G),nx.number_of_edges(g.G) # mise a jour du nombre de noeud et arete
            #Ajout des aretes manquantes a newg2     
            i=0
            while i<=min(m2,len(noeuds2)*len(noeudsopp1)):
              e=(np.random.choice(noeuds2,1),np.random.choice(noeudsopp1,1))
              if e not in newg2.edges():
                newg2.add_edge(int(e[0]),int(e[1]))
                i=i+1
            g2.G=nx.convert_node_labels_to_integers(newg2) #renommer les noeuds
            g2.G=g2.connected_Graph(g2.G) # verifier qu'il est connecte
            g2.n,g2.m=nx.number_of_nodes(g2.G),nx.number_of_edges(g2.G) # mise a jour du nombre de noeud et arete
            gcrois.append(g2)
          gcrois.append(g)
          
            
        if len(popSelectionnee)==1:
          gcrois.append(popSelectionnee.pop(0))
        return gcrois
        
    def mutation(self,popCroisee,k):
      print "Mutation"
      for ind in popCroisee:            #Pour chaque individu selectionne
        proba=np.random.random()//self.pMut
        if proba==0: #Proba de rajouter un noeud
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
        elif proba==3: # Proba de supprimer un noeud
          ind.G.remove_node(int(np.random.choice(ind.G.nodes(),1)))
          ind.G=ind.connected_Graph(ind.G)
          ind.n=ind.n-1
          ind.m=nx.number_of_edges(ind.G)
        elif proba==2: # Proba de supprimer une arete
          e=random.choice(ind.G.edges())
          ind.G.remove_edge(e[0],e[1])
          ind.G=ind.connected_Graph(ind.G)
          ind.m=nx.number_of_edges(ind.G)
        elif proba==1: # Proba de rajouter une arete
          if ind.m<ind.n*(ind.n-1)/2:
            e=tuple(np.random.choice(ind.G.nodes(),2))
            while e in ind.G.edges():
              e=tuple(np.random.choice(ind.G.nodes(),2))
            ind.G.add_edge(e[0],e[1])
            ind.m=ind.m+1
      return popCroisee
    
    #///// Mise a jour de la population /////
    def majPopulation(self,popMutee,f,ponderation):
      print "Mise a jour population"
      
      
			## Mise a jour de la population modifiee ##
      for i in range(1,self.seuilSelection) :
        
        self.pop[self.Npop-1-i].Pk = popMutee[i].calcul_Pk()
        self.pop[self.Npop-1-i].Ck = popMutee[i].calcul_Ck()
        self.pop[self.Npop-1-i].Diam = popMutee[i].calcul_Diam()
        self.pop[self.Npop-1-i] = popMutee[i]
      
      
      min_Pk = self.pop[0].stat_Pk(self.gamma)
      min_Ck = self.pop[0].stat_Ck()
      min_Dmin = self.pop[0].stat_Diam()
      min_Cout = self.pop[0].calcul_cout(self.gamma, ponderation)
      print min_Cout

			## Recherche des statistiques de la population en fin d'iteration ##
      for i in xrange(1,len(self.pop)):
				  
        statPk = self.pop[i].stat_Pk(self.gamma)
        statCk = self.pop[i].stat_Ck()
        statDmin = self.pop[i].stat_Diam()
        cout = self.pop[i].calcul_cout(self.gamma,ponderation)
        
        if statPk < min_Pk :
          min_Pk = statPk
        if statCk < min_Ck :
          min_Ck = statCk
        if statDmin < min_Dmin :
          min_Dmin = statDmin
        if cout < min_Cout :
					min_Cout = cout
					
      moy_Cout= np.mean(self.calculFitness(ponderation))
      ## Ecriture ## 
      f.writelines(str(min_Pk) + "\t" + str(min_Ck) + "\t"+ str(min_Dmin) + "\t"+ str(min_Cout) +"\t"+str(moy_Cout)+"\n")
      #return [min_Pk, min_Ck, min_Dmin]


#    def comparaison statisques de chaque test au seuil pour le reseau de meilleure fitness
