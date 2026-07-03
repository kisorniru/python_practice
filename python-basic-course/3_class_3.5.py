# List methods


num_list = [10, 20, 30, 40, 50]
print(num_list)

# It'll clear the entire list.
num_list.clear()
print(num_list)


# Find the index
num_list = [10, 20, 30, 40, 50, 10]
x = num_list.index(40)
print(x)

# Find the object count
num_list = [10, 20, 30, 40, 50, 10]
x = num_list.count(10)
print(x)


# Find the length of the list
num_list = [10, 20, 30, 40, 50, 10]
x = len(num_list)
print(x)


# Copy the list
num_list = [10, 20, 30, 40, 50, 10]
new_num_list = num_list.copy()
print(new_num_list)