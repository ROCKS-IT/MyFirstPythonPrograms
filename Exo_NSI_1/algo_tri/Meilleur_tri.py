def tripierre(tab):
    x = 0
    temp = 0
    result = []
    while len(tab)>=2:
        for i in range(len(tab)):
            if tab[i]<tab[x]:
                x=i
                temp=tab[i]
        tab.pop(x)
        result.append(temp)
        x=0
        temp=tab[0]
        print(tab,result)
    result.append(tab[0])
    tab.pop(0)
    return result,x,i
                
        
        
        
