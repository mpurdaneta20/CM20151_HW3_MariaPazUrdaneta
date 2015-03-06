# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#Punto 3A
import urllib
import os
import csv

# <codecell>

#Crea una carpeta donde se meteran los 100 archivos
dirname = 'Notas'
os.makedirs(dirname)
os.chdir(dirname)

# <codecell>

urllib.urlretrieve("https://github.com/forero/ComputationalMethods/raw/master/homework/2015-01/hw3/Notas.csv","Notas.csv")

# <codecell>

File=open('Notas.csv','r')
output=open('Mas.dat','w')

for line in File:
    l=line.replace(',', '+')
    print l
    output.write(l)
output.close()

# <codecell>

File=open('Notas.csv','r')
output=open('Exclamacion.dat','w')

s=os.system("sed s/\,/+/g Notas.csv >> Exclamacion.dat")
 
output.close()

# <codecell>


