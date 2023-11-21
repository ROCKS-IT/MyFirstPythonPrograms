#calculatrice polonaise inversée

from Pile import *

#chaque caractère de expre est soit un chiffre
#soit un des quatres opérateurs + - * /
def caculatrice(expr):
    p=Pile()
    for c in expr:
        if c in "0123456789":
            p.empiler(int(c))
        elif c in "+-*/":
            b = p.empiler()
            a = p.empiler()
            if c == "+":
                p.empiler(a+b)
            elif c == "-":
                p.empiler(a-b)
            elif c == "*":
                p.empiler(a*b)
            elif c == "/":
                p.empiler(a/b)
    return p.depiler()


    
        
        
