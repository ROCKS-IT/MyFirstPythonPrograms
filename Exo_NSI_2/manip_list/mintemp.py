def mini(t_moy, annees):
    tmini = t_moy[0]
    cpt2 = 0
    for i in range(len(t_moy)):
        if t_moy[i] < tmini:
            tmini = t_moy[i]
            cpt2 = annees[i]
    return tmini,cpt2
        
t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]
