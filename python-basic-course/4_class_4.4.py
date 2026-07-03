# Python Set
# A set is an unordered collection of unique elements
# does not allow duplicates
# defined inside {} braces or set()

numbers = [1, 2, 3, 4]
my_set = {1, 2, 3, 4, 4}
another_set = set(numbers)


print(my_set)
print(another_set)

# list to set conversion
my_list = [1, 2, 3, 4]
my_set = set(my_list)
print(my_set) # {1, 2, 3, 4}


# set to list conversion
my_set = {1, 2, 3, 4}
my_list = list(my_set)
print(my_list) # [1, 2, 3, 4]

# add inside a set
my_set = {1, 2, 3, 4}
my_set.add(5)
print(my_set)


# remove from a set
my_set = {1, 2, 3, 4, 5}
my_set.remove(5)
print(my_set)


# update a set
my_set = {1, 2, 3, 4, 5}
my_set.update([6, 7, 8])
print(my_set)

print("-----union-----")

# union of sets when intake the fist one
my_set_1 = {1, 2, 3, 4, 5}
my_set_2 = {3, 4, 5, 6, 7, 8, 9}
my_set_1.union(my_set_2) # my_set_1 | my_set_2
print(my_set_1)

# union of sets when intake the second one
my_set_1 = {1, 2, 3, 4, 5}
my_set_2 = {3, 4, 5, 6, 7, 8, 9}
my_set_2.union(my_set_1) # my_set_1 | my_set_1
print(my_set_2)

# union of sets when intake the fist one
my_set_1 = {1, 2, 3, 4, 5}
my_set_2 = {3, 4, 5, 6, 7, 8, 9}
my_set_1 | my_set_2 # my_set_1.union(my_set_2)
print(my_set_2)

print("-----union-----")

# clear a set
my_set = {1, 2, 3, 4, 5}
my_set.clear()
print(my_set)


# Looping in set
my_set = {1, 2, 3, 4, 5}
for x in my_set:
	print(x)












