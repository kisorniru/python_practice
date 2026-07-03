# Write a python program to find number of vowels in a given string.
# Input: "hello world!"
# Output: 3


vowels = "aeiouAEIOU"
vowel_count = 0

my_str = input("Enter a string : ")

for vowel in my_str:
	if vowel in vowels:
		vowel_count = vowel_count + 1


print("Total vowel : ", vowel_count)