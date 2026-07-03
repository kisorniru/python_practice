# Write a python function to print the maximum of three numbers
# Output should be: 15 for input of 10, 15, 5

def max_num(a, b, c):
	if a > b and a > c:
		return a
	elif b > a and b > c:
		return b
	else:
		return c

max = max_num(25, 20, 15)
print("Max Num :", max)
