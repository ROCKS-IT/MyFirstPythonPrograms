class Chrono:
    def __init__(self,h,m,s):
        self.h = h
        self.m = m
        self.s = s
        self._format()

    def __repr__(self):
        return str(self.h)+"h"+str(self.m)+"m"+str(self.s)+"s"

    def __str__(self):
        return str(self.h)+"h "+str(self.m)+"m "+str(self.s)+"s"

    def _format(self):
        self.m += self.s//60
        self.s = self.s%60
        self.h += self.m//60
        self.m = self.m%60

    def avance(self,t):
        self.s += t
        self._format()

    def __add__(self,t1):
        s= self.s + t1.s
        m= self.m + t1.m
        h= self.h + t1.h
        return Chrono(h,m,s)

    def __sub__(self,t1):
            s= self.s + t1.s
            m= self.m + t1.m
            h= self.h + t1.h
            return Chrono(h,m,s)
        
        

