
class Graphe :

    def __init__ (self,n):
        self.n = n
        self.mat_adj = [[ False ] * n for i in range(n)]


    def ajouter_arc (self,s1,s2):
        self.mat_adj[s1][s2] = True


    def arc (self,s1,s2):
        return self.mat_adj[s1][s2]


    def successeurs (self ,s):
        success = []
        for i in range(self.n):
            if self.mat_adj[s][i]:
                success.append(i)
        return success


    def predeccesseurs (self ,s):
        predes = []
        for j in range(self.n):
            if self.mat_adj[j][s]:
                predes.append(j)
        return predes

if __name__ == '__main__':
    g = Graphe(4)
