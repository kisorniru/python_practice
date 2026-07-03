# Functions
# Buit-In Function : print(), len() etc.
# Module Functions
# User-Define Functions
# Python function is a block of organized, reusable code that is used to perform a single, related action.
# Input -> Function -> Output

# Function syntex
"""
def function_name( perameters ):
	"function_docstring"
	function_suite
	return [expression]
"""

def greetings():
	print("Hello world!")
	return

def sum_numbers(a, b):
	sum = a + b
	# print(sum)
	return sum

greetings()
sum = sum_numbers(5, 2)
print(sum)