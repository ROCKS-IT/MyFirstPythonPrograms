#bibliothèque vecteur 2d
#crée un vecteur
def cree_vect(x,y):
    return (x,y)
#affiche sur la console les coordonné du vecteurs u
def affiche_vect(u):
    print("(",u[0],";",u[1],")")

#renvoie le x du vecteur
def x_vect(u):
    return u[0]
#renvoie le y du vecteur
def y_vect(u):
    return u[1]
#renvoie True si les vecteurs u et v sont égaux
#et renvoie False sinon
def est_egal_vect(u,v):
    return u[0] == v[0] and u[1] == v[1]
#retourne le vecteur somme u+v
def somme_vect(u,v):
    return (u[0]+v[0],u[1]+v[1])
#retourne le vecteur difference u-v
def difference_vect(u,v):
    return (u[0]-v[0],u[1]-v[1])
#retourne le vecteur ku
def k_vect(k,u):
    return (u[0]*k,u[1]*k)
#renvoie True si les vecteurs u et v sont colineaires
#et False sinon
def est_colin_vect(u,v):
    return(u[0]*v[1] == u[1]*v[0])

#renvoie le produit scalaire des vecteurs u et v
def prod_scal(u,v):
    return

