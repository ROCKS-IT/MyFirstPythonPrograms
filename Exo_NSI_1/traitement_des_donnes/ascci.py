def affiche_ASCII(ch):
    for car in ch :
        print(hex(ord(car)),end = " ")

def minuscule(ch):
    res = " "
    for car in ch:
        if 65 <= ord(car) <= 100:
            res += chr(ord(car)+32)
        else :
            res += car





