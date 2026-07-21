import random
print("Bienvenue au jeu de devinette")
print("choisez un nombre entre 1 et 100")

nombre_choisie = random.randint(1, 100)
essais = 0
trouve = False
while trouve == False:
    votre_choix = int(input("Insère votre choix: "))
    essais = essais + 1
    if votre_choix < nombre_choisie : 
        print("plus grand")
    elif votre_choix > nombre_choisie :
        print("plus petit")
    else :
        print(f"Bravo tu as trouvé en {essais} essais.")
        trouve = True