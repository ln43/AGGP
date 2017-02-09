#//////////////////////// IMPORTS //////////////////////////////////////
#///////////////////////////////////////////////////////////////////////
from Graphes import Graphes
import networkx as nx
import matplotlib.pyplot as plt
from scipy import stats

#//////////////////////// MAIN //////////////////////////////////////
#///////////////////////////////////////////////////////////////////////
print "Lancement du Main"
Gr=Graphes(15,5,2)
nx.draw(Gr.G)
plt.show()
print Gr.Pk


#Essais Helene
#Essai -> methode envisagee ne fonctionne pas au moins dans le cas ou on a des noeuds 0

#Graphe deja scale free
PK=Gr.Pk
PKtheo=[0]*len(PK)
gamma=2.5
for i in range(1,len(PK)):
  PKtheo[i]=i**(-gamma)
  
X=[(PK[i]-PKtheo[i])**2/PKtheo[i] for i in range(1,len(PK))]
Xsum=sum(X)
print Xsum

#Graphe aleat avec autant de noeuds
Gr2=Graphes(15,nx.number_of_edges(Gr.G),1)
nx.draw(Gr2.G)
plt.show()
print Gr2.Pk


PK=Gr2.Pk
PKtheo=[0]*len(PK)
gamma=2.5
for i in range(1,len(PK)):
  PKtheo[i]=i**(-gamma)
  
X=[(PK[i]-PKtheo[i])**2/PKtheo[i] for i in range(1,len(PK))]
Xsum=sum(X)
print Xsum

#Resultat : statistique plus elevee dans le cas du graphe aleat mais stat tres grande dans le cas 1 quand meme
#Idee : creer une table des statistiques faites avec barabasi pour comparer?


#pour essais
Gtry=nx.gnm_random_graph(10,15)


