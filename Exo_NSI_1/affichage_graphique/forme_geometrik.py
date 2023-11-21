from turtle import *
def carre(cotecar):
    for i in range(4):
        forward(cotecar)
        right(90)

def drapeau(piquet,cotecar):
    left(90)
    forward(piquet)
    carre(cotecar)

def panneau(piquet,cotecar):
    left(90)
    forward(piquet)
    left(45)
    carre(cotecar)

def triangle(cotetri):
    for i in range(3):
        forward(cotetri)
        left(120)

def maison(cotecar,cotetri):
    carre(cotecar)
    triangle(cotetri)

def malte(cotetri):
    right(30)
    for i in range(4):
        right(90)
        triangle(cotetri)
        
def diamand(cotetri,cotecar):
    triangle(cotetri)
    left(150)
    carre(cotecar)
    forward(cotecar)
    right(90)
    triangle(cotetri)
    forward(cotecar)
    left(120)
    carre(cotecar)

def diamande(cotetri,cotecar):
    for i in range(6):
        maison(cotetri,cotecar)
        right(100)
    

    
    
    

    
