s = "  Hello, Python World!  "

print("Original string:", repr(s))

# Accessing characters
print("First character:", s[0])
print("Last character:", s[-1])

# Slicing
print("Slice [2:8]:", s[2:8])

# Length
print("Length:", len(s))

# Strip whitespace
print("Strip:", s.strip())

# Convert to uppercase and lowercase
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())

# Replace substring
print("Replace 'Python' with 'Java':", s.replace("Python", "Java"))

# Split string into list
print("Split by comma:", s.split(","))

# Find substring index (-1 if not found)
print("Index of 'Python':", s.find("Python"))
print("Index of 'Java':", s.find("Java"))  # Not found, returns -1

# Check startswith and endswith
print("Starts with '  He':", s.startswith("  He"))
print("Ends with '!  ':", s.endswith("!  "))

# Join list into string
words = ["Python", "is", "awesome"]
joined = " ".join(words)
print("Join words:", joined)

# Count occurrences of substring
print("Count of 'o':", s.count("o"))

# Concatenation
greet = "Hi"
combined = greet + ", " + s.strip()
print("Concatenated string:", combined)

# Repetition
print("Repeat greet 3 times:", greet * 3)

# Membership test
print("'World' in s?", "World" in s)
print("'Java' in s?", "Java" in s)
