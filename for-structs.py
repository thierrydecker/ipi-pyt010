#
# structures de controle
#

#
# Boucles for
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
    ["Thierry", "Decker", 52],
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
# Version 2 (Comprehension list)
#
print("Le tuple contient ->", tuple([i for i in range(0, 2 * nb, 2)]))
print("Le tuple contient ->", tuple([i * 2 for i in range(0, nb)]))

#
# Exercice
#
# Créer par un boucle la liste suivante
# [ ['A',1], ['B',2], ... , ['Z',26] ]
#

#
# Correction
#

# Définition des bornes
debut, fin = ord('A'), ord('z')
# Création de la liste en compréhension
maListe = [[chr(i), ord(chr(i)) - debut + 1] for i in range(debut, fin + 1)]
# Affichage
print("maListe de", chr(debut), "à", chr(fin), "->", maListe)
