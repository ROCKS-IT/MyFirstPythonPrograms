class Noeud:
    def __init__(self,e=None,sag = None,sad = None):
        self.cle = e
        self.sag = sag
        self.sad = sad
        self.parent = None
        if sag:
            sag.parent = self
        if sad:
            sad.parent = self
            
    def montrer(self,tab=0):
        txt = ""
        if self.sad is not None:
            txt += self.sad.montrer(tab+3)
        txt += "\n" + " " * tab + str(self.cle)
        if self.sag is not None:
            txt += self.sag.montrer(tab+3)
        return txt
        
        
        
    def est_vide(self):
        return self.cle is None
        
    def est_feuille(self):
        return self.sag is None and self.sad is None
        
    def racine(self):
        if self.parent:
            return self.parent.racine()
        else:
            return self.cle
    
    def __str__(self):
        return self.montrer()
        
    def taille_arbre(A):
        if A is None or A.est_vide():
            return 0
        else:
            return 1+ taille_arbre(A.sag)+ taille_arbre (A.sad)

    def taille_arbre_It(A):
        p = Pile()
        
    
    def nb_feuilles(A):
        if A is None or A.est_vide():
            return 0
        else:
            if A.est_feuille():
                return 1
            else:
                return nb_feuilles(A.sag)+nb_feuilles(A.sad)
            
    def hauteurNoeud(A):
        if A.parent is None:
            return 0
        if A.parent is None:
            return 0
        else:
            return 1 + hauteurNoeud(A.parent)
            
    def hauteurNoeud_IT(A):
        cpt = 0
        while A.parent is not None:
            A = A.parent
            h += 1
        return h
    
    def hauteurArbre(A):
        if A.parent is None:
            return 0
        if A.est_feuille():
            return 0
        else:
            return 1+max(hauteurArbre(A.sag),hauteurArbre(A.sad))
            
    
        
        


            
    

        
        
arbre1 = Noeud("A",Noeud("B",None,Noeud("D")),Noeud("C"))

arbre2 = Noeud("A",Noeud("B",Noeud("C"),Noeud("D")),Noeud("E",None,Noeud("F")))
