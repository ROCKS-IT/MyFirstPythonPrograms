tab = [5,2,4,8,1,3]
temp = 0
tempx=0
tempy=0
def inverse(x,y):
    print(tab)
    for i in range(len(tab)):
        if x == tab[i]:
            tempx=i
        if y == tab[i]:
            tempx=i
        if x not in tab or y not in tab:
            print("Valeur de x ou y pas dans le tableau")
            break
    else:
        temp=tab[tempx]
        tab[tempx]=tab[tempy]
        tab[tempy]=temp
        print(tab)
        return "Valeur Inverse"



        
            
            
    
            
