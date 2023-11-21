def affiche(mat):
    for lig in mat:
        if cel:
            print("T", end = " ")
        else:
            print("F", end = " ")
    print()
            



N =5

matrice_Adj = [[False] * N for i in range(N) ]
matrice_Adj[0][0] = True
matrice_Adj[0][3] = True
matrice_Adj[1][1] = True
matrice_Adj[1][3] = True
matrice_Adj[2][2] = True
matrice_Adj[3][0] = True
matrice_Adj[3][1] = True
