base = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400

nbConvives = int(input("Entrez le nombre de personne(s) conviées à la fondue :"))

fromage = (fromage*nbConvives)/base
eau = (eau*nbConvives)/base
ail= (ail*nbConvives)/base
pain= (pain*nbConvives)/base

print("Pour faire une fondue fribourgeoise pour",nbConvives," personnes, il vous faut :")
print("-",fromage,"g de fromage")
print("-",eau,"dl eau")
print("-",ail,"gousses d'ail")
print("-",pain,"gr de pain")





