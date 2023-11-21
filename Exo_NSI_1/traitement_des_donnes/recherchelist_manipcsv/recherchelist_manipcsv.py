
# Nom : ...  Prénom : ...  Classe : ...  date : ...


### Ex 1. Fonction recherche  ###

def recherche(tab,n) :
    """ précondition : tab est un tableau non vide d'entiers
    n est un entier
    postcondition :la ofnction renvoie l'indice de la dernière occurence
    renvoie la longueur du tableau"""

    indice = len(tab)

    for i in range(len(tab)):
        if tab[i] == n:
            indice = i
    return indice


assert recherche([5, 3],1) == 2
assert recherche([2,4],2) == 0
assert recherche([2,3,5,2,4],2) == 3


### Ex. 2.

# a) importation du fichier notes.csv

import csv

with open("notes.csv",'r',encoding="utf-8") as f:
    tab = list(csv.DictReader(f,delimiter=';'))
    



# b) fonction moyenne_eleve

def moyenne_eleve(tab,eleve):
    m = -1
    for dico in tab :
        if dico ["prenom"] == eleve:
            m = (int(dico["coef1"])*int(dico["note1"])+\
                 int((dico["coef2"])*int(dico["note2"]))/5
    return m

#c)

def moyenne_classe(tab,classe):
                 m = -1
                 nb = 0
                 for dico in tab :
                        if dico ["classe"] == classe :
                                    m += moyenne_eleve(tab,dico["prenom"])
                 
                 
                        
                
                 
                 
    



assert moyenne_eleve(tab,"Lucas") == 12.6
assert moyenne_eleve(tab,"Jimmy") == 10.2
assert moyenne_eleve(tab,"Henry") == -1


# c) fonction moyenne_classe

def moyenne_classe(tab,classe):

    ...


assert moyenne_classe(tab,"1GA") == 12.066666666666668
assert moyenne_classe(tab,"1GD") == -1



        
            
        









        
            
