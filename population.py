# -*- coding: utf-8 -*-
#///////////////////////////////////////////////////////////////////////
#////////////////////////// POPULATION /////////////////////////////////
#///////////////////////////////////////////////////////////////////////

#///// IMPORTS /////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////
from Graphes import Graphes
import numpy as np
#-----------------------------------------------------------------------


#///// LA CLASSE ET SES METHODES ///////////////////////////////////////
#///////////////////////////////////////////////////////////////////////

class population :   
    def __init__(self, listGraph_, gamma_,seuilSelection_,pCrois_,pMut_) :
        self.pop = listGraph_ # Number of nodes
        self.Npop=len(self.pop)
        self.gamma=gamma_
        self.seuilSelection = seuilSelection_  #Seuil de selection
        self.pCrois = pCrois_
        self.pMut = pMut_
    
    #///// Calcul de fitness de chaque graphe d'une population ///// 
    def calculFitness(self):
        ##### Rajouter mis a jour Pk,Ck,chemin de chaque graphe a chaque pas de temps
        fitnessPop = []
        for i in xrange(len(self.pop)) :
            fitnessPop.append(self.pop[i].calcul_cout(self.gamma))
        return fitnessPop
    
    #///// Tri des fitness de la population ///// 
    def triFitness(self):
        fitnessPop = self.calculFitness()
        index = np.argsort(fitnessPop)             #Indices des genomes dans ordre croissant

        popTriee = []                              #Tableau des genomes de la population triee, TxN
        for j in xrange(len(self.pop)) :
            popTriee.append(self.pop[index[j]])
        return popTriee                           #Classes dans ordre croissant de cout

    #///// Selection des plus mauvaises fitness de la population pour les ameliorer ///// 
    def selectionPiresFitness(self):
        popTriee = self.triFitness()
        popSelectionnee = []                                  #Tableau des genomes de la population selectionnee TxNs
        for i in range(self.seuilSelection) :
            popSelectionnee.append(popTriee[self.Npop-1-i])   #Selectionne les cout les plus eleves
        return popSelectionnee
            
    #///// Croisement de la portion selectionnee de la population ///// 
    def croisement(self,popMutee):
        for g in popMutee:
          proba=np.random.random()
          if proba<self.pCrois:
            i=np.random.randint(0,len(popMutee))
            while (popMutee[i]==g).all():
                i=np.random.randint(0,len(popMutee))
            g2=popMutee[i]
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
            g.n,g.m=nx.number_of_nodes(g.G),nx.number_of_edges(g.G)
            
            i=0
            while i<m2 and nx.number_of_edges(newg2)<(nx.number_of_nodes(newg2)*(nx.number_of_nodes(newg2)-1)/2):
              e=(np.random.choice(noeuds2,1),np.random.choice(noeudsopp1,1))
              if e not in newg2.edges():
                newg2.add_edge(int(e[0]),int(e[1]))
                i=i+1
            g2.G=nx.convert_node_labels_to_integers(newg2)
            g2.n,g2.m=nx.number_of_nodes(g2.G),nx.number_of_edges(g2.G)
        return popMutee
        
<<<<<<< HEAD
    #///// Mutation de la portion selectionnee de la population ///// 
    def mutation(self):
      popSelectionnee = self.selectionPiresFitness(self.pop)
      for ind in popSelectionnee :              #Pour chaque individu selectionne
        if np.random.random()<self.pmut: #Tirage de la probabilite de muter
=======
    def mutation(self,popCroisee,pmut,k):
      for ind in popCroisee:              #Pour chaque individu selectionne
        if np.random.random()<pmut: #Tirage de la probabilite de muter
>>>>>>> origin/master
          ind.G.add_nodes(ind.n)
          Deg=0
          for d in ind.G.degree().values():
            Deg=Deg+d
          print Deg
          ind.G.add_node(ind.n)
          ind.n=ind.n+1
          for n in Gr.G.nodes():
            if np.random.random()<(k*ind.G.degree(n)*1.0/Deg):
              ind.G.add_edge(n,ind.n-1)
              Deg+=1
          ind.m=nx.number_of_edges(Gr.G)        
        return popSelectionnee
    
    #///// Mise a jour de la population /////
    def majPopulation(pop):
        popTriee = self.triFitness()
        popMutee = self.mutation()
        popCroisee = self.croisement(popMutee) #Moitie de la pop
        for i in range(self.seuilSelection) :
            self.pop[self.Npop-1-i].Pk = popCroisee[i].calcul_Pk()
            self.pop[self.Npop-1-i].Ck = popCroisee[i].calcul_Ck()
            self.pop[self.Npop-1-i].Dmin = popCroisee[i].calcul_Dmin()
            self.pop[self.Npop-1-i] = popCroisee[i]


#    def comparaison statisques de chaque test au seuil pour le reseau de meilleure fitness
