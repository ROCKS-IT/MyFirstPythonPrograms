class Cellule:
    def __init__(self, valeur, suivant) -> None:
        self.valeur = valeur
        self.suivant = suivant
    
    def __repr__(self):
        return str(self.valeur)

class ListeChainee:
    def __init__(self):
        self.tete = None

    def est_vide(self):
        return self.tete is None

    def __repr__(self):
        result = []
        curs = self.tete
        while curs is not None:
            redult.append(curs.valeur)
            curs = curs.suivant
        return str(result)

    def prepend(self,v):
        c = Cellule(v,self._tete)
        self._tete = c

    def pop(self):
        if not self.est_vide():
            valeur = self._tete.valeur
            self._tete = self ._tete.suivant
            return valeur
        raise IndexError("Liste Vide")


