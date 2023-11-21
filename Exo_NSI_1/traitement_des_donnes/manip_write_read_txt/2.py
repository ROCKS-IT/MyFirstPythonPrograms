

with open('mots_francais.txt','r',encoding='utf-8') as f :
    liste = []
    for i in range(10):
        chaine = f.readline().strip()
        liste.append(chaine)

print (liste)

with open('mots_francais.txt','r',encoding='utf-8') as f:
    while True :
        chaine = f.readline().strip()
        if chaine[0] == 'g' :
            print(chaine)
            break

with open('mots_francais.txt','r',encoding='utf-8') as f:
    n = 0
    while True :
        chaine = f.readline().strip()
        if chaine == '' :
            print(n)
            break
        n+=1

with open('mots_francais.txt','r',encoding='utf-8') as f:
    vmax, motmax = à, ""
    while True :
        mot = f.readline().strip()
        if len(mot) > vmax:
            vmax = len(mot)
            motmax = mot
    
    
    
        
        
