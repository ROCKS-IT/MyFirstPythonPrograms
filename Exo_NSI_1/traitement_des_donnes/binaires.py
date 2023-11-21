n = int(input("saisir un entier non nul"))
res = ""
while n!=0:
    q = n//2
    r = n % 2
    n = q
    res = str(r) + res

print(res)
