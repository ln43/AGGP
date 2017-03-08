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
        self.fichierOutput = "outputGamma" + str(self.gamma) + ".txt"

    
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
      
      for i in xrange(nombreIterations_):
        self.pop.pop=self.pop.triFitness(self.ponderation)
        ## Tri des fitness ##
        #~ X=self.pop.triFitness(ponderation_)
        #~ Y=[]
        #~ for i in range(len(X)):
            #~ Y.append(X[i].calcul_cout(2.5, ponderation_))
        #~ print "Fitness triees : ",Y
    
        ## Selection des pires fitness ##
        #~ X=self.pop.selectionPiresFitness(ponderation_)
        #~ Y=[]
        #~ for i in range(len(X)):
            #~ Y.append(X[i].calcul_cout(2.5, ponderation_))
        #~ print "Pires fitness : ",Y
    
        ## Croisement ##
        X=self.pop.croisement(self.ponderation)
        
        ## Affichage - Deux figures avant mutation ##
        #~ plt.subplot(221)
        #~ nx.draw(X[0].G)
        #~ plt.subplot(222)
        #~ nx.draw(X[1].G)
        
        ## Mutation ##
        X2=self.pop.mutation(X,2)
        
        ## Affichage - Deux figures apres mutation ##
        #~ plt.subplot(223)
        #~ nx.draw(X2[0].G)
        #~ plt.subplot(224)
        #~ nx.draw(X2[1].G)
    #~ 
        #~ plt.show()  
        
        ## Mise a jour de la population ##
        self.pop.majPopulation(X2)



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
