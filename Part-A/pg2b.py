# Initializing a list
my_list = [1, 2, 3]

# Add an element to the list
my_list.append(4)
print("After append: ", my_list)

# Add multiple elements to the list
my_list.extend([5, 6, 7])
print("After extend: ", my_list)

# Add an element at a specific index
my_list.insert(3, 8)
print("After insert: ", my_list)

# Remove an element from the list
my_list.remove(8)
print("After remove: ", my_list)

# Remove an element at a specific index
del my_list[3]
print("After delete: ", my_list)
