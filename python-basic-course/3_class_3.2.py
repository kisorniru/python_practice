# python sort function or sort() is only work upon list
# It's not created any new list rather it's updated the existing list
# sort function took two argument, although those are not mendatory  
# lsit.sort(key=none, reverse=False)

num_list = [10, 25, 33, 40, 5, 68]
name_list = ["python", "Java", "C", "C++", "PHP"]

# print before sort
print(num_list)
print(name_list)

# By default python will sort from small to big OR in ascending order in a list where reverse is False.
# print after sort
num_list.sort()
print(num_list)
name_list.sort()
print(name_list)


# To change default sorting order use reverse argument as True
# print after sort
num_list.sort(reverse=True)
print(num_list)
name_list.sort(reverse=True)
print(name_list)

