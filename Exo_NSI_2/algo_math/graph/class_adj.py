

#orienté (merci mec pour l'info 03/01/2023)
class Graphe :

    def __init__ (self):
        self.success = {}

    def ajouter_sommet(self,s):
        if s not in self.sucess:
            self.success[s] = set()

    def ajouter_arc(self,s1,s2):
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        self.success[s1].add(s2)

    def arc(self,s1,s2):
        return s2 in self.success[s1]

    def sommets(self):
        return list(self.success)

    def voisins(self,s):
        return self.success[s]
    
        
        
