# program to find common elements in two list with the help of set operations
# Input: l1 = [1,2,3]
# Input: l2 = [3, 4]
# Output: [3]

my_list_1 = [1,2,3,4]
my_list_2 = [3,4,5,6,7,8]


my_set_1 = set(my_list_1)
my_set_2 = set(my_list_2)

print(my_set_1)
print(my_set_2)
print("------------")

my_union_set = my_set_1.union(my_set_2) 
print(my_union_set) # {1, 2, 3, 4, 5}

my_union_set = my_set_2.intersection(my_set_1) 
print(my_union_set)