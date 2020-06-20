from random import randint

def somme_de(lances,Somme_voulue,nbDe):
    nombre=0
    Somme=0
    for compteur in range(lances):
        for i in range(ndDe):
            nb=randint(0,7)
            Somme+=nb
        if Somme==Somme_voulue:
            nombre=nombre+1
    return(nombre)

nbLanceDe=10000
nbExperience=10
nbDe=4
Somme=12

numbers=[]
for i in range(nbExperience):
    numbers.append(somme_de(nbLanceDe,Somme,nbDe))
print ("On a obtenu %s." % (numbers))
print ("On a donc un intervalle de [%s,%s] nombres pairs sur %s lancés." % (min(numbers),max(numbers),nbLanceDe))
print ("Cela donne une fréquence qui appartient à l'intervalle [%s,%s]." % (min(numbers)/nbLanceDe,max(numbers)/nbLanceDe))
