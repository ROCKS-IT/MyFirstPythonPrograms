
n = int(input("saisir un entier non nul"))
res = ""
symbole = "0123456789ABCDEF"
while n!=0:
    q = n//16
    r = n % 16
    n = q
    res = symbole[r] + res

print(res)

















#n = int(input("saisir un entier non nul"))
#res = ""
#while n!=0:
    #q = n//2
    #r = n % 2
    #n = q
    #res = str(r) + res

#print(res)
