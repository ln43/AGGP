#//////////////////////// IMPORTS //////////////////////////////////////
#///////////////////////////////////////////////////////////////////////
from Graphes import Graphes
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np



#//////////////////////// MAIN //////////////////////////////////////
#///////////////////////////////////////////////////////////////////////
print "Lancement du Main"
#~ Gr=Graphes(5,10)
#~ nx.draw(Gr.G)
#~ plt.show()

#~ Deg=0
#~ for d in Gr.G.degree().values():
  #~ Deg=Deg+d
#~ print Deg

#~ k=2
#~ Gr.G.add_node(nx.number_of_nodes(Gr.G))
#~ Gr.n=Gr.n+1
#~ for n in Gr.G.nodes():
  #~ print k*Gr.G.degree(n)*1.0/Deg
  #~ if np.random.random()<(k*Gr.G.degree(n)*1.0/Deg):
    #~ print True
    #~ Gr.G.add_edge(n,Gr.n-1)
    #~ Deg+=1
#~ Gr.m=nx.number_of_edges(Gr.G)

#~ nx.draw(Gr.G)
#~ plt.show()

#Essais Helene

# Methode 3 : Minimiser "SCE"

#Gr=Graphes(15,50)
#nx.draw(Gr.G)
#plt.show()
#print Gr.Pk
#
#PK=np.array(Gr.Pk)
#PKtheo=[0]*len(PK)
#gamma=2.5
#for i in range(1,len(PK)):
#  PKtheo[i]=i**(-gamma)
#  
#X=[(PK[i]-PKtheo[i])**2 for i in range(1,len(PK))]
#Xsum=sum(X)
#print Xsum
#
#print Gr.stat_Pk(gamma)
#Gtry=nx.gnm_random_graph(10,15)


#Essai Yasmina Petit monde
#~ Gr=Graphes(1000,3000)
#~ L=[1,1,1]
#~ print "Notre pgraphe de barabasi"
#~ print Gr.calcul_cout(2.2, L)



#~ Gr.G=Gr.connected_Graph(nx.gnm_random_graph(1000, 1000))
#~ Gr.n, Gr.m = Gr.G.number_of_nodes(),Gr.G.number_of_edges()
#~ Gr.Ck=Gr.calcul_Ck()
#~ Gr.Pk=Gr.calcul_Pk()
#~ Gr.Diam=Gr.calcul_Diam()
#~ print "Graphe aleatoire"
#~ print Gr.calcul_cout(2.2, L)



#~ Gr.G=Gr.connected_Graph(nx.barabasi_albert_graph(1000, 3))
#~ Gr.n, Gr.m = Gr.G.number_of_nodes(),Gr.G.number_of_edges()
#~ Gr.Ck=Gr.calcul_Ck()
#~ Gr.Pk=Gr.calcul_Pk()
#~ Gr.Diam=Gr.calcul_Diam()
#~ print "Graphe Barab"
#~ print Gr.calcul_cout(2.2, L)

#~ Gr.G=Gr.connected_Graph(nx.powerlaw_cluster_graph(1000,1,0.5))
#~ Gr.n, Gr.m = Gr.G.number_of_nodes(),Gr.G.number_of_edges()
#~ print Gr.n, Gr.m
#~ Gr.Ck=Gr.calcul_Ck()
#~ Gr.Pk=Gr.calcul_Pk()
#~ Gr.Diam=Gr.calcul_Diam()
#~ print "Graphe modele"
#~ print Gr.calcul_cout(2.2, L)



#print '----'
#print Gr.Dmin[1]
#print '----'
#print Gr.Dmin[1][1]
#print '----'
#print len(Gr.Dmin)
#for cle in dico.keys()
	#print cle
#pond=(3,3,1)

#~ G=nx.gnm_random_graph(15, 5)
#~ N=sorted(nx.connected_components(G), key = len, reverse=True)
#~ print type(N)
#~ print N
#~ print len(N) 



