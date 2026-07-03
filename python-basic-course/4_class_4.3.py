# String Methods


name = "dhaka, bangladesh"

# Capitalized
print(name.capitalize())

# upper
print(name.upper())

# lower
print(name.lower())


# stip : removes all unnecessary white spaces
# rstrip : removes right side unnecessary white spaces
# lstrip : removes left unnecessary white spaces

new_name = "        hello          "
print(new_name.lstrip())
print(new_name.rstrip())
print(new_name.strip()) 


# split : make a string to a list by deviding a separetor.
name = "United States"
print(name.split('e'))


# numeric check
id = '123'
new_id = 'a123'
print(id.isnumeric())
print(new_id.isnumeric())

# digit check
id = '123'
new_id = 'a123'
print(id.isdigit())
print(new_id.isdigit())

# replace : replace old value with a new value
# This is case sensetive
old_sentence = "Sonarga is the capital of bangladesh."
new_sentence = old_sentence.replace("Sonarga", "Dhaka")
print(new_sentence)


# count (sub_string, start, end)
# count the sub string repeatition inside a string.
# via start and end, you can choose a block of string from a full string
print(new_sentence.count('a'))
print(new_sentence.count('a', 10, 20)) 



































