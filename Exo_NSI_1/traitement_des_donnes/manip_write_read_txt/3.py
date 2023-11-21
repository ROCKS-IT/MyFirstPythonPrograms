nom_du_fichier = "test.txt"
# cré ation et ouverture du fichier test .txt en mode write ’w’ (é criture )
obj_fichier = open ( nom_du_fichier ,'w')
# é criture dans le fichier avec la mé thode write ()
obj_fichier . write ('Une premi ère ligne ... ')
obj_fichier . write ('toujours la premi ère ligne .\n') # ’\n’ : saut de ligne
obj_fichier . close () # fermeture du fichier avec la mé thode close ()

obj = open ('test .txt ','a') # ouverture du fichier test .txt en mode append ( ajout )
obj . write ('Une deuxi ème ligne .\n') # é criture dans le fichier avec la mé thode write ()
obj . write ('abcd \ tefgh \n') # ’\t’ tabulation
nombre = 3.14
obj . write ( str ( nombre ) ) # str () transforme un nombre en chaîne
obj . close ()

with open("test.txt",'r') as obj:
    for ligne in obj:
        print(ligne/strip())
