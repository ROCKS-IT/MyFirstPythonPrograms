


choix=int(input("1=while 2=for :"))

if choix == 1:
    n = int(input("Donne factorielle:"))
    cpt = 0
    x = n
    while cpt != n-1:
        cpt +=1
        x *= n-cpt
    print(x)

else:
    n = int(input("Donne factorielle:"))
    x = n
    for i in range(n-1):
        x *= n-(i+1)
    print(x)
