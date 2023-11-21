## Exo1Fonction de la recherche  ##

def recherche(tab,n) :
    """ précondition :  renvoie la dernière occurrence de la chose quelle l'on cherche
    postcondition : tab et n sont des entiers"""
    index = len(tab)
    for i in range(len(tab)):
        if tab[i] == n:
            index = i


assert recherche([5, 3],1) == 2
assert recherche([2,4],2) == 0
assert recherche([2,3,5,2,4],2) == 3

### Ex2

# a) importation de notes.csv

import csv

with open("notes.csv",'r',encoding='utf-8') :
    tab = list(csv.DictReader(delimiter = ';'))


# b fonction moyenne eleve

def moyenne_eleve(tab,eleve):
    for dico in tab:
        if dico['prenom'].lower() == eleve.lower():
            return ((float(dico['note1']) * float(dico['coef1']) + float(dico['note2']) * float(dico['coef2'])) / 5)
        else:
            return - 1


assert moyenne_eleve(tab,"Jenamnuail") == 15.4
assert moyenne_eleve(tab,"Ré-douanes") == 9.8


# c) fonction moyenne_classe

def moyenne_classe(tab, classe):
    moyennes = []

    for dico in tab:
        if dico['classe'] == classe:
            moyennes.append(moyenne_eleve(tab, dico['prenom']))

    if len(moyennes) > 1:
        somme = 0
        for m in moyennes:
            somme += m
        return somme / len(moyennes)
    else :
        return -1


assert moyenne_classe(tab,"1GA") == 12.066666666666668
assert moyenne_classe(tab,"1GD") == -1
