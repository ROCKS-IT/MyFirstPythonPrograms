def tri_bulle(tab):
    for i in range(len(tab)):
        for j in range(0, len(tab)-i-1):
            if tab[j] > tab[j+1] :
                tab[j], tab[j+1] = tab[j+1], tab[j]
    return tab
       
tab = [98, 22, 15, 32, 2, 74, 63, 70]


 

