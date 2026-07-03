# Single line comment
# Type Casting
a = 10
b = 20.5
c = a + b
print(f"Before type casting: {c}")

"""
Multi-line comment
This is a multi-line comment that can span multiple lines.
It is often used for longer explanations or documentation.
"""
# Type Casting
a = True
b = 10.5
c = a + b
print(f"Before type casting: {c}")

# input string
name = str(input("Enter your name: "))
print (f"Hello, {name}!")

# Control Statements
# if-else
expression = input("Enter your expression operator (+, -, *, /, %, **, //): ")

if expression == "+":
    print("You have selected addition.")
elif expression == "-":
    print("You have selected subtraction.")
elif expression == "*":
    print("You have selected multiplication.")
elif expression == "/":
    print("You have selected divission.")
elif expression == "%":
    print("You have selected modulus.")
elif expression == "**":
    print("You have selected exponentials.")
elif expression == "//":
    print("You have selected floor division.")
else:
    print("Invalid operator selected.")