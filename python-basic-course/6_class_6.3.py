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
	def meao(self):
		print(f"{self.name} is saying meao.")


# Create Object
cat1 = Cat()
cat1.name = "Tom"
cat1.meao()
cat1.make_sound()


# Derived Class
class Dog(Animal):
	def meao(self):
		print(f"{self.name} is saying bukhvukh.")


# Create Object
dog1 = Dog()
dog1.name = "Pluto"
dog1.meao()
dog1.make_sound()