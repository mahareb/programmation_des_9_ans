# Fonctions pour contrôler le serpent
def aller_haut():
    if serpent.direction != "bas":  # Le serpent ne peut pas aller en haut s'il va en bas
        serpent.direction = "haut"

def aller_bas():
    if serpent.direction != "haut":  # Le serpent ne peut pas aller en bas s'il va en haut
        serpent.direction = "bas"

def aller_gauche():
    if serpent.direction != "droite":  # Le serpent ne peut pas aller à gauche s'il va à droite
        serpent.direction = "gauche"

def aller_droite():
    if serpent.direction != "gauche":  # Le serpent ne peut pas aller à droite s'il va à gauche
        serpent.direction = "droite"

# Fonction pour faire bouger le serpent
def mouvement():
    if serpent.direction == "haut":
        y = serpent.ycor()  # On prend la position actuelle en Y
        serpent.sety(y + 20)  # On bouge le serpent de 20 unités vers le haut

    if serpent.direction == "bas":
        y = serpent.ycor()  # On prend la position actuelle en Y
        serpent.sety(y - 20)  # On bouge le serpent de 20 unités vers le bas

    if serpent.direction == "gauche":
        x = serpent.xcor()  # On prend la position actuelle en X
        serpent.setx(x - 20)  # On bouge le serpent de 20 unités vers la gauche

    if serpent.direction == "droite":
        x = serpent.xcor()  # On prend la position actuelle en X
        serpent.setx(x + 20)  # On bouge le serpent de 20 unités vers la droite

# Écouter les touches du clavier pour contrôler le serpent
fenetre.listen()
fenetre.onkey(aller_haut, "Up")      # Si on appuie sur la flèche "Up", le serpent va en haut
fenetre.onkey(aller_bas, "Down")     # Si on appuie sur "Down", le serpent va en bas
fenetre.onkey(aller_gauche, "Left")  # Si on appuie sur "Left", il va à gauche
fenetre.onkey(aller_droite, "Right") # Si on appuie sur "Right", il va à droite

# Boucle principale du jeu
while True:
    fenetre.update()       # On met à jour l'écran
    mouvement()            # On appelle la fonction pour bouger le serpent

    # Pause pour ralentir le jeu et le rendre jouable
    time.sleep(0.1)
