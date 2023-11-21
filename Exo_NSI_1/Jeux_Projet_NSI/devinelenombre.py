from random import randint

mystere = randint(0,999)
essai = 0
reponse = -1
triche = 1001

while reponse != mystere :
    essai += 1
    reponse = int(input("devine le nombre ! :"))
    if reponse == triche:
        essai = essai - 1
        print("code de triche activé :",mystere,"est le nombre mystère")
    if reponse < mystere :
        print("plus grand")
    if reponse > mystere :
        print("plus petit")
    if reponse == mystere :
        print ("bravo tu magnifquement beau tu la fais en",essai,"essai")









