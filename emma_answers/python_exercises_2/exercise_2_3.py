# Write a function which generates the reverse complement of a sequence. Bonus points for dealing with gaps or incorrect base letters.


### take a sequence, reverse, replace. 

# need dict of A:t etc 
base_comp_dict = {"a":"t", "t":"a", "c":"g","g":"c","A":"T", "T":"A", "C":"G", "G":"C", "N":"N"}


def correct_bases(seq):
    corrected_seq = ""
    for i in seq:
        bases = ["A", "T", "C", "G", "a", "t", "c", "g"]
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
seq="GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTGAT"
answer = reverse_comp(seq)
print(answer)
