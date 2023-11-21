def fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * fact(n-1)


def fact2(n):
    o = 1
    y = 0
    for i in range(n):
        y = n * i
        o=o+1
    return(n,o,y)

for i in range(1,21):
    p=0.45
    n=20
    x =((fact(n)/(fact(i)*fact(n-i)))*(p**i)*(1-p)**(n-i))
    print(x)


