# String : A string is a immutable sequence of unicode charecters.
# String Modification

s1 = "WORD"
print("Original String :", s1)

l1=list(s1)
print("List String :", l1)

l1.insert(3, "L")
print("Updated List String :", l1)

# separetor.join(list)
s2 = ''.join(l1)
print("New String :", s2)


# String Concatenation
old1 = "Hello"
old2 = "World"
new = old1 + ' ' + old2
print(new)


# String Formating
# using % operator
# using format() mathod of str class
# using f-string

name = "Tutorialspoint"
city = "Dhaka"
age = 35

# using % operator
print("Welcome to %s" %name)
print("Welcome to %s at %s!" %(name, city))
print("Welcome to %s at %s when %d!" %(name, city, age))


# using f-string
print(f"Welcome to {name} at {city} when {age}!")


# using format() method of str class
data_string = "Welcome to {} at {} when {}!"
print(data_string.format("Tutorialspoint", "Dhaka", 35))
data_string = "Welcome to {} at {} when {}!".format("Tutorialspoint", "Dhaka", 35)
print(data_string)
