# Initializing a nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Length of nested list
print("Length of nested list: ", len(nested_list))

# Concatenation of nested list
concatenated_list = [1, 2, 3] + [4, 5, 6] + [7, 8, 9]
print("Concatenated list: ", concatenated_list)

# Membership in nested list
print(3 in nested_list)  # returns true

# Iteration over nested list
for sub_list in nested_list:
    for val in sub_list:
        print(val)

# Indexing and Slicing in nested list
print(nested_list[1])    # returns [4, 5, 6]
print(nested_list[1][2]) # returns 6
