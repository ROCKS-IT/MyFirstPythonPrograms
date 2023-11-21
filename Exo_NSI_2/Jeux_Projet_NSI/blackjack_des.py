from random import *
totalmach = 0
totalplayer = 0
boucle = 0
y=0
while boucle == 0:
    y = int(input("nombre de dès que je veux lancer:"))
    for i in range(y):
        totalmach = totalmach + randint(1,6)
        totalplayer = totalplayer + randint(1,6)
        if totalmach + totalplayer > 42:
            print("NULLE DEGAGE")
            boucle = int(input("zero:"))
        if totalmach > 21:
            print("LE BANQUIER A PERDU",totalmach,"contre",totalplayer)
            boucle = int(input("zero:"))
            totalmach = 0
            totalplayer = 0
        if totalplayer > 21:
            print("LE JOUEUR A PERDU",totalplayer,"contre",totalmach)
            boucle = int(input("zero:"))
            totalmach = 0
            totalplayer = 0           
    
#print(("banquier:"), totalmach, ("joueur:"), totalplayer)
