# Error Handling

# # Syntax Error in python or any other programming language is an error that occures when the code does not follow the syntax rules of that language.
# # like no semocolon needed in python so if you do it than it's a syntax error, like indentation missing in python is a syntax error.
# # Programmer should be careful about it and they have to deal it by there own.
# # Example
"""
nums = [1,2
print(nums) # it will generate an Invalid syntax error due to not having closing braces for list.
"""

# Exception handling

# # An exception is an event, which occurs during the execution of a program that disrupts the flow of the program's execution.
# # Syntactically code is okay but logically not okay.
# # Example
"""
x = 3 / 0
print(x) # Syntactically code is perfect but logically you can't devide anything by zero so here is a ZeroDivisionError. This is an exception. 
"""

# Types of Exceptions

# # Python features over 60 built-in exceptions.
# # Here is the most common exception
# Exception
# SyntaxError
# StopIteration
# ValueError
# TypeError
# IndexError
# KeyError
# SystemExit
# ArithmeticError
# OverflowError
# FloatingPointError
# ZeroDivisionError
# AssertionError
# AttributeError
# IOError
# FileNotFoundError
# ...


# Exception Handling
"""
try:
	you do your operation here which might create an exception
except Exception1:
	If there is exception 1 then execute this block
except Exception2:
	If there is exception 2 then execute this block
else:
	If there is no exception then execute ihis block
finally:
	An optional block that always runs regardless of whether an error occurred or not, usually used for cleanups like closing files.
"""

try:
	x = 3 / 0
	print(x)
except:
	print("an exception occure")


print("-------------------------")

# Specify the exception

try:
	x = 3 / 0
	print(x)
except ZeroDivisionError:
	print("You can't devided by zero.")


print("-------------------------")

# Specify the exception

try:
	y = int(input("Enter the nunber: "))
	x = 3 / y
	print(x)
except ZeroDivisionError:
	print("Zero Division Error : You can't devided by zero.")
except ValueError:
	print("Value Error : Please input an integer number.")
else:
	print("No error occure")
finally:
	print("Always show")


print("-------------------------")

# Custom exception

try:
	x = int(input("Enter the nunber: "))
	if x % 2 == 0:
		raise Exception("I can't allow this, this is a custom exception message.")
except ZeroDivisionError:
	print("Zero Division Error : You can't devided by zero.")
except ValueError:
	print("Value Error : Please input an integer number.")
except Exception as e:
	print(e)
except Exception:
	print("Caught an custom error")
else:
	print("No error occure")
finally:
	print("Always show")