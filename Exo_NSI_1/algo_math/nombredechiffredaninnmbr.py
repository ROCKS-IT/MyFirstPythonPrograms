n = int(input ("Choisi un nombre entier positif ou nul:"))

if n <= 0 :
    print ("Tu ne sais pas lire !")

else :
    n = int(input ("Choisi un nombre entier positif ou nul:"))
    longueur = 1
    while n//10>0 :
        n = n // 10
        longueur += 1
    print (longueur,"chiffres present dans se nombre.")



