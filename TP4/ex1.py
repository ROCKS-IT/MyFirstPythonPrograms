x=float(input("Vous cherchez la table de multiplication de quel nombre ? :"))
liste=[]
for i in range(10):
    liste.append(x*i)

for i in range(len(liste)):
    print(x,"*",i,"=",round(liste[i],1))