L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
x = L1[0]
total = -1
save = 0
sbr = 0
for i in range(len(L1)):
    x = L1.count(L1[i])
    if x > save:
        save = x
        sbr = L1[i]




print("Le nombre le plus frequent dans la liste est le :",sbr,"(",save,"x)")







""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""