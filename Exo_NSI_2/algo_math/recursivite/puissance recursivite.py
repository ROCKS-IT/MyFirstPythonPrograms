def puissance(x,n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        result = puissance(x,n //2)
        return result * result
    else:
        result = puissance(x ,(n -1)//2)
        return x * result * result
