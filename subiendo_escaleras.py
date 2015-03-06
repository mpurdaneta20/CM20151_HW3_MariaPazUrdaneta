# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import random

# <codecell>

def SubiendoEscaleras(Escalon):
    if Escalon == 0:
        return 0
    elif Escalon == 1:
        return 1
    else:
        return SubiendoEscaleras(Escalon-1) + SubiendoEscaleras(Escalon-2)

# <codecell>

print SubiendoEscaleras(13)

# <codecell>

print SubiendoEscaleras(15)

# <codecell>

#Genera un numero aleatorio en un rango de 1- 10000
L=random.choice(range(1,10000))
print L

#Rellena la matriz A con numeros entre 1-L y la matriz B con numeros entre 1-20
A=[]
for i in range(L):
    s=random.choice(range(1,L))
    A.append(s) 
print A

B=[]
for i in range (L):
    n=random.choice(range(1,20))
    B.append(n)
print B

# <codecell>

#Funcion que genera los modulos de A con respecto a 2B. 
def escaleras(A,B):
    G=[]
    for i in range(L):
         m=2*B[i]
         C=A[i]%m
         G.append(C)
    return G
#Luego convierte la nueva matriz de numero de escalones (modulos), al numero de maneras posibles de subir dicha escalera de n escalones.
    NumeroPasos=[]
    for i in range(L):
         F=SubiendoEscaleras(G[i])
         NumeroPasos.append(F)   
    print "La matriz que determina el numero de posibilidades de subir una escalera con",G, "escalones es",NumeroPasos

# <codecell>

#Resultado final.
s=escaleras(A,B)
print s
# <codecell>


