# Demande le nombre d'étudiants à l'utilisateur
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0;
# déclaration d’une liste vide qui va contenir autant de notes que
notes = []
result =0

for i in range(nombreEtudiants):
    notes.append(int(input("Note d'un élève:")))

for i in range(len(notes)):
    result = result + notes[i]
moyenne = (result/nombreEtudiants)
print("moyenne de classe :",moyenne)

print("Numéro de l’Etudiant | note | ecart a la moyenne")
for i in range(nombreEtudiants):
    print(i,"|",notes[i],"|",notes[i]-moyenne)