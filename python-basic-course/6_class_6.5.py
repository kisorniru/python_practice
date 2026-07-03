# OOP ( Object Oriented Programming ) Recap
# Abstraction
# Encapsulation
# Inheritance
# Polymorphism


# Base Class
class Animal:
	name = ""
	age = 0
	color = ""

	def make_sound(self):
		print("Sound")



# Derived Class
class Cat(Animal):
	def make_sound(self):
		print(f"{self.name} is saying meao.")


# Create Object
cat1 = Cat()
cat1.name = "Tom"
cat1.make_sound()


# Derived Class
class Dog(Animal):
	def make_sound(self):
		print(f"{self.name} is saying bukhvukh.")


# Create Object
dog1 = Dog()
dog1.name = "Pluto"
dog1.make_sound()



# # Better Coding style

# Base Class
class betterAnimal:
	
	def __init__(self, name, age=None, color=None):
		self.name = name
		self.age = age
		self.color = color

	def make_sound(self):
		print("Sound")



# Derived Class
class Cat(betterAnimal):

	def __init__(self, name, age=None, color=None):
		super().__init__(name, age, color) # Use super() to inherit properly

	def make_sound(self):
		print(f"{self.name} is saying meao.")


# Create Object
cat1 = Cat("Tom")
cat1.make_sound()


# Derived Class
class Dog(betterAnimal):

	def __init__(self, name, age=None, color=None):
		super().__init__(name, age, color) # Use super() to inherit properly

	def make_sound(self):
		print(f"{self.name} is saying bukhvukh.")


# Create Object
dog1 = Dog("Pluto")
dog1.make_sound()