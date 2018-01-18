def somme(*nombres):
    """Retourne la somme des nombre de la liste donnée
    """
    total = 0
    for nombre in nombres:
        total += nombre
    return total

nombres = [1,2,3,4]

print(somme(*nombres))
