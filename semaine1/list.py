patients = ["Paul", "Marie", "Joe", "Yazid", "Karim"]

def ajouter_patient():
    votre_nom = input("inserez votre nom ici: ")
    patients.append(votre_nom)
    print("patient ajouté !")
   
ajouter_patient()


def afficher_patient():
    for patient in patients:
        print(patient)

afficher_patient()
