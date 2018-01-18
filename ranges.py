import random

#
# Exercices sur les ranges
#

#
# Afficher le compte à rebours d'un entier à un autre
#
# Correction
#


debut, fin = 20, 0
for i in range(debut, fin - 1, -1):
    print("De {} à {} --> {}".format(debut, fin, i))

#
# Créer une liste d'entiers et la trier en ordre décroissant
#


debut, fin = 10, 20
maListe = [i for i in range(debut, fin + 1)]
maListe.reverse()
print("maListe -> {}".format(maListe))

#
# Créer une liste de n entiers aléatoires (compris entre <debut> et <fin>) et la trier en
# ordre croissant. L'afficher avant et après le tri
#
nb, debut, fin = 10, 0, 10001
maListe = [random.randrange(debut, fin) for i in range(nb + 1)]
print("maListe avant tri -> {}".format(maListe))
maListe.sort()
print("maListe après tri -> {}".format(maListe))
