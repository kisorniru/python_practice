# Write a python program to create  a class representing a circle. Includes methods to calculate its area and perimeter.

class Circle:
	def __init__(self, radius):
		if radius <= 0:
			raise ValueError("Radius must be positive")
		else:
			self.radius = radius

	# Class variable not object specific.
	# Not everytime pi will create while object create.
	pi = 3.1416

	def area(self):
		# area calculation formula : pi * radius^2
		return self.pi * (self.radius ** 2)

	def perimeter(self):
		# perimeter calculation formula : 2 * pi * radius
	 	return 2 * self.pi * self.radius


try:
    circle_1 = Circle(5)
    circle_1_area =  circle_1.area()
    print(f"Circle area : {circle_1_area:.2f}")
    circle_1_perimeter = circle_1.perimeter()
    print(f"Circle perimeter : {circle_1_perimeter:.2f}")
except ValueError as e:
    print(e)
else:
    print("Circle 1 created successfully")
finally:
    print("Program finished")

print("---------")

try:
	circle_2 = Circle(10)
	circle_2_area =  circle_2.area()
	print(f"Circle area : {circle_2_area:.2f}")
	circle_2_perimeter = circle_2.perimeter()
	print(f"Circle perimeter : {circle_2_perimeter:.2f}")
except ValueError as e:
	print(e)
else:
	print("Circle 2 created successfully")
finally:
	print("Program finished")