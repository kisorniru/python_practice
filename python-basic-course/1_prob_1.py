# Take a heights of your 2 friends (in inches) as input and print their average height!
# Example:
# height_1 = 68
# height_2 = 70
# This should print 69
# Hint: use variables to take inputs
# Print the average height in ft and inch format (5'7")

height_1 = float(input('Enter the height of your first friend in inches: '))
height_2 = float(input('Enter the height of your second friend in inches: '))
average_height = (height_1 + height_2) / 2
print("The average height of your friends is:", average_height, "inches")
print(f"The average height of your friends in feet and inches is:", int(average_height // 12), "'", int(average_height % 12), '"')