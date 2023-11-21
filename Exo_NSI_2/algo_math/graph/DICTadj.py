

#non-orienté dictionnaire bizar pas finis
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

    def voisinage(self,s):
        return self.success[s]
    
g = GrapheNO ()
g.ajouter_arete('A','E')
g.ajouter_arete('A','C')
g.ajouter_arete('B','A')
g.ajouter_arete('B','D')
g.ajouter_arete('C','D')
g.ajouter_arete('D','E')
g.ajouter_arete('D','A')
g.ajouter_arete('E','B')
g.ajouter_arete('E','C')
g.ajouter_arete('E','F')
g.ajouter_arete('F','D')

        
