# python buit in function : enumerate 
# for index, item in enumerate(iterable)

num_list = [10, 25, 33, 40, 5, 68]

# without index
for num in num_list:
	print(num)


print("-----------")

# with index
for index, num in enumerate(num_list):
	print(index, num)


print("-----------")

# with or without index
for num in num_list:
	print(num_list.index(num), num)
