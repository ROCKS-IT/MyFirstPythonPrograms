minutes = int(input("nombre de minutes:"))
heure = 0
jour = 0
while  minutes >= 60:
    if minutes >=  60:
        heure += 1
        minutes = minutes - 60
    if heure >= 24:
        heure = heure - 24
        jour = jour + 1
print(jour,heure,minutes)
    
    

