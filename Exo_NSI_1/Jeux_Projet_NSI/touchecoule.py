from random import randint
import turtle

# Taille du plateau
x_min = -500
x_max = 500
y_min = -400
y_max = 400

# On definit certains paramètres du jeu
nb_essaie_max = 3


# Position aléatoire
position_sous_marin = (randint(x_min, x_max), randint(y_min, y_max))

# On demande la position initiale
position_utilisateur = input("Quel est votre position de départ ? Ecrivez sous la forme \"position_x, position_y\" \n> ")
position_utilisateur = position_utilisateur.split(",")
position_utilisateur = [int(position_utilisateur[0]), int(position_utilisateur[1])]

# Si le joueur est en dehors du plateau, on lui demande de la définir a nouveau
while not (x_min <= position_utilisateur[0] <= x_max and y_min <= position_utilisateur[1] <= y_max):
    position_utilisateur = input("Vous êtes hors des limites !\nQuel est votre position de départ ? Ecrivez sous la forme \"position_x, position_y\" \n> ")
    position_utilisateur = position_utilisateur.split(",")
    position_utilisateur = [int(position_utilisateur[0]), int(position_utilisateur[1])]


turtle.hideturtle()  # Trace un carré qui correspond à la taille du plateau
turtle.speed(10)
turtle.penup()
turtle.goto(x_min, y_min)
turtle.pendown()
turtle.goto(x_max, y_min)
turtle.goto(x_max, y_max)
turtle.goto(x_min, y_max)
turtle.goto(x_min, y_min)

# On crée le sous-marin
sous_marin = turtle.Turtle()
sous_marin.penup()
sous_marin.setposition(*position_sous_marin)
sous_marin.hideturtle()

# On crée l'utilisateur
utilisateur = turtle.Turtle()
utilisateur.penup()
utilisateur.setposition(*position_utilisateur)


def donner_distance(position_sm, position_u):
    """Fonction permettant de renvoyer la distance entre l'utilisateur et le sous-marin"""
    distance = abs(position_sm[0] - position_u[0]) + abs(position_sm[1] - position_u[1])  # On utilise des valeurs absolue avec abs()
    return distance


# On définit certaines variables du jeu
nb_essaie = 0
distance_initiale = donner_distance(position_sous_marin, position_utilisateur)
distance_parcourue = 0
victoire = True  # Variable utilisée pour savoir si l'utilisateur a gagné ou non a la fin

# Boucle principale du jeu
while donner_distance(position_sous_marin, position_utilisateur) > 5:  # Tant que le joueur est a plus de 5 de distance du sous-marin
    print("Vous vous trouvez a", str(donner_distance(position_sous_marin, position_utilisateur)), "cases du sous-marin !")  # On annonce la distance qui nous sépare du sous-marin

    direction = input("Comment souhaitez vous vous orienter ? (0 | 90 | 180 | 270)\n> ")  # On demande la direction
    while direction not in ["0", "90", "180", "270"]:  # Tant que la direction n'est pas correcte, on redemande
        direction = input("Votre direction n'est pas correcte.\nComment souhaitez vous vous orienter ? (0 | 90 | 180 | 270)\n> ")

    utilisateur.setheading(int(direction))  # On définit la direction à l'utilisateur

    distance_avancee = int(input("De combien voulez vous avancer ? (entre 1 et 20)\n> "))  # On demande la distance d'avancée
    while not 1 <= distance_avancee <= 20:  # Tant que la direction est trop grande ou trop petit, on redemande
        distance_avancee = int(input("Votre distance n'est pas correcte.\nDe combien voulez vous avancer ? (entre 1 et 20)\n> "))

    if direction == "0":
        if position_utilisateur[0] + distance_avancee > x_max:  # Si la distance fait sortir l'utilisateur du plateau, on l'ajuste
            distance_avancee = x_max - position_utilisateur[0]
        position_utilisateur[0] += distance_avancee
    elif direction == "90":
        if position_utilisateur[1] + distance_avancee > y_max:
            distance_avancee = y_max - position_utilisateur[1]
        position_utilisateur[1] += distance_avancee
    elif direction == "180":
        if position_utilisateur[0] - distance_avancee < x_min:
            distance_avancee = position_utilisateur[0] - x_min
        position_utilisateur[0] -= distance_avancee
    elif direction == "270":
        if position_utilisateur[1] - distance_avancee < y_min:
            distance_avancee = position_utilisateur[1] - y_min
        position_utilisateur[1] -= distance_avancee

    utilisateur.forward(distance_avancee)  # On fait finalement avancer l'utilisateur
    distance_parcourue += distance_avancee
    nb_essaie += 1
    if nb_essaie >= nb_essaie_max:  # Si le nombre d'essais maximal a été atteins, on sort de la boucle
        victoire = False
        break

if victoire:
    print("Bravo ! Vous avez trouver le sous-marin !")
else:
    print("Oh non ! On dirait que vous avez perdu !")

#  On donne les différentes informations de la partie
print("Vous avez fait", nb_essaie, "essaies, et avez parcouru", distance_parcourue, "cases !")
print("La distance initiale était de", distance_initiale)
sous_marin.showturtle()  # On affiche le sous-marin

input("Appuyez sur entrer pour quitter")  # Permet de ne pas quitter le programme tout seul à la fin
