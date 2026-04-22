#!/usr/bin/env python3

import csv

def read_fasta(fasta_file):
    # make a variable to store the genome sequence
    seq = ''
    with open(fasta_file, "r") as f:
        for line in f:
            if line.startswith(">"):
                continue
            else:
                seq += line.rstrip()
    return seq

def read_gff():
    print("inside read_gff")

def write_output():
    print("inside write_output")


# set the environment for this script
# is it main(), or is this a module being called by something else?
if __name__ == '__main__':
    main()
