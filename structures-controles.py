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
