from random import *
mystere = randint(0,100)
essai = 0
reponse = -1

while reponse != mystere:
    essai +=1
    reponse = int(input("devine le nombre! :"))
    if reponse < mystere:
        print("plus grand")
    if reponse > mystere:
        print("plus petit")
    elif reponse == mystere:
        print("bravo en",essai,"coups")
