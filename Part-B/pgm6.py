#Implementation of the problem solving strategies: either using Forward Chaining or Backward Chaining

# List of facts in the form of [X, Y], where X is an action and Y is an object
facts = [['croaks', 'frog'],
         ['eatsflies', 'frog'],
         ['frog', 'green'],
         ['chirps', 'canary'],
         ['sing', 'canary'],
         ['canary', 'yellow']]


def find_related_facts(starting_facts, all_facts):
    # List to store related facts
    related_facts = []
    # Flag to control the while loop
    keep_finding = True

    while keep_finding == True:
        keep_finding = False
        # Loop through each starting fact
        for fact in starting_facts:
            # Loop through all facts
            for f in all_facts:
                # If a fact is found that relates to the current fact
                if f[0] == fact:
                    # Create a new related fact from the two related facts
                    new_related_fact = [fact, f[1]]
                    # Add the new related fact to the list of related facts,
                    # if it doesn't already exist in the list
                    if new_related_fact not in related_facts:
                        related_facts += [new_related_fact]
                        starting_facts += [f[1]]
                        keep_finding = True
    return related_facts


# Example usage
result = find_related_facts(['croaks', 'frogs'], facts)
print(result)
