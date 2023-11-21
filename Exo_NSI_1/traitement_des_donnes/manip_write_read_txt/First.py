# script : programme_test .py
nom_du_fichier = " test .txt"
# cré ation et ouverture du fichier test .txt en mode write ’w’ (é criture )
obj_fichier = open ( nom_du_fichier ,"w")
# é criture dans le fichier avec la mé thode write ()
obj_fichier . write ('JE MAPPELLE PIERE LE ¨PAGBO')
obj_fichier . write ('AEAEFRGRGRGRRGGRRG./n') # ’\n’ : saut de ligne
obj_fichier . close () # fermeture du fichier avec la mé thode close ()
