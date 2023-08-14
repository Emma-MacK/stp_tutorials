# Given two positive integers a and b, return the sum of all odd integers from a to b inclusively

def sum_range(int_1, int_2):
    total = 0 
    x = range(int(int_1), int(int_2) +1)
    for n in x:
        if n % 2 == 1:
            total = total + n
    return total

answer = sum_range(10, 25)
print(answer)

