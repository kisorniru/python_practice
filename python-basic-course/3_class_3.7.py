# Function Arguments ()
# Default
# Keyword
# Positional
# Arbitrary

# Default Arguments
def showinfo( name, city = "Dhaka" ):
	"This prints a passed info into this function"
	print("Name :", name)
	print("City :", city)
	return

showinfo(name = "Siddique", city = "Sylhet")
showinfo(name = "Siddique")

print("---------------------------")


# Keyword & Positional Arguments
def printinfo( name, age ):
	"This prints a passed info into this function"
	print("Name :", name)
	print("Age :", age)
	return

# when you call the function by defining the argument with keyword, it's called keyword argument
printinfo(name = "Keyword Argument", age = 34)
print("---------------------------")
printinfo(age = 34, name = "Keyword Argument")

print("---------------------------")

# when you call the function by defining the argument without keyword, it's called positional argument
printinfo("Positional Argument", 34)


print("---------------------------")

# Arbitrary / Variable Arguments
def add(*args):
	s = 0
	for x in args:
		s = s + x
	return s

result = add(10, 2, 8, 20)
print("Arbitrary Argument :", result)