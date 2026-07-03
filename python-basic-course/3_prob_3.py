# Write a python function to check weather a number falls within the range (1, 100)
# print Yes or No
# Output should be: "Yes", for input 15 and "No" for input 110

def num_in_range(num):
	if num >= 1 and num <=100:
		print("Yes")
	else:
		print("No")


num_in_range(101)