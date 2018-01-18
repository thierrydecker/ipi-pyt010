#!/usr/bin/env python
# -*- coding: utf-8 -*-


def decimal_to_cidr(dm):
    if not isinstance(dm, str):
        print("A string is needed")
        return None
    splitted_dm = list(dm.split(sep='.'))
    if len(splitted_dm) != 4:
        print("A decimal mask must have four fields")
        return None
    for i in range(len(splitted_dm)):
        if not splitted_dm[i].isalnum():
            print("Fields must be positive integers")
            return None
        splitted_dm[i] = int(splitted_dm[i])
        if splitted_dm[i] > 255:
            print("Fields must be positive integers less or equal to 255")
            return None
        splitted_dm[i] = format(splitted_dm[i], "0>8b")
    binary_mask = "".join(splitted_dm)
    cidr_mask = binary_mask.count('1')
    if cidr_mask != binary_mask[0:cidr_mask].count('1'):
        print("Invalid mask")
        return None
    return cidr_mask


def main():
    decimal_mask = '255.255.255.128'
    print("Le masque CIDR de {} est {}".format(decimal_mask, decimal_to_cidr(decimal_mask)))


if __name__ == '__main__':
    main()
