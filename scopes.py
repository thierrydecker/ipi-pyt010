#!/usr/bin/python
# -*- coding="utf-8" -*-

# Imports de la biblithèque standard
#

#
# Imports des bibliothèques tierces
#

#
# Internal functions
#

def f(a, l=[]):
    l.append(a)
    return l


def g(a, l=None):
    if l is None:
        l = []
    l.append(a)
    return l


#
# main() function
#
def main():

    for i in range(4):
        l = f("a")
    print(l)

    for i in range(4):
        l = g("a")
    print(l)


if __name__ == '__main__':
    main()
