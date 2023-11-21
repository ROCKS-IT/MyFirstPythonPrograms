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
            

        
        
arbrel = Noeud("A",Noeud("B",None,Noeud("D")),Noeud("C"))

arbre2 = Noeud("A",Noeud("B",Noeud("C"),Noeud("D")),Noeud("E",None,Noeud("F")))
