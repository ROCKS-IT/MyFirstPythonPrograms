with open('departements-region.csv','r',encoding='utf-8') as f:
    dep_tab = []
    while True :
        ligne = f.readline().strip()
        if ligne == '':
            break
        liste = ligne.split(',')
        dep_tab.append(liste)

#for i in range(5):
    #print(dep_tab[i])

#ex5

with open('departements-region.csv','r',encoding='utf-8') as f:
    dep_dico = []
    entete = f.readline().strip().split(',')
    while True :
        ligne = f.readline().strip()
        if ligne == '':
            break
        liste = ligne.split(',')
        dico = {}
        for i in range(len(entete)):
            dico[entete[i]] = liste [i]
        dep_dico.append(dico)

for i in range(5):
    print(dep_dico[i])





    
