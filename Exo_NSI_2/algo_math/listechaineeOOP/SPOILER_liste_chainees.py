class Cellule:
    def __init__(self,valeur,suivant):
        self.valeur = valeur
        self.suivant = suivant

    def __repr__(self):
        return str(self.valeur)

class ListeChainee:
    def __init__(self):
        self._tete=None
        self._queue=None
        self._longueur=None

    def est_vide(self):
        return self._tete is None

    def __repr__(self):
        result = []
        curs = self._tete
        while not curs is None:
            result.append (curs.valeur )
            curs = curs.suivant
        return str(result)

    def prepend (self ,v):
        c = Cellule (v, self._tete )
        self._tete = c
        if self._tete.suivant is None:
            self._queue = c

    def append(self):
        if self.est_vide():
            self.prepend(v)
        else:
            c = Cellule(v,None):
                self._queue.suivant = c
                self._queue = self._queue.suivant
  
    def pop (self):
        if not self.est_vide ():
            valeur = self._tete.valeur
            self._tete = self._tete.suivant
            return valeur
        raise IndexError("Liste vide !!")

    def __len__(self):
        return self._longueur

    def lit_tete(self):
        if self.est_vide():
            return None
        else:
            return self._tete.valeur

    def lit_queue(self):
        

    def lit_curseur(self):
         

    

    
    
