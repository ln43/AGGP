# -*- coding: utf-8 -*-
#///////////////////////////////////////////////////////////////////////
#////////////////////////// POPULATION /////////////////////////////////
#///////////////////////////////////////////////////////////////////////

#///// IMPORTS /////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////
from Graphes import Graphes
import numpy as np
#///// LA CLASSE ET SES METHODES ///////////////////////////////////////
#///////////////////////////////////////////////////////////////////////

class population :   
    def __init__(self, listGraph_, gamma_,seuilSelection_) :
        self.pop = listGraph_ # Number of nodes
        self.Npop=len(self.pop)
        self.gamma=gamma_
        self.seuilSelection = seuilSelection_  #Seuil de selection
     
    def calculFitness(self):
        fitnessPop = []
        for i in xrange(len(self.pop)) :
            fitnessPop.append(self.pop[i].calcul_cout(self.gamma))
        return fitnessPop
    
    def triFitness(self):
        fitnessPop = self.calculFitness()
        index = np.argsort(fitnessPop) #Indices des genomes dans ordre croissant

        popTriee = []     #Tableau des genomes de la population triee, TxN
        for j in xrange(len(self.pop)) :
            popTriee.append(self.pop[index[j]])
        return popTriee     #Classes dans ordre croissant de cout

    def selectionPiresFitness(self):
        popTriee = self.triFitness()
        popSelectionnee = []      #Tableau des genomes de la population selectionnee TxNs
        for i in range(self.seuilSelection) :
            popSelectionnee.append(popTriee[self.Npop-1-i])     #Selectionne les cout les plus eleves
        return popSelectionnee     
            
    def croisement(self,pCrois):
        popSelectionnee = self.selectionPiresFitness(self.pop)
        for g in popSelectionnee:
          proba=np.random.random()
          if proba<pCrois:
            i=np.random.randint(0,len(popSelectionnee))
            while (popSelectionnee[i]==g).all():
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
            nx.draw(g.G)
            plt.show()
            
            i=0
            while i<m2 and nx.number_of_edges(newg2)<(nx.number_of_nodes(newg2)*(nx.number_of_nodes(newg2)-1)/2):
              e=(np.random.choice(noeuds2,1),np.random.choice(noeudsopp1,1))
              if e not in newg2.edges():
                newg2.add_edge(int(e[0]),int(e[1]))
                i=i+1
            g2.G=nx.convert_node_labels_to_integers(newg2)
        return popSelectionnee
        #Scinder en deux sous-graphes et faire echanger ces sous-graphes.
        
    def mutation(self,popCroisee,pMut):
        
        #for ind in xrange(len(popSelectionnee)):              #Pour chaque individu selectionne
            #for graphe in xrange(len(popSelectionnee[ind])):    #Pour chaque gene de son genome
                #if Tm > np.random.random() :                         #Tirage de la probabilite de muter
                #    popSelectionnee[ind][gene] *= (-1)        #Mutation, 1 devient -1 et inversement
        return popCroisee
    
    def majPopulation(pop):
        popTriee = self.triFitness(self.pop)
        popCroisee = self.croisement(self.pop) #Moitie de la pop
        pop[self.seuil,len(pop)] = popTriee[0,self.seuil-1]
        pop[0,self.seuil-1] = popCroisee

#    def comparaison statisques de chaque test au seuil pour le reseau de meilleure fitness