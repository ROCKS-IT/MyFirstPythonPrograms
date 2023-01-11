L = []

n = int(input("Donne la taille du tableau:"))
for i in range(n):
    val = int(input("Valeur:"))
    L.append(val)

print(sorted(L))

L.sort()
print(L)