# Write a python program to create a class that represents a shape. Include methods to calculate its area and perimeter.
# Implement subclasses for different shapes like circle, triangle and square.

class Shape:
	def area(self):
		raise NotImplementedError

	def perimeter(self):
		raise NotImplementedError


class Circle(Shape):
	def __init__(self, radius):
		if radius <= 0:
			raise ValueError("Radius must be positive.")

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

class Triangle(Shape):
	def __init__(self, base, height, side1, side2, side3):
		if base <= 0:
			raise ValueError("Base must be positive.")

		if height <= 0:
			raise ValueError("Height must be positive.")
		
		if side1 <= 0:
			raise ValueError("Side 1 must be positive.")
		
		if side2 <= 0:
			raise ValueError("Side 2 must be positive.")
		
		if side3 <= 0:
			raise ValueError("Side 3 must be positive.")

		if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
			raise ValueError("Invalid triangle sides.")
		
		self.base = base
		self.height = height
		self.side1 = side1
		self.side2 = side2
		self.side3 = side3

	def area(self):
		# area calculation formula : 0.5 * base * height
		return 0.5 * self.base * self.height

	def perimeter(self):
		# perimeter calculation formula : side1 + side2 + side3
	 	return self.side1 + self.side2 + self.side3

class Square(Shape):
	def __init__(self, side):
		if side <= 0:
			raise ValueError("Side must be positive.")
		
		self.side = side

	def area(self):
		# area calculation formula : side^2
		return self.side ** 2

	def perimeter(self):
		# perimeter calculation formula : 4 * side
	 	return 4 * self.side

# Helper function, outside all classes, you can place it into another file as well 
def print_shape_details(name, shape):
    print(f"{name} area : {shape.area():.2f}")
    print(f"{name} perimeter : {shape.perimeter():.2f}")

# Another helper function for object creation with try-except
def process_shape(shape_name, shape_class, *args):
    try:
        shape_object = shape_class(*args)
    except ValueError as e:
        print(e)
    else:
        print_shape_details(shape_name, shape_object)
    finally:
        print("Program finished")

# Object creation
process_shape("Circle", Circle, 5)
print("---------")
process_shape("Triangle", Triangle, 5, 5, 5, 5, 6)
print("---------")
process_shape("Square", Square, 5)
