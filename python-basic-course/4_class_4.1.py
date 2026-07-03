# String : A string is a immutable sequence of unicode charecters.
# Enclosed in a single or double or triple quotes.

name = "BongoDev"
print(name)
print("------------------")

for char in name:
	print(char)

print("------------------")
print(name[3])


# string : positive index : 0,1,2,3
# string : negetive index : -1,-2,-3

print("------------------")
print(name[-1])

# string slicing : 0,1,2,3

var = "HELLO PYTHON"
print(var[2]) # L
print(var[-12]) # H

# positive slicing [start index : before end index]
print(var[3:8]) # LO PY

# positive slicing [start index : before end index]
print(var[1:5]) # ELLO


# positive slicing [start index, it's default value is 0': before end index]
print(var[:5]) # HELLO
