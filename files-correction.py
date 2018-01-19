#!/usr/bin/python
# -*- coding= utf-8 -*-

# Imports de la biblithèque standard
#

#
# Imports des bibliothèques tierces
#

#
# Internal functions
#


def exercice1(file_src, file_dst):
    # Insere dans un fichier les lignes paires
    fd = open(file_src, 'r')
    file_content = fd.readlines()
    fd.close()
    fd = open(file_dst, 'w')
    file_result = []
    for i in range(0, len(file_content)):
        if (i + 1) % 2 == 0:
            file_result.append(file_content[i])
    fd.writelines(file_result)
    fd.close()


def exercice2(file_src, file_dst_consonnes, file_dst_rest):
    # Un fichier avec les consonnes
    # Un fichier avec les reste
    consonnes = 'zrtypqsdfghjklmwxcvbnZRTPQSDFGHJKLMWXCVBN'
    fd = open(file_src)
    file_content = fd.read()
    fd.close()
    fd_consonnes = ""
    fd_autres = ""
    for letter in file_content:
        if letter == '\n':
            fd_consonnes += letter
            fd_autres += letter
        else:
            if letter in consonnes:
                fd_consonnes += letter
            else:
                fd_autres += letter
    fd = open(file_dst_consonnes, 'w')
    fd.write(fd_consonnes)
    fd.close()
    fd = open(file_dst_rest, 'w')
    fd.write(fd_autres)
    fd.close()


def exercice3(file_src, file_dst):
    # renverser l'ordre des lignes
    fd = open(file_src, 'r')
    file_content = fd.readlines()
    file_content.reverse()
    fd.close()
    fd = open(file_dst, 'w')
    fd.writelines(file_content)
    fd.close()


#
# main() function
#
def main():
    exercice1('hugo.txt', 'dst1.txt')
    exercice2('hugo.txt', 'dst21.txt', 'dst22.txt')
    exercice3('hugo.txt', 'dst3.txt')


if __name__ == '__main__':
    main()
