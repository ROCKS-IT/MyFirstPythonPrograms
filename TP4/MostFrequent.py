L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
x = 0
cpt = 0
save = 0
sbr = 0
for i in range(len(L1)):
    x = L1[i]
    for y in range(len(L1)):
        if x == L1[y]:
            cpt += 1

    if cpt > save:
        save = cpt
        sbr = L1[i]
    cpt = 0


print("Le nombre le plus frequent dans la liste est le :",sbr,"(",save,"x)")







""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""