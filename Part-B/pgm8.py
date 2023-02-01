# This program implements the FLAMES game

def flames(name1, name2):
    # Concatenate the two names and remove common letters
    full_name = name1 + name2
    for letter in name1:
        if letter in name2:
            full_name = full_name.replace(letter, '', 2)
    # Calculate the length of the full_name
    length = len(full_name)
    # Define the FLAMES acronym
    flames = 'FLAMES'
    while len(flames) > 1:
        # Get the position to split the string
        split_pos = (length - 1) % len(flames)
        # Split the string and keep only the second part
        flames = flames[split_pos + 1:] + flames[:split_pos]
    # Return the result
    if flames == 'F':
        return 'Friends'
    elif flames == 'L':
        return 'Love'
    elif flames == 'A':
        return 'Affection'
    elif flames == 'M':
        return 'Marriage'
    elif flames == 'E':
        return 'Enemy'
    else:
        return 'Sibling'

# Get the two names
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

# Get the result
result = flames(name1, name2)

# Print the result
print("The relationship is:", result)