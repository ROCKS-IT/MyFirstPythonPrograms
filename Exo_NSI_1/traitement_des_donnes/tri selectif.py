def position(t,i):
    for k in range(i,0,-1):
        if t[k-1]<=t[i]:
            return k


    return 0

def inserer(t,k,i):
    v = t[i]
    for j in range(i,k,-1):
        t[j]=t[j-1]
    t[k] = v

def tri_insertion(t):
    for i in range(1,len(t)):
        k= position(t,i)
        inserer(t,k,i)
