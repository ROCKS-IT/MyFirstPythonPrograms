#creation d'une classe pile
class Pile:
    def __init__(self):
        self.data = []

    def est_vide(self):
        return self.data == []

    def empiler(self,v):
        self.data.append(v)

    def depiler(self):
        if self.est_vide():
            raise Exception("pile vide")
        return self.data.pop()

    def __str__(self):
        return " | ".join([str(v) for v in self.data])

    def taille(self):
        return len(self.data)

def remplirpile(P,lst):
    for elt in lst:
        P.empiler(elt)

def reverse(P):
    Q = Pile()
    while not P.est_vide():
        a = P.depiler()
        Q.empiler(a)
    return Q

def reverse2(P):
    Q = Pile()
    R = Pile()
    while not P.est_vide():
        a = P.depiler()
        Q.empiler(a)
        R.empiler(a)
    while not R.est_vide():
        a = R.depiler()
        P.empiler(a)
    return Q

def intervert(P):
    a = P.depiler()
    b = P.depiler()
    P.empiler(a)
    P.empiler(b)
    return P

def litN(P,n):
    Q = Pile()
    for i in range(n):
        if P.est_vide():
            P = reverse(Q)
            return None
        a= P.depiler()
        Q.empiler(a)
    while not Q.est_vide():
        b= Q.depiler()
        P = empiler(b)
    return a

def litN_v2(P,n):
    Q= Pile()
    i= 0
    while i < n and not P.est_vide():
        a= P.depiler()
        Q. empiler(a)
        i += 1
    if i == n :
        return a
    else:
        return None

def rotpile(P):
    if P.est_vide():
        return
    Q = Pile()
    a= P.depiler()
    while not P.est_vide():
        x = P.depiler()
        Q.empiler(x)
    P.empiler(a)
    while not Q.est_vide():
        x = Q.depiler()
        P.empiler(x)

def taille(P):

def rotkpile(p,k):
    if p.est_vide():
        return
    q = Pile()
    r = Pile()
    for i in range(k):
        x = p.depiler()
        r.empiler(x)
    while not p.est_vide():
        x = p.depiler()
        q.empiler(x)
    while not r.est_vide():
        x = r.depiler()
        p.empiler(x)
    while not q.est_vide():
        x = q.depiler()
        p.empiler(x)
    

P = Pile()
remplirpile(P,[7,3,2,1])
print("P:",P)
Q = reverse2(P)
print("Q:",Q)
print("P:",P)
  
        
        
        
