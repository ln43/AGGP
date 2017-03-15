#///////////////////////////////////////////////////////////////////////
#///////////////////// ALGORITHME GENETIQUE ////////////////////////////
#///////////////////////////////////////////////////////////////////////


#///// IMPORTS /////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////
from Graphes import Graphes
from population import population
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
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
        self.fichierOutput = "outputGamma" + str(self.gamma) + ".txt"


#    ///// Generer la population d'etude /////
    def generePopInit(self,n,m,Npop,seuilSelection):
      Pop=[]
      for i in range(Npop):
        Pop.append(Graphes(n,m))
      return population(Pop,self.gamma,seuilSelection,self.pcrois, self.pmut)

#    ///// Execution de l'algorithme /////
    def loop(self):
      for i in xrange(nombreIterations_):
        print "Iteration ",i
        ## Tri de la population par fitness ##
        self.pop.pop=self.pop.triFitness(self.ponderation)
        ## Selection et croisement des pires graphes de la population ##
        X=self.pop.croisement(self.ponderation)
        ## Mutation de la population selectionnee ##
        X2=self.pop.mutation(X,self.kmut)
        ## Mise a jour de la population ##
        self.pop.majPopulation(X2)

  # Selectionne le graphe optimal et l'affiche
    def select_optimal(self):
      print " \n AFFICHAGE DE LA SOLUTION OPTIMALE \n "
      self.pop.pop=self.pop.triFitness(self.ponderation)
      Gopt=self.pop.pop[0]
      
      plt.figure()
      
      plt.subplot(211)
      Pktheo=[i**(-self.gamma) for i in range(1,len(Gopt.Pk))]
      plt.scatter(range(len(Gopt.Pk)),Gopt.Pk)
      plt.plot(range(1,len(Gopt.Pk)),Pktheo,'r-')
      plt.title("Distribution des P(k)")
      plt.xlabel("degre")
      plt.ylabel("P(k)")
      
      plt.subplot(212)
      Cktheo=[i**(-1) for i in range(1,len(Gopt.Ck))]
      plt.scatter(range(len(Gopt.Ck)),Gopt.Ck)
      plt.plot(range(1,len(Gopt.Ck)),Cktheo,'r-')
      plt.title("Distribution des C(k)")
      plt.xlabel("degre")
      plt.ylabel("C(k)")
      
      plt.show()
      
      print "Diametre du graphe optimal : ", Gopt.Diam
      print "Diametre loi du petit monde : ", np.log(Gopt.n)
      print "Statistique final : ", Gopt.calcul_cout(self.gamma,self.ponderation,)
      
      nx.draw(Gopt.G)
      plt.title("Graphe optimal")
      plt.show()


#-----------------------------------------------------------------------
      


#///// FICHIERS LUS ET ECRITS //////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////

field = "parametresEntres.txt"

#///// Ouverture du fichier /////
fichierparam = open(field,'rb')
enter = fichierparam.readlines()
param = [0]*(len(enter)-5)

for i in xrange(5,len(enter)):
    param[i-5] = enter[i].split("\t")[0]     #Nombre d'iterations

#///// Affectation des parametres /////
gamma_ = float(param[0])
n_ = int(param[1])
m_ = float(param[2])
Npop_ = int(param[3])
seuilSelection_ = int(param[4])
nombreIterations_ = int(param[5])     #Nombre d'iterations
ponderation_ = [int(param[6][1]),int(param[6][3]),int(param[6][5])]
pmut_ = float(param[7])
pcrois_ = float(param[8])
kmut_ = float(param[9])
#-----------------------------------------------------------------------


#///// APPEL ///////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////

#///// Creation de l'algorithme genetique /////
A=algorithmeGenetique(gamma_,n_,m_,Npop_,seuilSelection_,nombreIterations_,ponderation_,pmut_,pcrois_,kmut_)
print "Fitness init : ",A.pop.calculFitness(ponderation_)

#///// Iterations de l'algorithme /////
A.loop()
#-----------------------------------------------------------------------

#///// Affichage, solution finale /////
A.select_optimal()
