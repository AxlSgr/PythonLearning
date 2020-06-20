from random import random

def Zone_Bleue(lances):
    nombre=0
    for i in range(lances):
        x=random()
        y=random()
        if y<x**2:
            nombre+=1
    return(nombre)

nbLances=100000

nombre=0
nombre=Zone_Bleue(nbLances)
print ("Il y a eu %s lancés qui ont touché la zone bleue sur %s" % (nombre,nbLances))
print ("L'aire de la zone bleue est donc environ %s" % (round(float(nombre)/float(nbLances),2)))
