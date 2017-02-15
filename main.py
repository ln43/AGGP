#//////////////////////// IMPORTS //////////////////////////////////////
#///////////////////////////////////////////////////////////////////////
from Graphes import Graphes
import networkx as nx
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

#//////////////////////// MAIN //////////////////////////////////////
#///////////////////////////////////////////////////////////////////////
print "Lancement du Main"

#Essais Helene

# Methode 3 : Minimiser "SCE"

Gr=Graphes(15,50)
nx.draw(Gr.G)
plt.show()
print Gr.Pk

PK=np.array(Gr.Pk)
PKtheo=[0]*len(PK)
gamma=2.5
for i in range(1,len(PK)):
  PKtheo[i]=i**(-gamma)
  
X=[(PK[i]-PKtheo[i])**2 for i in range(1,len(PK))]
Xsum=sum(X)
print Xsum

#Gtry=nx.gnm_random_graph(10,15)


