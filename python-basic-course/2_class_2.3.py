# Data type: List
# List is a sequence of comma separated values which is ORDERED and CHANGEABLE. Allows duplicate members. 
# List encloses values in square brackets [].
# Inside a list, we call each value an item.
# List can hold different data types like int, float, string, etc.
# Example : [1, 'a', 3.5, True, [1, 2, 3], (4, 5), {6: 'six'}]

my_list = [25, 35, 40]
x = my_list[0] # access
my_list[1] = 544 # change / update
print(x)
print(my_list)

my_list.append(45) # It will add in the last

print(my_list)
my_list.insert(2, 35) # It will insert 35 at index 2; insert(index, value)

print(my_list)

my_list.remove(35) # It will remove the first occurrence of 35
print(my_list)

my_list.pop() # It will remove the last item from the list
print(my_list)

my_list.pop(1) # It will remove the item at index 1 from the list
print(my_list)

for num in my_list: # It will print all the items in the list
    num = num - 5
    print(num)


for num in my_list: # It will print all the items in the list
    my_list[my_list.index(num)] = num - 5

print(my_list)



















