# Take two numbers as input, print "Genjam" if one is negative and one is positive. Else print "Thik ase"
# Example:
# input_1 = -5
# input_2 = 7
# This should print "Genjam"
#  Hint: use conditionals with logical operators


input_1 = int(input("Enter the first number: "))
input_2 = int(input("Enter the second number: "))

if (input_1 < 0 and input_2 > 0) or (input_1 > 0 and input_2 < 0):
    print("Genjam")
else:
    print("Thik ase")