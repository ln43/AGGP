#///////////////////////////////////////////////////////////////////////
#///////////////////// ALGORITHME GENETIQUE ////////////////////////////
#///////////////////////////////////////////////////////////////////////


#///// IMPORTS /////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////
from Graphes import Graphes
from population import population
import networkx as nx
import matplotlib.pyplot as plt
#-----------------------------------------------------------------------




#///// LA CLASSE ET SES METHODES ///////////////////////////////////////
#///////////////////////////////////////////////////////////////////////

class algorithmeGenetique :
    


    def __init__(self,gamma_,n,m,Npop,seuilSelection_,nombreIterations_,ponderation_,pmut_,pcrois_,kmut_) :        
        self.gamma = gamma_ 
        self.pcrois=pcrois_
        self.pmut=pmut_
        self.nombreIterations = nombreIterations_
        self.pop = self.generePopInit(n,m,Npop,seuilSelection_)
        self.ponderation=ponderation_
        self.kmut=kmut_
    
#    ///// Recuperation des parametres /////
#    def enterParameters(self, field):
                

#    ///// Generer la population d'etude /////
    def generePopInit(self,n,m,Npop,seuilSelection):
      Pop=[]
      for i in range(Npop):
        Pop.append(Graphes(n,m))
      return population(Pop,self.gamma,seuilSelection,self.pcrois, self.pmut)

#    ///// Execution de l'algorithme /////
    def loop(self):
      P_crois=self.pop.croisement(1)
      P_mut=self.pop.mutation(P_crois,1,k)
      self.pop.majPopulation(P_mut)

#-----------------------------------------------------------------------
      


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

#-----------------------------------------------------------------------

#///// APPEL ///////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////

p=[1,2,3]
A=algorithmeGenetique(2.2,10,20,10,4,100,p,1,1,2)
print A.pop.calculFitness(p)
X=A.pop.triFitness(p)


Y=[]
for i in range(len(X)):
  Y.append(X[i].calcul_cout(2.5, p))
print Y
X=A.pop.selectionPiresFitness(p)
Y=[]
for i in range(len(X)):
  Y.append(X[i].calcul_cout(2.5, p))
print Y
  
#-----------------------------------------------------------------------
