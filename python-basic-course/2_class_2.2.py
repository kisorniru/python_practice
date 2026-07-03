# Loops
# Following iis the multiline comment in python.
"""
Loops are used to execute a block of code repeatedly until a certain condition is met. There are two main types of loops in python: for loops and while loops. 

For loops are used to iterate over a sequence (like a list, tuple, or string) and execute a block of code for each item in the sequence.

For while loops are used to execute a block of code repeatedly as long as a certain condition is true. The loop will contain a condition that is checked before each iteration, and if the condition is false, the loop will terminate. 
"""

# For Loop
# for iterating_variable in sequence:
#   statement(s)

"""
name = "python"
for char in name:
    print(char)


a = 10
b = 20
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for number in number_list:
    sum = sum + number
    print("Sum of first", a, "numbers is:", sum)
"""

# range(start, stop, step) 
# start default is 0
# stop is required
# step default 1
"""
for number in range(1,21,2):
    print(number)
"""


# while loop
# while expression:
#   statement(s)

"""
counter = 0
while counter < 5:
    counter += 1
    print("Counter value:", counter)
"""

# Nested Loops
# A nested loop is a loop inside another loop. The inner loop will be executed one time for each iteration of the outer loop. Nested loops can be used to iterate over multi-dimensional data structures, such as lists of lists or matrices.

"""
for num1 in range(1, 3):
    for num2 in range(1, 6):
        print(f"Outer loop iteration: {num1}, Inner loop iteration: {num2}")
"""

# Loop control statements
# Loop control statements are used to change the flow of execution in a loop. There are three main loop control statements in python: break, continue, and pass.

# break : stops the loop and exist the loop imidiately.
name = "python"
for char in name:
    if char == "t":
        break
    print(char)


print("--------------------------------")

# continue : skips the current iteration and moves to the next iteration of the loop.
name = "python"
for char in name:
    if char == "t":
        continue
    print(char)

print("--------------------------------")

# pass : does nothing and is used as a placeholder for future code. It can be used in loops, functions, and classes where a statement is required syntactically but you do not want to execute any code.
name = "python"
for char in name:
    if char == "t":
        pass
    print(char)





















