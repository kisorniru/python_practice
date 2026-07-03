# Print all even numbers from 2 to 50 using a for loop

even_numbers = []

for num in range(2, 50):
    if num % 2 == 0:
        # print(num)
        even_numbers.append(num)

print("Even numbers from 2 to 50:", even_numbers)

# Another way using range(start, stop, step)

new_even_numbers = []

for num in range(2, 50, 2):
    new_even_numbers.append(num)

print("New Even numbers from 2 to 50:", new_even_numbers)