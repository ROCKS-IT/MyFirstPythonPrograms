# rendu monnaie

pieces = [100,50,10,2,1]
piece = [4,3,1]

def rendu (s):
    return [ s//5 , (s % 5) // 2 ,(s % 5) % 2]

def rendu_monnaie_G(s):
    result = {}
    for p in pieces:
        result[p]= s//p
        s = s % p
    return result

def rendu_monnaie_Rec(s):         #LE NOMBRE DE PIECES
    if s == 0:
        return 0
    r = s
    for p in piece :
        if p <= s:
            r = min(r,1+rendu_monnaie_Rec(s-p))
    return r

memo = {}
def rendu_monnaie_mem(s):         #Avec mémorisation
    if s in memo:
        return memo[s]
    if s == 0:
        memo[s]
    r = s
    for p in piece :
        if p <= s:
            r = min(r,1+rendu_monnaie_Rec(s-p))
    memo [s] = r
    return r

