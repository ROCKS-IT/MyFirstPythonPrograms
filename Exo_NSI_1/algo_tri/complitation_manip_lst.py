#tpa alogorythmiques

# 1)

from random import randint

def gen_tab(n,a,b):
    """post condition:renvoie un tableau de n
    entier compris entre a et b
    précondition : a,b et n sont des entiers"""
    tab = []
    for i in range(n):
        tab.append(randint(a,b))
    return tab

print(gen_tab(10,30,70))

#2) def min_tab(t):
"""renvoie les minimumdu tableau t
t est un tableau non vide d'entiers"""
def min_tab(t):
    n = len(t)
    mini = t[0]
    for i in range(1,n):
        if t[i]<mini:
            mini = t[i]
    return mini

assert(min_tab([5,7,9,4,8]) == 4)

#3)

def indice_min_tab(t):
    """renvoie un indice du minimun du tableau t
    t est un tableau non vide d'entiers """
    n = len(t)
    imin = t[0]
    for i in range(1,n):
        #invariant : t[min] est le minimum de t [:i]
        if t[i]< t [imin]:
            imin = i
    return imin

#7)
def convert_tab_to_dico(t):
    dico = {}
    for elem in t:
        if not elem in dico:
            dico[elem] = 0

        dico[elem] += 1
    return dico

    


    

