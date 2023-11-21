#generateur de question
from random import randint
score = 0
for x in range (5):
    mysterea = randint(0,10)
    mystereb = randint(0,10)
    reponsesys = mysterea*mystereb
    print("Question",x+1,"Combien font",mysterea,"fois",mystereb,)
    reponseuti = int(input("Ca fait: "))
    if reponsesys != reponseuti:
        print("La réponse est ",reponsesys,".")
        print("Recommence, esclave!")
    else:
        print("Bravo")
        score+=1
print("Le score est de",score,"/ 5")
print("Bravo tu as fini l'exercice")

