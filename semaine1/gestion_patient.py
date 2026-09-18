print("============= GESTIONNAIRE DES PATIENTS ==============")
print("1- Afficher les patients")
print("2- Ajouter un patient")
print("3-Sauvegarder dans un fichier")
print("4- Quitter")


patients = []
patients = [{"nom":"Paul","age":24,"sexe":"M"},
{"nom":"Marie","age":28,"sexe":"F"},
{"nom":"Joe","age":18,"sexe":"M"}
]

def sauvegarder_patients():
    fichier = open("patients.txt", "w")
    for patient in patients:
        fichier.write(patient["nom"] + " - "
        + str(patient["age"])
        + "ans - "
        + patient["sexe"] + 
        "\n"
        )

    fichier.close()

    print("Patients sauvegardés avec succès")

def charger_patients():
    fichier = open("patient.txt", "r")
    for ligne in fichier:
       informations = ligne.strip().split(" - ")

       print(informations)

    fichier.close()

charger_patients()





def afficher_patient():
    for patient in patients:
        print("Nom : ",patient["nom"])
        print("Age : ", patient["age"])
        print("Sexe : ", patient["sexe"])
        print("----------------------")


def ajouter_patient():
    nom = input("inserer le nom du patient svp : ")
    age = int(input("Age du patient: "))
    sexe = input("inserer son sexe : ")

    nouveau_patient = {
        "nom": nom ,
        "age": age ,
        "sexe": sexe
    }
    patients.append(nouveau_patient)

    print("Patient ajouté avec succès !")

choix = 0
while choix != 4:

    choix = int(input("votre choix : "))

    if choix == 1 :
        afficher_patient()
        print("RETOUR DANS LA BOUCLE")
    elif choix == 2 :
        ajouter_patient()
    elif choix == 3 :
        sauvegarder_patients()
    elif choix == 4 :
        print("A Bientôt")   
    else :
        print("Choix invalide")

