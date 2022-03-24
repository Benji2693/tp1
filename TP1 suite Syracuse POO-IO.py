
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
        val = int(x.valeur)
        listeSyracuse = []
        while val != 1:
            if (val%2==1) :
                val = val*3+1
                listeSyracuse.append(val)
            else:
                val = val // 2
                listeSyracuse.append(val)
        print(listeSyracuse)

print("Entrer le fichier contenant la valeur pour appliquer la suite de Syracuse: ")
test = Tp1(str(input()))
test.syracuse()
