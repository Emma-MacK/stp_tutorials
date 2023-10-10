# Script to handle python exercise 3

# Write a script to opens file 1abc.sec, count the number of lines, print number of lines back to the user

line_total = 0

with open("resources/1abc.sec", "r") as f:
    for line in f:
        line_total+=1

print(line_total)
