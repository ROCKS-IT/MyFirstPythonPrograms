class Cellule:
    def __init__(self,valeur,suivant):
        self.valeur = valeur
        self.suivant = suivant

    def __repr__(self):
        return str(self.valeur)

class ListeChaineeDBL:
    def __init__(self):
        self._tete=None
        self._queue=None
        self._longueur= 0
        self._curseur = None
        self._prec= None

    def est_vide(self):
        return self._tete is None

    def __repr__(self):
        result = []
        curs = self._tete
        while not curs is None:
            result.append (curs.valeur )
            curs = curs.suivant
        return str(result)

    def __len__(self):
        return self._longueur

    def lit_tete(self):
        if self.est_vide():
            return None
        else:
            return self._tete.valeur

    def lit_queue(self):
        if self.est_vide():
            return None
        else:
            return self._queue.valeur

    def lit_curseur(self):
        if self.est_vide():
            return None
        else:
            return self._curseur.valeur

    def avance(self):
        if self._curseur == self._queue:
            return 1
        else:
            self._curseur = self._curseur.suivant
            return 0

    def avance(self):
        if self._curseur == self._tete:
            return 1
        else:
            self._curseur = self._curseur.precedent
            return 0

    def prepend (self ,v):
        c = Cellule (v, self._tete )
        self._tete = c
        self._longueur +=1
        if self._longueur == 1:
            self._curseur = self._tete
            
        if self._tete.suivant is None:
            self._queue = c
       

    def append(self,v):
        if self.est_vide():
            self.prepend(v)
        else:
            c = Cellule(v,None):
                self._longueur +=1
                self._queue.suivant = c
                self._queue = self._queue.suivant
               


    def pop (self):
        if not self.est_vide ():
            self._longueur -= 1
            valeur = self._tete.valeur
            if self._curseur == self._tete:
                self._curseur = self._tete.suivant

            self._tete = self._tete.suivant
            return valeur
        raise IndexError("Liste vide !!")

    
        
    
