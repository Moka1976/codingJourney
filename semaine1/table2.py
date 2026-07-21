n = 8
est_premier = True

for d in range(2, n):
 if n % d == 0 :
    est_premier = False
    
print(est_premier)