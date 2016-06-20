# Copyright 2016 Steve Matsumoto

"""
Script docstring goes here.
"""

import argparse
import fileinput

def read_file(filename):
    """
    Read AS relationships file to parse providers and customers.

    Args:
        filename (str): the path to the AS relationships file

    Returns:
        A pair of sets representing the provider and customer ASes,
        respectively.
    """
    prov = set([])
    cust = set([])
    for line in fileinput.input(filename):
        if line[0] == '#':
            continue
        [as1, as2, rel] = map(int, line.strip().split('|'))
        if rel == -1:
            prov.add(as1)
            cust.add(as2)
    return (prov, cust)

def main():
    """
    Print a list of root ASes given an AS relationships file.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='path to AS relationships file')
    args = parser.parse_args()
    (prov, cust) = read_file(args.file)
    for asn in prov - cust:
        print(asn)

if __name__ == '__main__':
    main()
