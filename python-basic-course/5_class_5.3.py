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

# To make it simple for "open - file related work - close" use "with open("filename", "mode") as file:"

# File write
# write() - Writes string to file
# writelines() - writes all string as lines to file

with open("5_file_5.2.txt", "r+") as file:
	file.write("BongoDev")
	file.seek(0)
	print(file.read())
