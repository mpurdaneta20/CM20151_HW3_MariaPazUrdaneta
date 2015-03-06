# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#Punto 3A
import urllib
import os

# <codecell>

#Crea una carpeta donde se meteran los 100 archivos
dirname = 'Test'
os.makedirs(dirname)
os.chdir(dirname)

# <codecell>

#Se descargan los archivos 
for a in range(50,5801,50):
    print a
    if a==50:
        urllib.urlretrieve("https://github.com/forero/ComputationalMethods/raw/master/homework/2015-01/hw3/Test/test00050.txt","test00050.txt")
        urllib.urlretrieve("https://github.com/forero/ComputationalMethods/raw/master/homework/2015-01/hw3/Test/test00003.txt","test00003.txt")
    elif a>50:
        urllib.urlretrieve("https://github.com/forero/ComputationalMethods/raw/master/homework/2015-01/hw3/Test/test00"+str(a)+".txt","test00"+str(a)+".txt")  

# <codecell>

#Se realiza una animacion de las primeras dos columnas de cada archivo. Por comodidad se expersa a que archivo pertenece cada pareja de columnas.
File=open('test00003.txt','r')
a=3
print "El nombre del archivo termina en",a
for column in File:
    print column[0:24]
    
for a in range(50,5801,50):
    print "El nombre del archivo termina en",a
    if a==50:
        File=open('test00050.txt','r')
        for column in File:
            print column[0:24]
    elif a>50:
        File=open('test00'+str(a)+'.txt','r')
        for column in File:
            print column[0:24]
            
        

# <codecell>


