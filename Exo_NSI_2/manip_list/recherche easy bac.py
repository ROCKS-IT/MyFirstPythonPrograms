def recherche(elt,tab):
    for i in range(len(tab)):
        if tab[i] == elt :
            return i+1
    else:
        return -1


tab1 = [5,9,10,4,8]



def max(tab):
    x=tab[0]
    for i in range(len(tab)):
        if x < tab[i]:
            x = tab[i]
    return x


def croissant(a,b,c):
    if a < b < c:
        print("croissant")
    else:
        print("non")



def fichepaye(heure,argenth):
    if heure <= 160:
        salaire = heure*argenth
        print(salaire)
    elif heure >= 161 and heure <= 200:
        surplus = (heure - 160) * (argenth*1.25)
        print(surplus)
        salaire = (1600) + surplus
        print(salaire)
    elif heure >= 201:
        surplus2 = (heure - 200) * (argenth*1.50)
        surplus = (39) * (argenth*1.25)
        print(surplus,surplus2)
        salaire = (1600)+(surplus)+(surplus2)
        print(salaire)


        

        
