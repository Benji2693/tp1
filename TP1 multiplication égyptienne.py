# exercice multiplication egyptienne 
def multiplicationEgyptienne(n, p):
    # Renvoie le produit de n par p 
    produit = 0
    while n != 0:
        if n % 2 == 1:  # multiplicateur impair
            produit += p
        n //= 2 # division euclidienne par 2 du multiplicateur
        p *= 2 # multiplication par 2 du multiplicande
    return produit

print("Entrer 2 valeurs à multiplier: ")
a = int(input())
b = int(input())
test = multiplicationEgyptienne(a, b)
print(a," x ",b," = ",test)