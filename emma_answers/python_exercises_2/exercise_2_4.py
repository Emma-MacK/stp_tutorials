
# Combine translation and reverse complement functions to generate a six frame translation of a DNA sequence. This means you should translate three forward reading frames starting at the first, second and third base of the first codon of the forward sequence, and three reverse reading frames starting at the first, second and third base of the first codon of the reverse complement of the sequence

base_comp_dict = {"a":"t", "t":"a", "c":"g","g":"c","A":"T", "T":"A", "C":"G", "G":"C", "N":"N"}
# make a dictionary to has codons and their matching amino acids

codon_bases_dict = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T','AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K','AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R','CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P','CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R','GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V','GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A','GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E','GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G','TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S','TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L','TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*','TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W'}
## codon_bases_dict["ATA"]

def correct_bases(seq):
    corrected_seq = ""
    for i in seq:
        bases = ["A", "T", "C", "G", "a", "t", "c", "G"]
        if i in bases:
            corrected_seq = corrected_seq + i
        else:
            corrected_seq = corrected_seq + "N"
    return corrected_seq

def reverse_comp(seq):
    reverse = correct_bases(seq[::-1])
    comp=""
    # print(reverse)
    for i in reverse:
        comp = comp + base_comp_dict[i]
    return comp

def seq_translate(seq):
    seq = seq.upper()
    seq = correct_bases(seq)  
    translation = "Forward \n"
    for frame in frames:
        translation = translation + str(frame + 1) + "\t"
        for i in range(frame, len(seq), 3):
            codon=seq[i:i+3]
            if codon in codon_bases_dict:
                translation=translation+codon_bases_dict[codon]
            elif len(codon) < 3:
                translation=translation
            else:
                translation=translation+"X" 
        translation = translation + "\n"
        
    # repeat for reverse 
    translation = translation + "Reverse \n"
    for frame in frames:
        seq = reverse_comp(seq)
        translation = translation + str(frame + 1) + "\t"
        for i in range(frame, len(seq), 3):
            codon=seq[i:i+3]
            if codon in codon_bases_dict:
                translation=translation+codon_bases_dict[codon]
            elif len(codon) < 3:
                translation=translation
            else:
                translation=translation+"X" 
        translation = translation + "\n"
    print(translation)

frames = [0, 1, 2]
#sequence = "aggagtaagcccttgcaactggaaatacacccattg"
sequence = "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCC"
answer = seq_translate(sequence)
print(answer)
