#///////////////////////////////////////////////////////////////////////
#///////////////////// ALGORITHME GENETIQUE ////////////////////////////
#///////////////////////////////////////////////////////////////////////


#///// IMPORTS /////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////
from Graphes import Graphes
from population import population
import networkx as nx
import matplotlib.pyplot as plt




#///// LA CLASSE ET SES METHODES ///////////////////////////////////////
#///////////////////////////////////////////////////////////////////////

class algorithmeGenetique :
    
    def __init__(self,gamma_,n,m,Npop,seuilSelection_,nombreIterations_) :
        
        self.gamma = gamma_ 
        self.nombreIterations = nombreIterations_
        self.pop = self.generePopInit(n,m,Npop,seuilSelection_) 
        
#    ///// Recuperation des parametres /////
#    def enterParameters(self, field):
                
    def generePopInit(self,n,m,Npop,seuilSelection):
      Pop=[]
      for i in range(Npop):
        Pop.append(Graphes(n,m))
      return population(Pop,self.gamma,seuilSelection)

    def loop(self):
      P_mut=self.pop.mutation()
      P_crois=self.pop.croisement(P_mut)
      self.pop.majPopulation(P_crois)
      


#///// FICHIERS LUS ET ECRITS //////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////

#fichierparam = 'parametresEntres.txt'
#fichierOutput = 'outputGamma + str(self.gamma) + '.txt'
#
### Ouverture du fichier ##
#fichierparam = open(field,'rb')
#enter = fichierparam.readlines()
#param = [0]*(len(enter)-5)
#
#for i in xrange(5,len(enter)):
#    param[i-5] = int(enter[i].split("\t")[0])     #Nombre d'iterations
#
### Affectation des parametres ##
#nombreIterations_ = param[0]     #Nombre d'iterations
#gamma_ = param[1]
#nombreGraphesPopInit_ = param[2]
#seuilSelection_ = param[3]        


#///// APPEL ///////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////
A=algorithmeGenetique(2.5,10,15,5,2,100)
print A.pop.calculFitness()