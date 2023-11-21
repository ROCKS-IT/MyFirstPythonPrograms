L1 = [1,3,5,12]
L2 = [-2,4,8,15]

def fusion0(L1,L2):
    L = []
    i1 = 0
    i2 = 0
    while i1 < len(L1) or i2 < len(L2):
        if i1 >= len(L1):
            L = L+L2[i2:]
            break
        if i2 >= len(L2):
            L = L+L1[i1:]
            break
        if L1[i1] < L2[i2]:
            L.append(L1[i1])
            i1 += 1
        else:
            L.append(L2[i2])
            i2 += 1
    
def fusion(tab,deb,m,fin):
    L = tab[deb:m]
    R = tab[m:fin]
    i, j = 0, 0
    for k in range (deb,fin):
        if i >= m-deb:
            tab[k] = R[j]
            j += 1
        elif j >= fin-m:
            tab[k] = L[i]
            i += 1
        elif L[i] <= R[j]:
            tab[k] = L[i]
            i += 1
        else:
            tab[k] = R[j]
            j+=1

def tri_fusion(tab, deb, fin):
    if fin - deb > 1:
        m = (deb+fin)//2
        tri_fusion(tab,deb,m)
        tri_fusion(tab,m,fin)
        fusion(tab,deb,m,fin)
