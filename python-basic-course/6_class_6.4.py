# OOP ( Object Oriented Programming ) Recap
# Abstraction
# Encapsulation
# Inheritance
# Polymorphism

# Encapsulation example Class
class SecretFile:
	_balance = 1000 # _ makes it private
	name = ""

	def print_balance(self):
		print(f"Your current balance is {self._balance}")

	def set_balance(self, new_balance):
		if new_balance < 2000:
			print("Balance update not possible.")
		else:
			self._balance = new_balance
			print("Balance update successful.")

# Creating Objects
user_1 = SecretFile()
user_1.name = "Mr. Kamal"
# print(user_1.balance)

new_balance = int(input("Enter new Balance: "))
user_1.set_balance(new_balance)
user_1.print_balance()



# Encapsulation example Class
class Computer:
	def __init__(self):
		self.__maxprice = 900

	def sell(self):
		print(f"Selling price : {self.__maxprice}")

	def setMaxPrice(self, price):
		self.__maxprice = price

# Creating Objects
device_1 = Computer()
device_1.sell()

# Update device price
device_1.__maxprice = 1000
device_1.sell()

# Using setter function
device_1.setMaxPrice(5000)
device_1.sell()