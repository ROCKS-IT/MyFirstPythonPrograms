#Question C:
x= 0
dessousdix=0
entredixquinze=0
supquinze=0
cpt= 0
while cpt != 10:
    x= int(input("donne nombre:"))
    if x<0 and x > 20:
        x = int(input("donne nombre:"))
    elif (x < 10):
        dessousdix +=1
        cpt+=1
    elif(x>=10 and x < 15):
        entredixquinze+=1
        cpt += 1
    elif(x>=15 and x<=20):
        supquinze+=1
        cpt += 1

print("Il y'a",dessousdix,"valeurs inférieur strictement à 10")
print("Il y'a",entredixquinze,"valeurs supérieur ou égale à 10 et inférieur strictement à 15")
print("Il y a",supquinze,"valeurs supérieur ou égale à 15")