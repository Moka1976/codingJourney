import random 
rejouer = "oui"
while rejouer =="oui":
    nombre_choisie = random.randint(1, 20)
    essaie = 0
    trouve = False

    print("Bienvenue a notre jeu de devinette")
    print("choisisez un nombre entre 1 et 20")

    while trouve == False and essaie > 7 :
        votre_choix = int (input("saisir votre choix ici : "))
        essaie = essaie + 1

        if votre_choix < nombre_choisie : 
            print("plus grand")
        elif votre_choix > nombre_choisie :
                print("plus petit")
    else: 
        print(f"Bravo tu as trouver en {essaie} essaie")

        if trouve == False:
            print(f"Oops, le nombre était {nombre_choisie}")

            rejouer = input("Veux-tu réjouer ? (oui/non)")