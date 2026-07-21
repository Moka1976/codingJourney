def est_premier(n):
    if n < 2:
        return False
    est_premier_resultat = True
    for d in range(2, n):
            if n % d == 0:
                est_premier_resultat = False
    return est_premier_resultat

for nombre in range(1, 51):
    if est_premier(nombre):
        print(nombre)