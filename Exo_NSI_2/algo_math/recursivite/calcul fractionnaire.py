from math import gcd #importation de la fonction pgcd

def simplify(num,den):
    pgcd = gcd(num,den)
    nresult = num//pgcd
    dresult = den//pgcd
    if dresult < 0:
        dresult = -dresult
        nresult = -nresult
    return (nresult,dresult)


def cree_frac(num,den):
    assert type(num) == int and type(den) == int
    assert den != 0
    return simplify(num,den)

def somme_frac(f1,f2):
    a,b,c,d = f1[0],f1[1],f2[0],f1[1]
    num = a*d+c*b
    den = b*d
    return simplify(num,den)



    
    
