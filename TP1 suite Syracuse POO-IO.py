
# exercice syracuse avec POO e tlectrure écriture

class Tp1:
    def __init__(self,name):
        self.name=name

    def ouvertureFichier(f):
        fichier = open(f.name, "r")
        f.valeur = fichier.read()
        fichier.close()

    def syracuse(x):
        x.ouvertureFichier()
        listeSyracuse = []
        while x.valeur != 1:
            if (x.valeur%2==1) :
                x.valeur = x.valeur*3+1
                listeSyracuse.append(x)
            else:
                x.valeur = x.valeur // 2
                listeSyracuse.append(x.valeur)
        print(listeSyracuse)

print("Entrer le fichier contenant la valeur pour appliquer la suite de Syracuse: ")
test = Tp1(str(input()))
test.syracuse()
