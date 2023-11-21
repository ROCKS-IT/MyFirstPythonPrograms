from random import randint
from math import sqrt

def list_alea_croiss(n):
    v = randint (1,50)
    lst = [v]
    for i in range(n):
        v = v+ randint(1,50)
        lst.append(v)
    return lst
        
        
def rech_dico(lst,x):
    d= 0
    f= len(lst)-1
    while f-d >= 0:
        m= (f+d)//2
        if x == lst[m]:
            return lst[m]
        elif x < lst[m]:
            f = m-1
        elif x > lst[m]:
            d = m+1
        else:
            return m
    return -1

def rech_dico_recurs(lst,x,d,f):
    m= (f+d)//2
    if f-d < 0:
        return -1
    if x == lst[m]:
        return m
    elif x > lst[m]:
        return rech_dico_recurs(lst,x,m+1,f)
    elif x < lst[m]:
        return rech_dico_recurs(lst,x,d,m-1)

def rech(lst,x):
    for i in range (len(lst)):
        if lst[i] == x:
            return i
    return -1
        
    

lst = list_alea_croiss(20)
print(lst)
#nb = int(input("entrer nbr"))
#print(rech_dico(lst,nb))
        

            

            
        

    
