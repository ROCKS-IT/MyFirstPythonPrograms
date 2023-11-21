from random import randint
def U(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return U(n-1)+U(n-2)




def alea_liste(n):
    tab = []
    for i in range(n):
        tab.append(randint(-1000,1000))
    return tab



def maxi(liste):
    v_max = liste[0]
    pos_max = 0
    for i in range(len(liste)):
        if v_max < liste[i]:
            v_max = liste[i]
            pos_max = i
    return v_max,pos_max

print("liste aléatoire:")
liste = alea_liste(10)
print(liste)

v_max, pos_max = maxi(liste)
print("la valeur max est",v_max,"en position",pos_max +1)
