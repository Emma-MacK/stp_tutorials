# develop a function which gives the GC content of a sequence. This is the number of G plus C bases in a sequence as a percentage of the total number of bases

### plan ###

# convert to upper case
# count occurances of C or G in a sequence
# get sequence length

seq = "aggagtaagcccttgcaactggaaatacacccattg"

def calc_GC(sequence):
    sequence=sequence.upper()
    G_count = sequence.count("G")
    C_count = sequence.count("C")
    GC_content = round((G_count + C_count)/len(sequence)*100, 2)
    print("The GC content is:", GC_content, "%")

calc_GC(seq)