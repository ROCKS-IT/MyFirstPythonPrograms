#

from Pile import *

def testParenthese(expr):
    p=Pile()
    for car in expr:
        if car == "(":
            p.empiler(car)
        elif car == ")":
            if p.est_vide():
                return False
            else:
                p.depiler()
    return p.est_vide()
    
        
        
        
        
