
L = []


tempminlocation = 0
save = 0

n = int(input("Donne la taille du tableau:"))
for i in range(n):
    val = int(input("Valeur:"))
    L.append(val)

tempminvalue = L[0]

print(L)


for i in range (n-1):
    for w in range(i+1, len(L)):
        if tempminvalue > L[w]:
            tempminvalue = L[w]
            tempminlocation = w
    save = L[i]
    L[i]=tempminvalue
    L[tempminlocation]=save
    #REMISE A ZERO DES VALEURS
    tempminlocation = i+1
    tempminvalue = L[i+1]
    save = 0
    print(L)








