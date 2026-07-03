# File Handling
# Open a file
# Read / Write on the file
# Close

# file = open("filename", "mode")
# mode = read / write / read only / append

# File Opening Modes
# r for reads
# r+ opens for read and writing (can not truncate a file)
# w for writing
# w+ for writing and reading (ca truncate a file)
# rb for reading a binary file. The file pointer is placed at the beginning of the file.
# rb+ reading or writing a binary file.
# wb+ writing a binary file.
# a+ opens for appending.
# ab+ opens a file for both appending and reading a binary file.

# File Open
my_file = open("5_file_5.2.txt", "r")
print(my_file) # Prints the file object details (like name, mode, and encoding), not its contents.
print("----------------------")

# File Read
# read() - Reads the entire file
# readline() - Reads one line at a time
# readlines() - Reads all lines into a list

print(my_file.read()) # Reads everything from start to finish. The cursor is now at the end.
print("----------------------")
print(my_file.readline()) # Returns an empty string ("") because there is no text past the end.
print("----------------------")
print(my_file.readlines()) # Returns an empty list ([]) for the same reason.
print("----------------------")


# Reset cursor to the beginning (index 0)
my_file.seek(0)
print(my_file.readline()) # Returns an empty string ("") because there is no text past the end.
print("----------------------")

# Reset cursor to the beginning (index 0)
my_file.seek(0)
print(my_file.readlines()) # Returns an empty list ([]) for the same reason.
print("----------------------")

# File Close
my_file.close()

# To make it simple for "open - file related work - close" use "with open("filename", "mode") as file:"
with open("5_file_5.2.txt", "r") as file:
	print(file.read())

