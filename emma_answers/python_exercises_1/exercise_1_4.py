# Given a string representing a DNA sequence, print it in blocks, i.e. with gaps every so many bases.
# get string, get number, get range of numbers from length of string
# splitting based on input number, 

def split_string(string, input_num):
    split_str = ""
    for i in range(0, len(string)+input_num, input_num):
        split_str = split_str + string[i - input_num: i] + " "
        # print(split_str)
    return split_str

# in_str="aggagtaagcccttgcaactggaaatacacccattg"
in_str="GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTGAT"
answer = split_string(in_str, 10)

print(answer)
