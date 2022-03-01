
# exercice syracuse

def syracuse(x):
    listeSyracuse = []
    while x != 1:
        if (x%2==1) :
            x = x*3+1
            listeSyracuse.append(x)
        else:
            x = x // 2
            listeSyracuse.append(x)
    print(listeSyracuse)

print("Entrer 1 valeur pour appliquer la suite de Syracuse: ")
syracuse(int(input()))

