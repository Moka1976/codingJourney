print("entrez votre age")
votre_age = int (input("quel est ton age ?"))
if votre_age > 18:
    print("bravo vous etes maintenat majeur") 
elif votre_age <= 18:
    print("désole vous etes encore mineur")
age_estimé = 180 - votre_age
print(f"vous aurez {age_estimé} dans 180 ans")