# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import urllib
import os
import sys
import string
import unicodedata
from os import system

# <codecell>

urllib.urlretrieve("https://github.com/forero/ComputationalMethods/raw/master/homework/2015-01/hw3/Sainte-Beuve.txt","Sainte-Beuve.txt")

# <codecell>

s=sys.argv[1]
File = open('Sainte-Beuve.txt','r')
os.system("head -"+str(s)+" Sainte-Beuve.txt > Vocales.txt")
#os.system("head -6 Sainte-Beuve.txt > Vocales.txt")

# <codecell>

S=open('Vocales.txt','r')
for line in S:
    cont=0
    S=unicode(line,'utf8')
    S= unicodedata.normalize('NFKD', S).encode('ASCII', 'ignore')
    S=S.lower()
    vocales="aeiou"
    for letter in line:
        if letter in vocales:
            cont=cont+1
    print cont
    print S
    

# <codecell>


