#Essais Helene
# Methode 1 : "chi-2"

#Graphe deja scale free

#Gr=Graphes(15,5,2)
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
#X=[(PK[i]-PKtheo[i])**2/PKtheo[i] for i in range(1,len(PK))]
#Xsum=sum(X)
#print Xsum
#
##Graphe aleat avec autant de noeuds
#Gr2=Graphes(15,nx.number_of_edges(Gr.G),1)
#nx.draw(Gr2.G)
#plt.show()
#print Gr2.Pk
#
#PK=np.array(Gr2.Pk)
#PKtheo=[0]*len(PK)
#gamma=2.5
#for i in range(1,len(PK)):
#  PKtheo[i]=i**(-gamma)
#  
#X=[(PK[i]-PKtheo[i])**2/PKtheo[i] for i in range(1,len(PK))]
#Xsum=sum(X)
#print Xsum

########## Resultat : 
## Statistique plus elevee dans le cas du graphe aleat mais stat tres grande dans le cas 1 quand meme
#Idee : creer une table des statistiques faites avec barabasi pour comparer?


# Methode 2 : Coeff de correlation le plus proche de 1 (en prenant le log)

#Graphe deja scale free
Gr=Graphes(15,5,2)
nx.draw(Gr.G)
plt.show()

# Pas de prise en compte des degre non representes
PK=np.array(Gr.Pk)
k=[]
for i in range(len(PK)):
  if PK[i]>0:
    k.append(i)
PK=np.log(PK[PK!=0])
k=np.log(k)
gamma=2.5
x=np.array([k,PK])
r=abs(np.corrcoef(x)[0,1])
print " R ideal 2 = " , r

#Prise en compte des degre avec 0 noeuds
#PK=np.array(Gr.Pk[1:len(Gr.Pk)])
#k=[]
#for i in range(len(PK)):
#  if PK[i]>0:
#    PK[i]=np.log(PK[i])
#  else:
#    PK[i]=10^6
#k=np.log(range(1,len(PK)+1))
#gamma=2.5
#x=np.array([k,PK])
#r=abs(np.corrcoef(x)[0,1])
#print " R ideal = " ,r
#plt.plot(k,PK)
#plt.show()


#Graphe aleat avec autant de noeuds
Gr2=Graphes(15,nx.number_of_edges(Gr.G),1)
nx.draw(Gr2.G)
plt.show()
print Gr2.Pk

PK=Gr2.Pk
k=[]
for i in range(len(PK)):
  if PK[i]>0:
    k.append(i)
PK=np.log(PK[PK!=0])
k=np.log(k)
gamma=2.5
x=np.array([k,PK])
r=abs(np.corrcoef(x)[0,1])
print " R aleat = " , r
plt.plot(k,PK)
plt.show()

########## Resultat : 
## Meme resultat , meilleur dans le cas de celui generer par barbasi mais pas top quand meme

# Methode 3 : Minimiser "SCE"
#Graphe deja scale free

#Gr=Graphes(15,2,2)
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
##Graphe aleat avec autant de noeuds
#Gr2=Graphes(15,nx.number_of_edges(Gr.G),1)
#nx.draw(Gr2.G)
#plt.show()
#print Gr2.Pk
#
#PK=np.array(Gr2.Pk)
#PKtheo=[0]*len(PK)
#gamma=2.5
#for i in range(1,len(PK)):
#  PKtheo[i]=i**(-gamma)
#  
#X=[(PK[i]-PKtheo[i])**2 for i in range(1,len(PK))]
#Xsum=sum(X)
#print Xsum
#
##pour essais
#Gtry=nx.gnm_random_graph(10,15)
