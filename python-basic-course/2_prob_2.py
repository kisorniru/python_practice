# Given List; num_list = [1, 4, 5, 23, 10, 12, 15, 19, 25]
# Loop through the list and print the numbers that are divisible by 5
# output: 5, 10, 15, 25

num_list = [1, 4, 5, 23, 10, 12, 15, 19, 25]
divisibled_num = []

for divisibled_by_num in num_list:
	if divisibled_by_num % 5 == 0:
		divisibled_num.append(divisibled_by_num)
		print(divisibled_by_num)

print(divisibled_num)