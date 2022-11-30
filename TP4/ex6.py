
L = []

y = 0
N = 0
saveTi= 0
saveTy = 0
position = 0
p=0

N = int(input("Entrez la valeur"))

for i in range(N):
    x = int(input(f"Valeur n{i}"))
    L.append(x)


for i in range(N):
    saveTy = L[i]


    while y != N:
        if L[y] < saveTy:
            saveTy = L[y]
            position = y

        y =  y+1

    saveTi = L[i]
    L[i] = saveTy
    L[position] = saveTi
    p += 1
    y=0
    y = p
    position = y
    print(L)
