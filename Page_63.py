# Fonction pour faire une addition
def addition(a, b):
    return a + b  # On retourne le résultat de l'addition

# Fonction pour faire une soustraction
def soustraction(a, b):
    return a - b  # On retourne le résultat de la soustraction

# Fonction pour faire une multiplication
def multiplication(a, b):
    return a * b  # On retourne le résultat de la multiplication

# Fonction pour faire une division
def division(a, b):
    if b != 0:  # On vérifie que le second nombre n'est pas zéro (on ne peut pas diviser par zéro)
        return a / b  # Si b n'est pas zéro, on retourne le résultat de la division
    else:
        return "Erreur : Division par zéro !"  # Si b est zéro, on affiche une erreur

# On affiche un message pour accueillir l'utilisateur
print("Bienvenue dans la calculatrice simple !")

# On demande à l'utilisateur de choisir une opération
operation = input("Choisis une opération (addition, soustraction, multiplication, division) : ")

# On demande à l'utilisateur d'entrer deux nombres
nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))

# On vérifie quelle opération a été choisie et on appelle la fonction correspondante
if operation == "addition":
    print("Résultat :", addition(nombre1, nombre2))
elif operation == "soustraction":
    print("Résultat :", soustraction(nombre1, nombre2))
elif operation == "multiplication":
    print("Résultat :", multiplication(nombre1, nombre2))
elif operation == "division":
    print("Résultat :", division(nombre1, nombre2))
else:
    print("Opération non reconnue.")  # Si l'utilisateur entre une opération qui n'existe pas
