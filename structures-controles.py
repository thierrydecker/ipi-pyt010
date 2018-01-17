#
# structures de controle
#

#
# Définition d'une variable et assignation
#
a = 1

#
# if ... else ... (si ... sinon ...)
#
if a == 10:
    print("ma variable est égale à 10")
else:
    print("ma variable n'est pas égale à 10")

#
# if ... elif ... (si ... sinon si ...)
#
if a == 10:
    print("ma variable est égale à 10")
elif a == 1:
    print("ma variable n'est pas égale à 10")

#
# Boucles
#

#
# for ...
#
machaine = "ABCDEF"

for caractere in machaine:
    print("machaine ->", caractere)

maliste = ['A', 'B', 'C', 'D']

#
# Sans avoir besoin de l'index
#
for element in maliste:
    print("maliste ->", element)

#
# en ayant besoin de l'index
#
for compteur in range(len(maliste)):
    print(compteur, "maliste ->", maliste[compteur])

#
# Exercice
#
liste_de_personnes = [
    ["Thierry", "Decker", 54],
    ["Martine", "Durand"],
    ["Pierre", "Martin"]
]

#
# Correction
#
for personne in liste_de_personnes:
    for element in personne:
        print(element)

#
# Exercice
#
# Creer un tuple contenant les dix premiers nombres pairs
#
nb = 10
#
# Version 1
#
pairs = []
for i in range(0, nb * 2, 2):
    pairs.append(i)
pairs = tuple(pairs)
print("Le tuple contient ->", pairs)

#
# Version 2
#
print("Le tuple contient ->", tuple([i for i in range(0, 2 * nb, 2)]))
print("Le tuple contient ->", tuple([i * 2 for i in range(0, nb)]))

#
# Exercice
#
# Créer par un boucle la liste suivante
# [ ['A',1], ['B',2], ... , ['Z',26] ]
#
debut, fin = 'A', 'z'
maListe = [[chr(i), ord(chr(i)) - ord(debut) + 1] for i in range(ord(debut), ord(fin) + 1)]
print("maListe de", debut, "à", fin, "->", maListe)
