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

#
# main() function
#

#
# Open a file
#


def file_open(file_name, rights):
    # Rights : 'r' -> read
    #          'w' -> write
    #          'a' -> append
    file_descriptor = open(file_name, rights)
    return file_descriptor


#
# Close a file
#


def file_close(file_descriptor):
    file_descriptor.close()


#
# Read a file in one big string
#


def file_read(file_descritor):
    file = file_descritor.read()
    return file


#
# Read a file in one big list (each line in an element of the list
#


def file_read_lines(file_descritor):
    file_list = file_descritor.readlines()
    return file_list


#
# Read a file in one string per line at a time
#


def file_read_next_line(file_descritor):
    line = file_descritor.readline()
    return line


#
# Write a string into a file
#


def write_file_line(file_descriptor, text):
    file_descriptor.write(text)


#
# Write a list of strings into a file
#


def write_file_lines(file_descritor, text):
    file_descritor.writelines(text)


#
# Main function
#


def main():
    file_name = 'test.txt'
    rights = 'w'
    file_descriptor = file_open(file_name, rights)

    text = 'abc\n'
    write_file_line(file_descriptor, text)
    text = 'def\n'
    write_file_line(file_descriptor, text)

    text = [
        'This is an exemple 1\n',
        'This is an exemple 2\n',
        'This is an exemple 3\n',
    ]
    write_file_lines(file_descriptor, text)

    file_close(file_descriptor)

    file_name = 'test.txt'
    rights = 'r'
    file_descriptor = file_open(file_name, rights)

    text = file_read(file_descriptor)
    print(text)

    file_close(file_descriptor)

    file_name = 'test.txt'
    rights = 'r'
    file_descriptor = file_open(file_name, rights)

    text = file_read_lines(file_descriptor)
    print(text)

    file_close(file_descriptor)

    file_name = 'test.txt'
    rights = 'r'
    file_descriptor = file_open(file_name, rights)

    text, line_number = None, 1
    while text != "":
        text = file_read_next_line(file_descriptor)
        print(line_number, " -> ", text, end="")
        line_number += 1

    file_close(file_descriptor)


if __name__ == '__main__':
    main()
