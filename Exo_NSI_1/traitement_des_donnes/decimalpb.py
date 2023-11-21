from math import sqrt
while True:
    try:
        chaine = input ("donner un nombre décimal:")
        chaine = chaine.replace(",",".")
        n = float(chaine)
        racine = sqrt(n)
        assert n > 0
        racine = sqrt(n)
    except ValueError:
        print(chaine,"Le nombre doit etre décimal:")
    except AssertionError:
        print("Le nombre doit etre positif:")
    else:
        print("La racine de ",n," est:",racine)
        break
        
