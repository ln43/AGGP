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
    
    def __init__(self,gamma_,n,m,Npop,seuilSelection_,nombreIterations_,ponderation_,pmut_,pcrois_,kmut_,output_field_) :
        self.gamma = gamma_ 
        self.pcrois=pcrois_
        self.pmut=pmut_
        self.nombreIterations = nombreIterations_
        self.pop = self.generePopInit(n,m,Npop,seuilSelection_)
        self.ponderation=ponderation_
        self.kmut=kmut_
        self.fichierOutput = output_field_ + "_gamma" + str(self.gamma) + ".txt"


#    ///// Generer la population d'etude /////
    def generePopInit(self,n,m,Npop,seuilSelection):
      Pop=[]
      for i in range(Npop):
        Pop.append(Graphes(n,m))
      return population(Pop,self.gamma,seuilSelection,self.pcrois, self.pmut)

#    ///// Execution de l'algorithme /////
    def loop(self):
      
      control = []
      iterations = []
      f = open(self.fichierOutput,'w')
      f.writelines("min_Pk\t min_Ck\t min_Diam\t min_Cout\n")
      print "\n--- EXECUTION ---"
    
      for i in xrange(nombreIterations_):
        print "\n- Iteration ",i," -"
        ## Tri de la population par fitness ##
        self.pop.pop=self.pop.triFitness(self.ponderation)
        ## Selection et croisement des pires graphes de la population ##
        X=self.pop.croisement(self.ponderation)
        ## Mutation de la population selectionnee ##
        X2=self.pop.mutation(X,2)
        ## Mise a jour de la population ##
        self.pop.majPopulation(X2,f,self.ponderation)

  # Selectionne le graphe optimal et l'affiche
    def select_optimal(self):
      print " \n--- AFFICHAGE DE LA SOLUTION OPTIMALE ---\n "
      self.pop.pop=self.pop.triFitness(self.ponderation)
      Gopt=self.pop.pop[0]
      
      plt.figure()
      
      plt.subplot(211)
      Pktheo=[i**(-self.gamma) for i in range(1,len(Gopt.Pk))]
      plt.scatter(range(len(Gopt.Pk)),Gopt.Pk)
      plt.plot(range(1,len(Gopt.Pk)),Pktheo,'r-')
      plt.title("Distribution des P(k)")
      plt.xlabel("Degre")
      plt.ylabel("P(k)")
      
      plt.subplot(212)
      Cktheo=[i**(-1) for i in range(1,len(Gopt.Ck))]
      plt.scatter(range(len(Gopt.Ck)),Gopt.Ck)
      plt.plot(range(1,len(Gopt.Ck)),Cktheo,'r-')
      plt.title("Distribution des C(k)")
      plt.xlabel("Degre")
      plt.ylabel("C(k)")
      
      
      print "Diametre du graphe optimal : ", Gopt.Diam
      print "Diametre loi du petit monde : ", np.log(Gopt.n)
      print "Statistique final : ", Gopt.calcul_cout(self.gamma,self.ponderation,)
      plt.show()
      
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
output_field_ = str(param[10])
#-----------------------------------------------------------------------


#///// APPEL ///////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////

#///// Creation de l'algorithme genetique /////
A=algorithmeGenetique(gamma_,n_,m_,Npop_,seuilSelection_,nombreIterations_,ponderation_,pmut_,pcrois_,kmut_,output_field_)
print "\n--- POPULATION INITIALE ---\nFitness init : ",A.pop.calculFitness(ponderation_)

#///// Iterations de l'algorithme /////
A.loop()
#-----------------------------------------------------------------------

#///// Affichage, solution finale /////
A.select_optimal()
