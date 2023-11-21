#classe Intervalle

class Intervalle:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.est_vide():
            return "[]"
        return "["+str(self.a)+";"+str(self.b)+"]"

    def est_vide(self):
        """envoie True si l'intervalle et vide ici b<a"""
        return self.b < self.a

    def __len__(self):
        """renvoie la longueur de l'intervalle"""
        if self.est_vide():
            return 0
        else:
            return self.b - self.a

    def __contains__(self,nombre):
        """Renvoie True si nombre appartient dans l'intervalle"""
        return self.a <= nombre and nombre <= self.b

    def __eq__(self,inter):
        """Renvoie True si les intervalles sont égaux
           tous les intervalles vides sont considérés égaux"""
        if self.est_vide()and Inter.est_vide():
            return True
        elif self.a == inter.a and self.b == inter.b:
            return True
        return False

    def __le__(self,inter):
        if self.est_vide():
            return True
        if self.a >= inter.a and self.b <= inter.b:
            return True
        else:
            return False

def intersection(self,interv):
    if self.est_vide() or interv.est_vide():
        return Intervalle(0,-1)
    if interv.b < self.a or self.b < interv.a:
        return Intervalle(0,1)
    if interv.a in self:
        return Intervalle(interv.a, self.b)
    if interv.b in self:
        return Intervalle(interv.a, interv.b)
    if interv <= self:
        return interv
    if self <= interv:
        return self

    
# test de la classe
I1 = Intervalle(-2,7)
I2 = Intervalle(5,5)
I3 = Intervalle(4,2)

print("La longueur de I1 est :",len(I1))
print("La longueur de I2 est :",len(I2))
print("La longueur de I3 est :",len(I3))
