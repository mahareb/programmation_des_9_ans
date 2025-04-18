import random  # On importe la bibliothèque random pour choisir un nombre au hasard

nombre_secret = random.randint(1, 100)  # Choisir un nombre secret entre 1 et 100
tentative = 0  # On commence à zéro tentative
trouve = False  # Variable pour savoir si le nombre a été trouvé ou non

print("Je pense à un nombre entre 1 et 100. Essaie de deviner !")

while not trouve:  # Boucle qui continue tant que le nombre n'est pas trouvé
    devine = int(input("Devine le nombre : "))  # Demander à l'utilisateur de deviner
    tentative += 1  # Compter le nombre de tentatives
    if devine == nombre_secret:  # Si le nombre deviné est correct
        print(f"Bravo ! Tu as trouvé en {tentative} tentatives.")
        trouve = True  # Le nombre a été trouvé, on arrête la boucle
    elif devine < nombre_secret:  # Si le nombre est trop petit
        print("C'est plus grand.")
    else:  # Si le nombre est trop grand
        print("C'est plus petit.")
