# La fonction menu !
from random import *

def menu():
    print("Choisis un niveau")
    print("1. Facile ") 
    print("2. Moyen")
    print("3. Difficile")
    print("4  Quitter le programme")
    choix = 0
    while choix==0:
        choix=int(input("ton choix : "))
    if choix==1:
        facile()
    elif choix==2: 
        moyen()
    elif choix==3:
        difficile()
    elif choix==4:
        print("Au revoir !")
        quit()
    else: 
        menu()  




def facile():
    print("Difficulté : Facile")
    nb=1
    score = 0
    while nb<=10:
        aleat1 = randint(1, 100)
        aleat2 = randint(1, 100)
        listes = [(aleat1 + aleat2), (aleat1 - aleat2)]
        aleat3 = listes[randint(0,1)]
        if aleat3 == (aleat1 + aleat2):
            print("Combien fait", aleat1, "+",aleat2)
        elif aleat3 == (aleat1 - aleat2):
            print("Combien fait", aleat1, "-",aleat2)
        reponse = int(input("réponse = "))
        nb = nb + 1
        result = aleat3
        if reponse==result :
            print("Réponse correcte")
            score = score + 1
        elif reponse!=result :
            score = score + 0
        print("Voici la correction:", result)
    print("Ton score est:", score, "/20")
    if score>5 :
        print("Bravo tu es très fort")
    elif score == 5:
        print("Tu as la moyenne")
    elif score<5 :
        print("Tu dois encore t'entraîner")
   


def moyen():
    print("Difficulté : Moyen")
    nb=1
    score = 0
    while nb<=10:
        aleat1 = randint(-100, 0)
        aleat2 = randint(-100, 0)
        listes = [(aleat1 + aleat2), (aleat1 - aleat2)]
        aleat3 = listes[randint(0,1)]
        if aleat3 == (aleat1 + aleat2):
            print("Combien fait", aleat1, "+",aleat2)
        elif aleat3 == (aleat1 - aleat2):
            print("Combien fait", aleat1, "-",aleat2)
        reponse = int(input("réponse = "))
        nb = nb + 1
        result = aleat3
        if reponse==result :
            print("Réponse correcte")
            score = score + 1
        elif reponse!=result :
            print("Réponse fausse")
            score = score + 0
        print("Voici la correction:", result)
    print("Ton score est:", score, "/20")
    if score>5 :
        print("Bravo tu es très fort")
    elif score == 5:
        print("Tu as la moyenne")
    elif score<5 :
        print("Tu dois encore t'entraîner")
    

def difficile():
    print("Difficulté : Difficile")
    nb=1
    score = 0
    while nb<=10:
        aleat1 = randint(-20, 50)
        aleat2 = randint(-20, 50)
        aleat4 = randint(-20, 50)
        listes = [(aleat1 * aleat2), (aleat1 + aleat4 - aleat2), \
                  (aleat2 * aleat4 * aleat1), (aleat4 - aleat2 * aleat1), \
                  (aleat1 - aleat4 + aleat2), (aleat4 * aleat2 - aleat1)]
        aleat3 = listes[randint(0, 5)]
        if aleat3==(aleat1 + aleat4 - aleat2) :
            print("Combien fait", aleat1, "+" ,aleat4, "-", aleat2)
        elif aleat3==(aleat2 * aleat4 * aleat1) :
            print("Combien fait", aleat2, "*", aleat4, "*", aleat1)
        elif aleat3==(aleat4 - aleat2 * aleat1) :
            print("Combien fait", aleat4, "-", aleat2, "*", aleat1)
        elif aleat3 == (aleat1 - aleat4 + aleat2):
            print("Combien fait", aleat1, "-", aleat4, "+", aleat2)
        elif aleat3== (aleat4 * aleat2 - aleat1):
            print("Combien fait", aleat4, "*", aleat2, "-", aleat1)
        elif aleat3 == ((aleat1 * aleat2)):
            print("Combien fait", aleat1, "*",aleat2)
        reponse = int(input("réponse = "))
        nb = nb + 1 
        result = aleat3
        if reponse==result :
            print("Réponse correcte")
            score = score + 1
        elif reponse!=result :
            print("Réponse fausse")
            score = score + 0
        print("Voici la correction:", result)
    print("Ton score est:", score, "/20")
    if score>5 :
        print("Bravo tu es très fort")
    elif score == 5:
        print("Tu as la moyenne")
    elif score<5 :
        print("Tu dois encore t'entraîner")
    
menu() 

