# 1.2 Given a string and two pairs of integers, return two slices of the string between the positions represented by the two number pairs inclusively

def string_slice(string, a_slice_1, a_slice_2, b_slice_1, b_slice_2):
    slice_1 = string[int(a_slice_1):int(a_slice_2)]
    slice_2 = string[int(b_slice_1):int(b_slice_2)]
    answer = slice_1 + " " + slice_2
    return answer 

string_in = "TheUniversityOfManchesterFacultyofBiologyMedicineAndHealth"

answer = string_slice(string_in, 3, 13, 15, 25)
print(answer)
