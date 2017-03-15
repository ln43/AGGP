#///// Evolution des statistiques des graphes /////
#//////////////////////////////////////////////////

#///// Donnez les valeurs de gamma etudiees et le nombre d'iterations /////
gamma = c(2.2,2.1)
iterations = 5

#///// Recuperation du fichier /////
min_Pk = matrix(0, nrow = iterations, ncol = length(gamma))
min_Ck = matrix(0, nrow = iterations, ncol = length(gamma))
min_Diam = matrix(0, nrow = iterations, ncol = length(gamma))
min_Cout = matrix(0, nrow = iterations, ncol = length(gamma))
leg = c()
x = seq(1, iterations)


for (i in 1:length(gamma)){
  d = read.table(paste('statistics_gamma',toString(gamma[i]),'.txt', sep = ""), header = T, sep = "\t")
  min_Pk[,i] = d[,1]
  min_Ck[,i] = d[,2]
  min_Diam[,i] = d[,3]
  min_Cout[,i] = d[,4]
  leg[i] = paste('Gamma = ', toString(gamma[i]), sep = "")
}  


#///// Plot /////
par(mfrow = c(2,2))

## Pk ##
plot(x, min_Pk[,1], col= 1, pch=19, las=1, typ = "b", main = 'Evolution du Pk minimal', ylab = 'Pk',xlab = 'Iterations', ylim = c(min(apply(min_Pk,2,min)),max(apply(min_Pk,2,max))))
for (i in 2:length(gamma)){
  print(i)
  lines(x, min_Pk[,i], col= i, pch=19, las=1, typ = "b")
}
legend("topright",leg, cex = .8, col = 1:length(gamma), lwd = 2, lty = 1)

## Ck ##
plot(x, min_Ck[,1], col= 1, pch=19, las=1, typ = "b", main = 'Evolution du Ck minimal', ylab = 'Ck',xlab = 'Iterations', ylim = c(min(apply(min_Ck,2,min)),max(apply(min_Ck,2,max))))
for (i in 2:length(gamma)){
  lines(x, min_Ck[,i], col= i, pch=19, las=1, typ = "b")
}
legend("topright",leg, cex = .8, col = 1:length(gamma), lwd = 2, lty = 1)

## Dmin ##
plot(x, min_Diam[,1], col= 1, pch=19, las=1, typ = "b", main = 'Evolution du Dmin minimal', ylab = 'Dmin',xlab = 'Iterations', ylim = c(min(apply(min_Diam,2,min)),max(apply(min_Diam,2,max))))
for (i in 2:length(gamma)){
  lines(x, min_Diam[,i], col= i, pch=19, las=1, typ = "b")
}
legend("topright",leg, cex = .8, col = 1:length(gamma), lwd = 2, lty = 1)

## Cout ##
plot(x, min_Cout[,1], col= 1, pch=19, las=1, typ = "b", main = 'Evolution du cout minimal', ylab = 'Cout',xlab = 'Iterations', ylim = c(min(apply(min_Cout,2,min)),max(apply(min_Cout,2,max))))
for (i in 2:length(gamma)){
  lines(x, min_Cout[,i], col= i, pch=19, las=1, typ = "b")
}
legend("topright",leg, cex = .8, col = 1:length(gamma), lwd = 2, lty = 1)

