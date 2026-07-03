# In Python, the sorted() function works on any iterable, including lists, tuples, sets, dictionaries, and strings.
# It's created new list.
# sorted function took three argument, although those are not mendatory  
# sorted(iterable / list, key=none, reverse=False)

num_list = [10, 25, 33, 40, 5, 68]
name_list = ["python", "Java", "C", "C++", "PHP"]

# print before sort
print(num_list)
print(name_list)

# By default python will sort from small to big OR in ascending order in a list where reverse is False.
# print after sort
new_num_list = sorted(num_list, reverse=True)
print(new_num_list)

new_name_list = sorted(name_list, reverse=True)
print(new_name_list)