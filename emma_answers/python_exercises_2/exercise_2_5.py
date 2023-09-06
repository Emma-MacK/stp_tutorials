# count single, di-nucleotide, and tri nucleotides in a sequence
import itertools
### plan ###

# get sequence, split into desired sizes for each frame, count unique occurances
# different desired groups have different potential frames (ie single there is only one frame, duo has two, trio has 3)

sequence="aggagtaagcccttgcaactggaaatacacccattg"

def find_nucleotides(sequence,group_size):
    # get possible combinations
    # make empty list
    nucleotide_groups=[]
    # get desired frame
    for frame in range(0,group_size):
        # loop to select characters in desired frame, producing a range with gaps the size of the desired grouping
        for i in range(frame, len(sequence), group_size):
            # add to list of nucleotide groups
            if len(sequence[i:i+group_size]) == group_size:
                nucleotide_groups.append(sequence[i:i+group_size])
            else:
                nucleotide_groups.append("shorter than desired group")
    # find all possible unique occurances for size
    unique=list(itertools.product(["a", "t", "g", "c"],repeat=group_size))
    # convert from list of tuples to a list
    possible=[]
    for item in unique:
        # print(item)
        uni = ""
        for i in item:
            # print(i)
            uni = uni + i
            # print(uni)
        possible.append(uni)
    # count occurances of each possible unique element
    unique_groups=""
    for element in possible:
        number=nucleotide_groups.count(element)
        unique_groups = unique_groups + element + "\t" + str(number) + "\n"
    print(unique_groups)

find_nucleotides(sequence,2)


