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

amino_acids = ['VAL', 'ILE', 'LEU', 'GLU', 'GLN', 'ASP', 'ASN', 'HIS', 'TRP', 'PHE', 'TYR' \
'ARG', 'LYS', 'SER', 'THR', 'MET', 'ALA', 'GLY', 'PRO', 'CYS']

# get amino acid

aa_of_interest = input("3 code amino acid:")

if aa_of_interest in amino_acids:
    print("real amino acids")
else:
    print("Not a real 3 code amino acid, use amino acid from: ", amino_acids)
    quit()

line_total = 0

with open(file, "r") as f:
    for line in f:
        if aa_of_interest in line:
            line_total+=1

print("Number of occurances of " + str(aa_of_interest) + ": " + str(line_total))
