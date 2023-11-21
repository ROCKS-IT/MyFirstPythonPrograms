

def somme(n):
    s = 0
    for i in range(n+1):
        s=s + i
    return s

def somme2(n):
    if n == 0:
        return 0
    else:
        return n + somme2(n-1)

def somme3(x,n):
    if n == 0:
        return 1
    else:
        return x * puissance(x,n-1)

def puissance(x,n):
    if n == 0:
        return 1
    elif x % 2 == 0:
        return puissance(x,n//2)
    else:
        return x * puissance(x,(n-1)//2)
        
        
    
