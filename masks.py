#!/usr/bin/python
# -*- coding:"utf-8" -*-

#
# Exercice sur les fonctions
#
# Initialiser une variable chaine de caractères contenant un masque réseau
# en notation décimale (aaa.bbb.ccc.ddd).
#
# Ecrire une ou plusieures fonctions permettant de convertir le masque décimal
# dans son équivalent CIDR
#
# Exemple : 255.255.255.0   doit donner /24
#           255.255.0.0     doit donner /16
#           255.255.255.252 doit donner /30
#
# Si le masque donné en notation décimale est invalide, retourner None.
#
# Vous n'etes pas autorisés à utiliser l'instruction import.
#


def decimal_to_cidr(dm):
    """Calcul du masque CIDR à partir du masque décimal
    inputs:
        - Masque décimal
    outputs:
        - Masque CIDR
    """

    # Did we get a string ?
    if not isinstance(dm, str):
        print("A string is needed")
        return None

    # Split the string into a list
    splitted_dm = list(dm.split(sep='.'))

    # Did we get four fields ?
    if len(splitted_dm) != 4:
        print("A decimal mask must have four fields")
        return None

    # Iterate over the mask's fields
    for i in range(len(splitted_dm)):

        # Did we get a numeric field ?
        if not splitted_dm[i].isalnum():
            print("Fields must be positive integers")
            return None

        # Convert the string into int
        splitted_dm[i] = int(splitted_dm[i])

        # Did we get an int > 255
        if splitted_dm[i] > 255:
            print("Fields must be positive integers less or equal to 255")
            return None

        # Format the field into its binary representation
        splitted_dm[i] = format(splitted_dm[i], "0>8b")

    # Build a string with the four fields concatenated
    binary_mask = "".join(splitted_dm)

    # Number of ones in the binary mask ?
    cidr_mask = binary_mask.count('1')

    # Is it a valid mask ?
    if cidr_mask != binary_mask[0:cidr_mask].count('1'):
        print("Invalid mask")
        return None
    return cidr_mask


def main():
    decimal_mask = '255.255.255.128'
    print("Le masque CIDR de {} est {}".format(decimal_mask, decimal_to_cidr(decimal_mask)))


if __name__ == '__main__':
    main()
