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
    
    def __init__(self,gamma_,n,m,Npop,seuilSelection_,nombreIterations_,ponderation_,pmut_,pcrois_,kmut_) :
        self.gamma = gamma_ 
        self.nombreIterations = nombreIterations_
        self.pop = self.generePopInit(n,m,Npop,seuilSelection_)
        self.ponderation=ponderation_
        self.pmut=pmut_
        self.pcrois=pcrois_
        self.kmut=kmut_
        
#    ///// Recuperation des parametres /////
#    def enterParameters(self, field):
                
    def generePopInit(self,n,m,Npop,seuilSelection):
      Pop=[]
      for i in range(Npop):
        Pop.append(Graphes(n,m))
      return population(Pop,self.gamma,seuilSelection)

    def loop(self):
      P_crois=self.pop.croisement(1)
      P_mut=self.pop.mutation(P_crois,1,k)
      self.pop.majPopulation(P_mut)
      


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
A=algorithmeGenetique(2.2,10,20,10,2,100,[1,1,1],1,1,2)


# Essais methodes 
print "Fitness init : ",A.pop.calculFitness()

X=A.pop.triFitness()
Y=[]
for i in range(len(X)):
  Y.append(X[i].calcul_cout(2.5))
print "Fitness triees : ", Y

X=A.pop.selectionPiresFitness()
Y=[]
for i in range(len(X)):
  Y.append(X[i].calcul_cout(2.5))
print "Pires fitness : ",Y

X=A.pop.croisement(1)

plt.subplot(221)
nx.draw(X[0].G)
plt.subplot(222)
nx.draw(X[1].G)

X2=A.pop.mutation(X,1,2)

plt.subplot(223)
nx.draw(X2[0].G)
plt.subplot(224)
nx.draw(X2[1].G)

plt.show()

  
