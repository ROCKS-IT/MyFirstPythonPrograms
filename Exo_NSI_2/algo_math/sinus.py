from math import *
#création de tableau
def sinuss():
    tab=[]
    x=0
    for i in range(20):
        tab.append(sin(x))
        x += 0.5
        print(x)
    return tab
        
