def carre(nombre):
    return nombre * nombre
    print(carre(6))
    carre()

def presentation(nom, age):
    print(f"Je suis {nom} et j'ai {age} ans ")
presentation("Theon Greggoy", 24)

def calculer_somme(t, g):
    print(f"la somme de {t} + {g} est {t + g} ")

calculer_somme(12, 8)

def est_majeur(age):
    if age < 18 :
        return False
    elif age >= 18 :
        return True
est_majeur(18)
if est_majeur(24):
    print("vous etes majeur")
else: 
    print("vous etes mineur")


    