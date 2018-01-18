def additionner_deux_nombres(premier_nombre, second_nombre):
    """
    Additionne deux nombres

    inputs:
        Deux nombres
    outputs:
        Un nombre
    """
    total = premier_nombre + second_nombre
    return total


a, b = "1", 10
print("la somme de {} et {} est {}".format(a, b, additionner_deux_nombres(a, b)))
