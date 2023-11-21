def trucresaux(adresse,masque):
    adr_resau = []
    for i in range(4):
        adr_reseau.append(adr[i]&mask[i])
    return adr_reseau

entree = input("nter adrese et masque")
adresse_str, masque_str = entree.split("/")

adresse = [int (v) for v in adresse_str.split(",")]
mask = int(masque_str)
masque_bin = "1"*mask+"0"*(32-mask)
masque = [int(masque_bin[i*8:(i+1)*8],2) for i in range(4)]



print("adresse:"adresse)
print("masque:"masque)
print("adresse reseau:",trucreseau(adresse,masque))
