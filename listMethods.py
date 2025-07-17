list1 = [1, 2, 3.90, "abc"]
print("Original list:", list1)

# Accessing elements
print("First element:", list1[0])
print("Last element:", list1[-1])

# Slicing
print("Slice [1:3]:", list1[1:3])

# Adding elements
list1.append(5)
print("After append(5):", list1)

list1.insert(2, "new")
print('After insert(2, "new"):', list1)

# Extending the list
list1.extend([6, 7])
print("After extend([6, 7]):", list1)

# Removing elements
list1.remove("abc")
print('After remove("abc"):', list1)

popped_item = list1.pop()
print("After pop():", list1)
print("Popped item:", popped_item)

# Finding elements
index_2 = list1.index(2)
print("Index of element 2:", index_2)

# Counting elements
count_2 = list1.count(2)
print("Count of element 2:", count_2)

# Reversing the list
list1.reverse()
print("After reverse():", list1)

# Copying the list
list_copy = list1.copy()
print("Copied list:", list_copy)

# Clearing the list
list1.clear()
print("After clear():", list1)
