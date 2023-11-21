#LES GROS FILE LA OEOEOEOEOEO

class File:
    def __init__(self):
        self.data = []

    def est_vide(self):
        return self.data == []

    def empiler(self,v):
        self.data.append(v)

    def depiler(self):
        if self.est_vide():
            raise Exception("file vide")
        return self.data.pop(0)

    def __str__(self):
        return " -> ".join([str(v) for v in self.data])

    def taille(self):
        return len(self.data)
    
                
