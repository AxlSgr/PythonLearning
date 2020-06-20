# Exercice 8
from random import random

def de_pair(lances):
    nombre=0
    for compteur in range(lances):
        if random()<=0.5:
            nombre+=1
    return(nombre)

nbLanceDe=10000
nbExperience=100

numbers=[]
for i in range(nbExperience):
    numbers.append(de_pair(nbLanceDe))
print ("On a obtenu %s." % (numbers))
print ("On a donc un intervalle de [%s,%s] nombres pairs sur %s lancés." % (min(numbers),max(numbers),nbLanceDe))
print ("Cela donne une fréquence qui appartient à l'intervalle [%s,%s]." % (min(numbers)/nbLanceDe,max(numbers)/nbLanceDe))