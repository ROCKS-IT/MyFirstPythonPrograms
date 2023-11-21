

#non-orienté
class GrapheNO:

    def __init__ (self):
        self.voisins = {}

    def ajouter_sommet(self,s):
        if s not in self.voisins:
            self.voisins[s] = set()

    def ajouter_arete(self,s1,s2):
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        self.voisins[s1].add(s2)
        self.voisins[s2].add(s1)

    def arete(self,s1,s2):
        return s2 in self.voisins[s1]

    def sommets(self):
        return list(self.success)

    def voisins(self,s):
        return self.success[s]
    
g = GrapheNO ()
g.ajouter_arete('A','B')
g.ajouter_arete('A','C')
g.ajouter_arete('A','D')
g.ajouter_arete('B','D')
g.ajouter_arete('B','E')
g.ajouter_arete('C','D')
g.ajouter_arete('C','E')
g.ajouter_arete('D','E')
g.ajouter_arete('D','F')
g.ajouter_arete('E','F')

        
