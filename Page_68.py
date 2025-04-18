import turtle  # On importe la bibliothèque Turtle pour dessiner le jeu
import time    # On importe time pour ralentir le jeu et donner un rythme
import random  # On importe random pour placer la nourriture aléatoirement

# Créer la fenêtre du jeu
fenetre = turtle.Screen()
fenetre.title("Jeu Snake")  # On donne un titre à la fenêtre
fenetre.bgcolor("black")  # La couleur de fond est noire
fenetre.setup(width=600, height=600)  # La fenêtre mesure 600x600 pixels
fenetre.tracer(0)  # Désactive le rafraîchissement automatique pour rendre le jeu plus fluide

# Créer le serpent
serpent = turtle.Turtle()  # On crée une tortue pour représenter le serpent
serpent.shape("square")  # Le serpent aura une forme carrée
serpent.color("green")  # Le serpent sera vert
serpent.penup()  # Le serpent ne laisse pas de trace derrière lui
serpent.goto(0, 0)  # Le serpent commence au centre de l'écran
serpent.direction = "stop"  # Le serpent est immobile au début

# Créer la nourriture
nourriture = turtle.Turtle()
nourriture.speed(0)  # On fixe la vitesse de la nourriture à la plus rapide (elle ne bouge pas)
nourriture.shape("circle")  # La nourriture aura une forme circulaire
nourriture.color("red")  # La nourriture sera rouge
nourriture.penup()  # La nourriture ne laisse pas de trace
nourriture.goto(0, 100)  # La nourriture apparaît en haut du serpent
