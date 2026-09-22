import json 
from datetime import datetime

produits = [
    {
        "nom":"Cahiers",
        "prix_achat": 500,
        "prix_vente": 750,
        "quantite": 30
    },
    {
        "nom":"Stylo",
        "prix_achat": 200,
        "prix_vente": 300,
        "quantite": 50
    }
]

ventes = []

def afficher_produits():
    print("\n============ STOCK ============")

    numero = 1

    for produit in produits:
        print(numero, "-",produit["nom"],
        "| Prix :", produit["prix_vente"],
        "FCFA | Stock :", produit["quantite"])

        numero += 1

def demander_entier(message):
    while True:
        try:
            valeur = int(input(message))
            if valeur <= 0:
                print("Ⅹ La valeur doit être supérieur à 0.")
            else:
                return valeur

        except ValueError:
            print("♦Ⅹ♦ Veuillez entrer un nombre valide. ")

def demander_choix(message):
    while True:
        try:
            choix = int(input(message))
            if choix < 0 and choix != int():
                print("Ⅹ Le choix ne correspond pas, veuillez réesseyer")
            else:
                return choix

        except ValueError:
            print("Ⅹ Veuillez entrer un nombre valide.")


def vendre_produit(produit):

    print("Une vente est en cours...")

    quantite_vendue = demander_entier(f"Combien de {produit['nom']} ont été vendus ?")
    
    if quantite_vendue <= 0:
        print("La quantité doit être superieur à 0.")

    elif quantite_vendue <= produit["quantite"]:
        produit["quantite"] -= quantite_vendue

        montant = produit["prix_vente"] * quantite_vendue
        benefice = (produit["prix_vente"] - produit["prix_achat"]) * quantite_vendue
        
        date_vente = datetime.now()

        vente = {
            "produit": produit["nom"],
            "quantite": quantite_vendue,
            "total": montant,
            "benefice": benefice,
            "date": date_vente
        }
        ventes.append(vente)

        print("Vente enregitrée !")
        print("Produit :", produit["nom"])
        print("Quantité vendue :", quantite_vendue)
        print("montant :", montant, "FCFA")
        print("Stock restant :", produit["quantite"])

    else:
        print("Stock insuffisant !")

def afficher_historique():
    print("\n========== HISTORIQUE DES VENTES ==========")

    if len(ventes) == 0:
        print("Aucune vente enrégistrée.")
        return

    total_general = 0
    total_benefice = 0 
    numero = 1

    for vente in ventes:
        date_formatee = vente["date"].strftime("%d/%m/%Y à %H:%M")

        print(numero, "-", vente["produit"], "| Quantité :",
        vente["quantite"], "| Total :", vente["total"], "FCFA", "| Bénéfice:", vente["benefice"], "FCFA")
        print("  Date :", date_formatee)

        total_general += vente["total"]
        total_benefice += vente["benefice"]
        numero += 1


    print("--------------------")
    print("Total des ventes :", total_general, "FCFA")
    print("Bénéfice total :", total_benefice, "FCFA")

def choisir_produit():

    afficher_produits()

    choix = demander_entier("Quel produit voulez-vous choisir ?")

    if choix >= 1 and choix <= len(produits):
        return produits[choix - 1]

    else:
        print("Choix invalide !")
        return None 

def ajouter_produit():
    print("--- AJOUETR UN PRODUIT ---")

    nom = input("Nom du produit : ")

    for produit in produits:
        if produit["nom"].lower() == nom.lower():
            quantite = int(input("Quantité à ajouter : "))
            produit["quantite"] += quantite

            print(f"{quantite} unité(s) ajoutée(s) au stock de {produit['nom']}.")
            print(f"Nouveau stock : {produit['quantite']}")
            return 

    prix_achat = int(input("Prix d'achat : "))
    prix_vente = int(input("Prix de vente : "))
    quantite = int(input("Quantité en stock : "))

    nouveau_produit = {
        "nom": nom,
        "prix_achat": prix_achat,
        "prix_vente": prix_vente,
        "quantite": quantite
        }

    produits.append(nouveau_produit)
    print("Produit ajouté avec succès !")

def reapprovisionner_produit():
    print("\n--- REAPPROVISIONNEMENT ---")

    numero = 1

    for produit in produits:
        print(numero, "-", produit["nom"])
        numero += 1

    choix = demander_entier("Quel produit voulez-vous réapprovitionner ? ")

    if choix >= 1 and choix <= len(produits):
        produit = produits[choix - 1]

        quantite = demander_entier("Quantité à ajouter : ")

        ancien_stock = produit["quantite"]

        produit["quantite"] += quantite

        print(f"Ancien stock : {ancien_stock}")
        print(f"Nouveau stock : {produit['quantite']}")
        print("Stock mis à jour avec succès !")

    else:
        print("Choix invalide !")

def rechercher_produit():
    print("\n========== RECHERCHE PRODUIT ==========")

    recherche = input("Nom du produit à rechercher : ").lower()

    trouve = False 

    for produit in produits:
        if recherche in produit["nom"].lower():
            print("\nProduit trouvé :")
            print("Nom :", produit["nom"])
            print("Prix d'achat :", produit["prix_achat"], "FCFA")
            print("Prix de vente :", produit["prix_vente"], "FCFA")
            print("Stock :", produit["quantite"])

            trouve = True

    
    if trouve ==False:
            print("♦ Aucun produit trouvé.")


def afficher_tableau_de_bord():
    print("\n========== TABLEAU DE BORD ==========")

    nombre_produits = len(produits)

    stock_total = 0

    for produit in produits:
        stock_total += produit["quantite"]

        nombre_ventes = len(ventes)

        chiffre_affaires = 0
        benefice_total = 0

    for  vente in ventes:
        chiffre_affaires += vente["total"]
        benefice_total += vente["benefice"]

        print("📎 Produits différents :", nombre_produits)
        print("📎 Quantité total en stock :", stock_total)
        print("📎 Nombre de ventes :", nombre_ventes)
        print("📎 Chiffre d'affaires : ", chiffre_affaires, "FCFA")
        print("📎 Bénéfice total :", benefice_total)

        print("====================")

def sauvegarde_donnees():
    donnees = {
        "produits": produits,
        "ventes": []
    }

    for vente in ventes:
        vente_copie = vente.copy()
        vente_copie["date"] = vente["date"].isoformat()

    donnees["ventes"].append(vente_copie)
    

    with open("stockpro_data.json", "w",
    encoding="utf-8") as fichier:
        json.dump(donnees, fichier, ensure_ascii=False, indent=4)
        print("⏺ Données sauvegardées avec succès !")

while True:
    print("============ STOCKPRO ============")
    print("1 - Voir les produits")
    print("2 - Vendre un produit")
    print("3 - Ajouter un produit")
    print("4 - Réapprovisionner un produit")
    print("5 - Historique des vente")
    print("6 - Tableau de bord")
    print("7 - Rechercher un produit")
    print("0 - Quitter")

    choix = demander_choix("Votre choix : ")
    if choix == 1:
        afficher_produits()

    elif choix == 2:
        produit_choisi = choisir_produit()

        if produit_choisi is not None:

            vendre_produit(produit_choisi)

    elif choix == 3:
        ajouter_produit()

    elif choix == 4:
        reapprovisionner_produit()

    elif choix == 5:
        afficher_historique()

    elif choix == 6:
        afficher_tableau_de_bord()

    elif choix == 7:
        rechercher_produit()
    
    elif choix == 0:
        print("Merci d'avoir utilisé StockPro !")
        break

    else:
        print("Choix invalide !")


sauvegarde_donnees()