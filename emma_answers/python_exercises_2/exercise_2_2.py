# Write a function to translate a DNA sequence into an amino acid sequence (don’t use imported modules to do this for now).

# make a dictionary to has codons and their matching amino acids

codon_bases_dict = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T','AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K','AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R','CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P','CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R','GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V','GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A','GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E','GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G','TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S','TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L','TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_','TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
## codon_bases_dict["ATA"]


### create a function that takes a sequence and checks that bases are legal. 
### If a base is not ATC or G then replace with N. this will also handle white spaces

def correct_bases(seq):
    corrected_seq = ""
    for i in seq:
        bases = ["A", "T", "C", "G", "a", "t", "c", "G"]
        if i in bases:
            corrected_seq = corrected_seq + i
        else:
            corrected_seq = corrected_seq + "N"
    return corrected_seq
    
## get a sequence, split it into codons, replace with amino acid code 

def seq_translate(seq):
    seq = seq.upper()
    seq = correct_bases(seq)
    translation = ""
    for i in range(0, len(seq), 3):
        codon=seq[i:i+3]
        if codon in codon_bases_dict:
            translation=translation+codon_bases_dict[codon]
        else:
            translation=translation+"X"
    return translation

sequence = "ATGGATTTATCTGCTCTTCGCGHTGAAGAAGTACAAAZTGTCATTAAGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAA"
answer = seq_translate(sequence)

print(answer)
