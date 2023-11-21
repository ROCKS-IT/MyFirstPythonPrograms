########## tp recherche dans une table ############
#1)

import csv
from math import *

with open("fr-esr-cartographie_formations_parcoursup.csv",'r',encoding='utf-8') as f:
    tab = list(csv.DictReader(f,delimiter = ';'))

tab = [dict(dico) for dico in tab]


#2)

def champs(table):
    return list(table[0].keys())

#3)

def etab_ville(mot_cle,ville):
    for dico in tab:
        if ville.lower() == dico['commune'].lower() and \
           (mots_cle.lower() in dico['nm'].lower() or \
            mots_cle.lower() in dico['rec'].lower() ):
            print(dico['nm'],dico['fl'],'\n')
            
#6) gps

def coord_gps(chaine):
    coord = chaine.split(',')
    lat = float(coord[0])
    long = float(coord[1])
    return [lat,long]







