# Write to a file
file = open("myfile.txt", "w")
file.write("Hello, this is a simple file handling example.")
file.close()

# Read from the file
file = open("myfile.txt", "r")
content = file.read()
print("File content:")
print(content)
file.close()
