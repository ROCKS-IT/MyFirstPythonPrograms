##############QUESTION 1##############
input("Question 1:")
binome = ('pierre.bourger@uha.fr', 1,  'kevin.de-azevedo@uha.fr', 2)
print("L'édudiant",binome[0],"est en binome avec l'étudiant",binome[2])



################ QUESTION 2 #############
input("Question 2:")
#Transformation en liste car sinon ça focntionne pas.
binome = list(binome)
binome[2]= str(input("Donne le nom du nouveau binome:"))
binome = tuple(binome)
print("L'édudiant",binome[0],"est en binome avec l'étudiant",binome[2])

###### QUESTION 3 ###########
input("Question 3:")
#Transformation en liste car sinon ça focntionne pas.
binome = list(binome)
del(binome[2])
del(binome[2])
binome = tuple(binome)
print("L'édudiant",binome[0],"est seul et triste")

###### QUESTION 4 ###########
input("Question 4:")
#Remise a zero, pour le but de l'exo
binome = ('pierre.bourger@uha.fr', 1,  'kevin.de-azevedo@uha.fr', 2)
binome = list(binome)
binome.append(str(input("Login de la troisième personne:")))
binome.append(3)
binome =tuple(binome)
print(binome)










