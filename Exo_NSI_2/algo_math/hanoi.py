def deplacer(d,f):
    print("deplacer de",d,"vers",f)

def hanoi(n,dep,fin,inter):
    if n ==1:
        deplacer(deb,fin)
    else:
        hanoi(n-1,deb,inter,fin)
        deplacer(deb,fin)
        hanoi(n-1,inter,fin,deb)

hanoi(4,1,3,2)
    
