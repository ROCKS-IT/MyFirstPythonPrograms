# Programme qui calcule une moyenne pondérée
from math import *
n = int(input("nombre de notes ? : "))
somme = 0
coefficients = 0
for i in range (1,n+1) :
      print("note",i)
      note = int(input("?: "))
      coef = int(input("?: "))
      somme += coef*note
      coefficients += coef

print("moyenne pondérée : ",somme/coefficients)
