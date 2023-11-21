from random import *
tab = [randint(-1000,1000) for i in range(5000)]
tab1 = list(tab)


def tri_selection(tab):
    n = len(tab)
    for i in range(n-1):
        mini = i
        for j in range(i+1,n):
            if tab[j] < tab[mini]:
                mini = j
        if mini != i:
            tab[i], tab[mini] = tab[mini], tab[i]



def tri_selection_while(tab):
    n = len(tab)
    i = 0
    while i < n-1:
        mini = i
        j= i +1
        while j<n:
            if tab[j] < tab[mini]:
                mini = j
            j +=1
        if mini != i:
            tab[i], tab[mini] = tab[mini], tab[i]
        i += 1
        
def tri_selectiondistance(tab,dist2):
    m = len(tab)
    for i in range(n-1):
        mini = i
        for j in range(i+1,n):
            if dist2(tab[j]) < dist2(tab[mini]):
                mini = j
        if mini != i:
            tab[i], tab[mini] = tab[mini], tab[i]
