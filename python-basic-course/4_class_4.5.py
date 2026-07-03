# Python tuple
# A tuple is a sequence of comma separeted items
# Enclosed in parentheses ()
# Emmutable, can not be changed, removed, added.
# Modification can be done by converting to the list.

my_tup = (1, 2, 3, 4, 4, 5, 2, 4)
print(my_tup)

# access
print(my_tup[1])

# count
print(my_tup.count(4))

# index
print(my_tup.index(5))

# join
my_tup_1 = (1, 2, 3)
my_tup_2 = (7, 8, 9)
new_tup = my_tup_1 + my_tup_2
print(new_tup)

# looping
for x in new_tup:
	print(x)



# tuple modification
my_tup = (1,2,3)
my_tup_to_list = list(my_tup)
print(my_tup_to_list)

my_tup_to_list.append(4)
print(my_tup_to_list)
my_tup_to_list.insert(4,5)
print(my_tup_to_list)
my_tup_to_list.remove(5)
print(my_tup_to_list)
my_tup_to_list.clear()
print(my_tup_to_list)
my_tup_to_list.append(1)
my_tup_to_list.append(1)
my_tup_to_list.append(2)
my_tup_to_list.append(3)
print(my_tup_to_list)

my_tup_from_list = tuple(my_tup_to_list)
print(my_tup_from_list)