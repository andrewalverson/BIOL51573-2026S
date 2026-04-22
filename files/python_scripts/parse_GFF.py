#!/usr/bin/env python3

import argparse
import gff_functions

def main():
    genome_sequence = gff_functions.read_fasta()
    print(genome_sequence)

    gff_functions.read_gff()
    gff_functions.write_output()


# set the environment for this script
# is it main(), or is this a module being called by something else?
if __name__ == '__main__':
    main()
