# 2.1. Refer back to exercise 1.4, where we printed a DNA string in blocks, with a space between each block. Now further develop your code so that it displays a DNA string in the style used in GenBank records.

# get string, get number, get range of numbers from length of string
# splitting based on input number, 

def split_string(string, block_size, row_size):
    block = 0
    split_str = ""
    for i in range(0, len(string)+block_size, block_size):
        split_str = split_str + string[i - block_size: i] + "\t"
       # if block is divisible by block size, new row
        if block%row_size == 0:
            split_str = split_str + "\n" + str(block*block_size+1) +"\t"
        block = block+1
    split_str = split_str.lower()
    print(split_str)

# in_str="aggagtaagcccttgcaactggaaatacacccattg"
in_str="GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTGAT"
answer = split_string(in_str, 10,6)
print(answer)
