

def trouver_longueur(text, lettre):
    f = 0
    for i in range(len(text)):
        if text[i] == lettre:
            f= f+1
            
        
    return f
        
print(trouver_longueur("ooooo", "o"))


liste = [5,3,6]
def maxi(liste):
    m=liste[0]
    for v in liste:
        if v > m:
            m=v
    return m
    
    
