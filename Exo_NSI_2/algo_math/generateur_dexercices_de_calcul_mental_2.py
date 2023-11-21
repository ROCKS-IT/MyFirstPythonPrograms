# La fonction menu !
from random import *

def addition():
    print("Niveau1 : Addition")
    nb=1
    score = 0
    while nb<=20:
        aleat1 = random.randint(1, 1000)
        aleat2 = random.randint(1, 1000)
        print("Combien fait", aleat1, "+",aleat2)
        reponse = int(input("réponse = "))
        nb = nb + 1
        result = (aleat1 + aleat2)
        if reponse==result :
            score = score + 1
        elif reponse!=result :
            score = score + 0
        print("Voici la correction:", result)
    print("Ton score est:", score, "/20")
    if score>=16 :
        print("Bravo tu es très fort")
    if score<5 :
        print("Tu dois encore t'entraîner")

def menu():
    print("Choisis un niveau")
    print("1. Addition ") 
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Opérations à plusieurs nombres")
    choix = 0
    while choix==0:
        choix=int(input("ton choix : "))
    if choix==1:
        addition()
    elif choix==2: 
        soustraction()
    elif choix==3:
        multplication()
    elif choix==4:
        touteopérations()
    elif choix==9:
        print("Au revoir !")
        exit
    else: 
        menu() 
    if choix!=9:
        menu() 

menu()

   

def soustraction():
    print("Niveau 2 : Soustraction")
    nb=1
    score = 0
    while nb<=20:
        aleat1 = random.randint(-20, 500)
        aleat2 = random.randint(-20, 500)
        print("Combien fait", aleat1, "-",aleat2)
        reponse = int(input("réponse = "))
        nb = nb + 1
        result = (aleat1 - aleat2)
        if reponse==result :
            score = score + 1
        elif reponse!=result :
            score = score + 0
        print("Voici la correction:", result)
    print("Ton score est:", score, "/20")
    if score>=16 :
        print("Bravo tu es très fort")
    if score<5 :
        print("Tu dois encore t'entraîner")
    

def multplication():
    print("Niveau 3 : Multiplication")
    nb=1
    score = 0
    while nb<=20:
        aleat1 = random.randint(1, 100)
        aleat2 = random.randint(1, 100)
        print("Combien fait", aleat1, "*",aleat2)
        reponse = int(input("réponse = "))
        nb = nb + 1
        result = (aleat1 * aleat2)
        if reponse==result :
            score = score + 1
        elif reponse!=result :
            score = score + 0
        print("Voici la correction:", result)
    print("Ton score est:", score, "/20")
    if score>=16 :
        print("Bravo tu es très fort")
    if score<5 :
        print("Tu dois encore t'entraîner")
    

def touteopérations():
    print("Niveau 4 : Toutes les opérations")
    nb=1
    score = 0
    while nb<=20:
        aleat1 = random.randint(-20, 100)
        aleat2 = random.randint(-20, 100)
        aleat4 = random.randint(-20, 100)
        listes = [(aleat1 + aleat4 - aleat2), (aleat2 * aleat4 * aleat1), (aleat4 - aleat2 * aleat1), (aleat1 - aleat4 + aleat2), (aleat4 * aleat2 - aleat1)]
        aleat3 = listes[random.randint(0, 4)]
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
        reponse = int(input("réponse = "))
        nb = nb + 1 
        result = aleat3
        if reponse==result :
            score = score + 1
        elif reponse!=result :
            score = score + 0
        print("Voici la correction:", result)
    print("Ton score est:", score, "/20")
    if score>=16 :
        print("Bravo tu es très fort")
    if score<5 :
        print("Tu dois encore t'entraîner")
    
        

