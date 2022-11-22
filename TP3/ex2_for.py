from time import *
x = int(input("entre nombre:"))
for i in range(x+1):
    sleep(0.2)
    print(x)
    sleep(0.2)
    x -= 1