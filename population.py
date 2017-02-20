# -*- coding: utf-8 -*-
#///////////////////////////////////////////////////////////////////////
#////////////////////////// POPULATION /////////////////////////////////
#///////////////////////////////////////////////////////////////////////

#///// IMPORTS /////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////
from Graphes import Graphes

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
        fitnessPop = self.calculFitness(self.pop)
        index = np.argsort(fitnessPop) #Indices des genomes dans ordre croissant

        popTriee = []     #Tableau des genomes de la population triee, TxN
        for j in xrange(len(self.pop)) :
            popTriee.append(self.pop[index[j]])
        return popTriee     #Classes dans ordre croissant de fitness

    def selectionPiresFitness(self):
        popTriee = self.triFitness(self.pop)
        popSelectionnee = []      #Tableau des genomes de la population selectionnee TxNs
        for i in xrange(self.seuilSelection) :
            selection.append(populationTriee[i])     #Selectionne les fitness les moins elevees
        return popSelectionnee     #Classes dans ordre croissant de fitness
            
    def mutation(self):
        popSelectionnee = self.selectionPiresFitnes(self.pop)
        #for ind in xrange(len(popSelectionnee)):              #Pour chaque individu selectionne
            #for graphe in xrange(len(popSelectionnee[ind])):    #Pour chaque gene de son genome
                #if Tm > np.random.random() :                         #Tirage de la probabilite de muter
                #    popSelectionnee[ind][gene] *= (-1)        #Mutation, 1 devient -1 et inversement
        return popSelectionnee  
    
    def croisement(popMutee):
        return popMutee
        #Scinder en deux sous-graphes et faire echanger ces sous-graphes.
    
    def majPopulation(pop):
        popTriee = self.triFitness(self.pop)
        popCroisee = self.croisement(self.pop) #Moitie de la pop
        pop[self.seuil,len(pop)] = popTriee[0,self.seuil-1]
        pop[0,self.seuil-1] = popCroisee

#    def comparaison statisques de chaque test au seuil pour le reseau de meilleure fitness