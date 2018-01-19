#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Standard imports
#
import argparse
import codecs
import os


#
# Third party imports
#

#
# Project imports
#

#
# Functions
#

def write_to_file(options, content):
    """

    Args:
        options: Dictionary of the options
        content: Text to be writen to file

    Returns:
        None

    """
    if os.path.exists(options['destination_file']):
        answer = input(
                '{} already exists. Do you want to override it (yes to confirm)? '.format(options['destination_file']))
        if answer != 'yes':
            return
    with open(options['destination_file'], mode='w', encoding=options['encoding']) as fd:
        fd.write(content)


def exists_encoding(encoding):
    """

    Args:
        encoding: The chosen encoding

    Returns:
        - True if codec exists
        - False if codec does not exist

    """
    try:
        codecs.lookup(encoding)
    except LookupError:
        return False
    return True


def load_content(options):
    """

    Args:
        options: Dictionary of the options

    Returns:
        content:
            - The string given in source string or
            - The content of the loaded file or
            - None if the given source file is not found

    """
    content = None

    if options['source_file'] is not None:
        if os.path.exists(options['source_file']):
            with open(options['source_file'], mode='r', encoding=options['encoding']) as fd:
                content = fd.read()
    else:
        content = options['source_string']

    return content


def encode(options):
    """
    Encode function

    Args:
        options: Dictionary of the options

    Returns:
        None

    """
    text_to_encode = load_content(options)

    if text_to_encode is None:
        print('Source file <{}> not found'.format(options['source_file']))
        encoded_text = None
    else:
        encoded_text = ''
        for symbol in text_to_encode:
            #
            # In chr(value), value must be in range(0,1114111)
            # 1.114.112 is the length of unicode table
            #
            encoded_symbol = chr((ord(symbol) + options['offset']) % 1114112)
            encoded_text += encoded_symbol

    if options['destination_file'] is not None:
        write_to_file(options, encoded_text)
    else:
        print('Encoded text:\n\n{}\n'.format(encoded_text))


def decode(options):
    """
    Decode function

    Args:
        options: Dictionary of the options

    Returns:
        None

    """
    text_to_decode = load_content(options)

    if text_to_decode is None:
        print('Source file <{}> not found'.format(options['source_file']))
        decoded_text = None
    else:
        decoded_text = ''
        for symbol in text_to_decode:
            #
            # In chr(value), value must be in range(0,1114111)
            # 1.114.112 is the length of unicode table
            #
            decoded_symbol = chr((ord(symbol) - options['offset']) % 1114112)
            decoded_text += decoded_symbol

    if options['destination_file'] is not None:
        write_to_file(options, decoded_text)
    else:
        print('Decoded text:\n\n{}\n'.format(decoded_text))


def caesar(options):
    """
    Switch function

    Args:
        options: Dictionary of the options

    Returns:
        None

    """
    if options['encode']:
        encode(options)
    else:
        decode(options)


def main():
    """
    Main function

    Returns:
        None

    """

    #
    # Create the parser
    #
    parser = argparse.ArgumentParser(description='Caesar\'s algorithm encoder/decoder')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-e', '--encode', action='store_true', help='Encode the source to the destination')
    group.add_argument('-d', '--decode', action='store_true', help='Decode the source to the destination')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-sf', '--source-file', help='Source file to encode/decode')
    group.add_argument('-ss', '--source-string', help='String to encode/decode')

    parser.add_argument('-df', '--destination-file', help='Destination file encoded/decoded')
    parser.add_argument('-o', '--offset', type=int, help='Offset to be used', required=True)
    parser.add_argument('-en', '--encoding', help='Codec', default='utf-8')

    arguments = parser.parse_args()

    options = {
        'decode'          : arguments.decode,
        'encode'          : arguments.encode,
        'source_file'     : arguments.source_file,
        'source_string'   : arguments.source_string,
        'destination_file': arguments.destination_file,
        'offset'          : arguments.offset,
        'encoding'        : arguments.encoding
    }

    if not exists_encoding(options['encoding']):
        #
        # Codec not supported
        #
        print('Codec {} is not supported'.format(options['encoding']))
        return

    if options['offset'] <= 0:
        #
        # Offset has to be strictly positive
        # If not, fallback to Caesar default offset
        #
        options['offset'] = 3
        print('Offset changed to {}'.format(options['offset']))

    caesar(options)


if __name__ == '__main__':
    #
    # Automatic execution of main()
    #
    main()
