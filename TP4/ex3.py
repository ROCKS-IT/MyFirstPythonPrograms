v1= []
v2= []
nMax = 10
n= 11
cpt = 0
calcul = 0
while n > nMax or n < 1:
    n = int(input("Quelle est la taille de vos vecteurs [entre 1 et 10] ?"))

while cpt != 2:
    if cpt == 0:
        print("Saisie du premier vecteur :")
        for i in range(n):
            x = float(input(f"v1[{i}]="))
            v1.append(x)
        cpt += 1
    if cpt == 1:
        print("Saisie du second vecteur :")
        for i in range(n):
            x = float(input(f"v1[{i}]="))
            v2.append(x)
        cpt += 1


for i in range(n):
    calcul = calcul + (v1[i]*v2[i])

print("Le produit scalaire de v1 par v2 vaut",calcul)