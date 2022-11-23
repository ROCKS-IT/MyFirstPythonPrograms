#EXERCICE 5
debut= int(input("heure de début:"))
fin= int(input("heure de fin:"))
result = 0
Npay =0
Nopay= 0


#FULL PAYE
if (debut>=7 and debut<=17)and(fin>=7 and fin<=17):
    Npay = fin-debut
    result = (fin-debut)*2
#FULL PAS PAYE
if (debut<=7 or debut>=17)and(fin<=7 or fin>=17):
    Nopay = fin - debut
    result = fin-debut
#DEBUT PAYE FIN NON PAYE
if (debut>=7 and debut<=17)and fin>17:
    Nopay = fin-17
    Npay = abs(debut-17)
    result = Nopay + (Npay*2)




#DEBUT NON PAYE ET FIN PAYE
#if (debut>=7 or debut<=17)and(fin>=7 and fin<=17):
    #result = 0



print("le tarif est de:",result,"euro")


