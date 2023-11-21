
from random import randint, shuffle
from time import *
import matplotlib.pyplot as plt

# ================================================================
# création des données d'entrée :
# tableaux d'entiers (ordre aléatoire, croissant et décroissants)
# de tailles 1000, 2000, 4000, 8000 et 16000

taille = 1000
donnees_alea = []
donnees_up = []
donnees_down = []
axis = []

for i in range(5):
    tab_alea = []
    tab_up = []
    tab_down = []
    for j in range(taille*2**i):
        tab_alea.append(j)
        tab_up.append(j) 
        tab_down.append(taille*2**i-j-1)
    shuffle(tab_alea) 
    donnees_alea.append(tab_alea)
    donnees_up.append(tab_up)
    donnees_down.append(tab_down)
    axis.append(taille*2**i)

# ================================================================

def executer_fonction(fonction,color,nom):
    """ mesure les temps d'exécution de la fonction passée en paramètre pour 
    des tableaux de tailles 1000, 2000, 4000, 8000 et 16000, et affiche les 
    résultats dans la console et sous forme de graphiques (avec matplotlib)"""
    temps_alea = []
    temps_up = []
    temps_down = []
    for i in range(5):
        debut = perf_counter()
        fonction(donnees_alea[i])
        fin = perf_counter()
        duree = fin-debut
        temps_alea.append(duree)
        
        debut = perf_counter()
        fonction(donnees_up[i])
        fin = perf_counter()
        duree = fin-debut
        temps_up.append(duree)

        debut = perf_counter()
        fonction(donnees_down[i])
        fin = perf_counter()
        duree = fin-debut
        temps_down.append(duree)
        
    plt.plot(axis,temps_alea,'-'+color,label=nom+' (aléatoire)')
    plt.plot(axis,temps_up,'--'+color,label=nom+' (croissant)')
    plt.plot(axis,temps_down,':'+color,label=nom+' (décroissant)')

    print("{:^8} | {:^39}".format("","temps d'exécution"))
    print("{:^8} | {:^11} | {:^11} | {:^11}".format("taille","aléatoire","croissant","décroissant"))
    print("{:^8} | {:^11} | {:^11} | {:^11}".format("","","",""))
    for i in range(5):
        print("{:8d} | {:011.8f} | {:011.8f} | {:011.8f}".format(taille*2**i,temps_alea[i],\
                                                                 temps_up[i],temps_down[i]))

# =================================================================
# ================== Fonctions à tester ===========================

# Recherche du minimum
#def element_min(tab) :
    ## A FAIRE ##

#executer_fonction(element_min,'r','Recherche du min')

# ===============================================================

# Recherche du maximum
#def element_max(tab) :
    ## A FAIRE ##

#executer_fonction(element_max,'r','Recherche du min')        

# ================================================================

# tri_selection

def tri_selection (tab) :
    for i in range(0,len(tab)-1) :    # de 0 à n-2
        indmin = i
        for j in range(i+1,len(tab)) : # de i+1 à n-1, recherche du min
            if tab[j] < tab[indmin] : indmin = j
        tab[indmin],tab[i]=tab[i],tab[indmin]  # echange de valeurs entre indmin et i

executer_fonction(tri_selection,'g','Tri par sélection')

# ==================================================================

# Tri par insertion
#def tri_insertion(tab) :
    ##  A FAIRE  ##

#executer_fonction(tri_insertion,'b','Tri par insertion')

# ===================================

# Tri bulle
#def tri_bulle (tab):
    ## A FAIRE ##

#executer_fonction(tri_bulle,'r','Tri bulle')

# ========================================================================================

# Tri fusion (fonction récursive ... programme terminale)
def fusion(gauche, droite):
    igauche, idroite = 0,0
    result = []
    while igauche < len(gauche) and idroite < len(droite):
        if gauche[igauche] < droite[idroite]:
            result.append(gauche[igauche])
            igauche += 1
        else:
            result.append(droite[idroite])
            idroite += 1
    result += gauche[igauche:]
    result += droite[idroite:]
    return result

def triFusion (tab):
    if len(tab) <= 1 :
        return tab
    milieu = len(tab) // 2
    gauche = triFusion(tab[:milieu])
    droite = triFusion(tab[milieu:])
    return fusion(gauche,droite)

executer_fonction(triFusion,'k','Tri fusion')


# ========================================================================================

plt.grid(True)
plt.legend(loc='upper left')
plt.show()








    
