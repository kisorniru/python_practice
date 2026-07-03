# Dictionary in Python
# dictionary is mutable
# No restriction in data-type 
# Data type that stores data in key-value pairs.
# Each key in a dictionany is unique and maps to a value.

# Example
"""
my_dictionary = {
	"Fruit" : ["Mango", "Banana"],
	"Flower": ["Lotus", "Rose"]
}
"""

# In dictionary one key-value pair is called as item
# Example: dict_eg = {'d': 'Dog', 'e': '20', 1: 'one'}
#                     ----------  ---------  --------
#                       item 1      item 2    item 3


my_dict = {
	"Fruit" : ["Mango", "Banana"],
	"Flower": ["Lotus", "Rose"]
}

# access
print(my_dict["Fruit"]) 		# If does not exist: return keyError
print(my_dict.get("Fruit")) 	# If does not exist: return None
print(my_dict.get("cake", "Nothing Found"))


# Add
my_dict["Cake"] = ["Chocolate", "Pastry", "Ice"]
print(my_dict)

# Modify
my_dict["Cake"] = ["Vanilla", "Vanilla Butter"]
print(my_dict)

# Add / Update using update() method
my_dict.update({"Cuisine": ["Chinise", "Thai", "Indian"], "Cake": ["Chocolate", "Pastry", "Ice"]})
print(my_dict)

# Remove
del my_dict["Cake"]
print(my_dict)

# pop
my_dict.pop("Cuisine")
print(my_dict)

print("---------------------------")

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items()) # return an tuple

print("---------------------------")

for key, value in my_dict.items():
	print(key, value)

print("---------------------------")

new_my_dict = my_dict.copy()
print(new_my_dict)

print("---------------------------")
print("Cake" in new_my_dict)


print("---------------------------")
new_my_dict.setdefault("key1", 80)
print(new_my_dict)

new_my_dict["key1"] = 100
print(new_my_dict)