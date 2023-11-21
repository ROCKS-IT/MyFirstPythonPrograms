from random import randint
from math import sqrt

def simu_X():
    alea = randint(1,100)
    if alea <= 78:
        return 1
    return 0

def simu_Y():
    return simu_X()+2*simu_X()-simu_X()

def simu_S():
    s = 0
    for i in range(7):
        s = s + simu_X()
    return s

def echantillon_S():
    echantillon = []
    for i in range(n):
        echantillon.append(simu_S())
    return echantillon

def proba_S(k):
    s = 0
    for simu in range(100000):
        s = s +simu_S()
    return s/100000


def estim_esp_S():
    s= 0
    for simu in range(100000):
        s = s + simu_S()
    return s/100000

def estim_var_S():
    s = 0
    esp = estim_esp_S()
    for simu in range(100000):
        s = s + (simu_S()-esp)**2
    return s/100000
    
