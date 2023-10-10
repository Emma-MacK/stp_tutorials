# Script to handle python exercise 3

import os

# adapt the script so the user can specify an input file, and a 3 letter amino acid code, only count the lines with that amino acid code
# Handle incorrect file names and amino acid codes

# get file
file = input('File of interest:')

# check file exists

if os.path.exists(file):
    print("File exists")
else:
    print("File does not exist, check file path")
    quit()

# amino acid codes

amino_acids = {'VAL':0, 'ILE':0, 'LEU':0, 'GLU':0, 'GLN':0, 'ASP':0, 'ASN':0, 'HIS':0, 'TRP':0, 'PHE':0, 'TYR':0, 'ARG':0, 'LYS':0, 'SER':0, 'THR':0, 'MET':0, 'ALA':0, 'GLY':0, 'PRO':0, 'CYS':0}

# get amino acid


with open(file, "r") as f:
    for line in f:
        # get 3 code amino acid
        # add 1 to the value in the dict
        line_list = line.split()
        # get 3rd element, which is where the aa is held
        aa_code = line_list[3]
        amino_acids[aa_code] += 1

for key in amino_acids.keys():
    print(amino_acids[key], "occurances of", key )
