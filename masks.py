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

def decimal_to_cidr(decimal_mask):
    """Calcul du masque CIDR à partir du masque décimal
    inputs:
        - Masque décimal
    outputs:
        - Masque CIDR
    """
    cidr_mask = None

    # Tests de validité du masque décimal
    if not isinstance(decimal_mask, str):
        print("A string is needed")
        return

    splitted_dm = list(decimal_mask.split(sep='.'))

    if len(splitted_dm) != 4:
        print("A decimal mask must have four fields")
        return

    for part in splitted_dm:
        if not part.isalnum():
            print("Fields must be positive integers")
            return

    for i in range(len(splitted_dm)):
        splitted_dm[i] = int(splitted_dm[i])
        if splitted_dm[i] > 255:
            print("Fields must be positive integers less or equal to 255")
            return

    for i in range(len(splitted_dm)):
        splitted_dm[i] = bin(splitted_dm[i])

    binary_mask = ''
    for i in range(len(splitted_dm)):
        binary_mask += splitted_dm[i][2:].zfill(8)

    number_of_ones = binary_mask.count('1')

    if number_of_ones != binary_mask[0:number_of_ones].count('1'):
        print("Invalid mask")
        return None
    return number_of_ones








decimal_mask = '255.0.0.0'
print("Le masque CIDR de {} est {}".format(decimal_mask, decimal_to_cidr(decimal_mask)))
