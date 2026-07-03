# write a python program to list unique characters with their count in a string
# Input: "hello"
# Output: h=1, e=1, l-2, o=1


def count_unique_charecters(my_str):
	# create a list
	char_counts = {}

	# Loop through each charecter in the string
	for char in my_str:
		if char in char_counts:
			char_counts[char] += 1
		else:
			char_counts[char] = 1

	# print char_counts current stage
	print("-------------")
	print(char_counts)
	print("-------------")

	# display the results
	for char, count in char_counts.items():
		print(f"'{char}' : {count}")



my_str = input("Enter a string: ") # hello world
count_unique_charecters(my_str)