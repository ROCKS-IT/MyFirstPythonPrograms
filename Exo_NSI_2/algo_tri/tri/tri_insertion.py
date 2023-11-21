def dist2(pt):
    return pt[0]*pt[0]+pt[1]*pt[1]

def tri_insertion(tab,dist2):
    for i in range(1,len(tab)):
        x = tab[i]
        j = i
        while j > 0 and dist2(tab[j-1]) > dist2(x):
            tab[j] = tab[j-1]
            j = j-1
        tab[j]=x
    return tab


tab = [(5,2),(8,3),(1,6),(7,4),(-2,5)]


            


