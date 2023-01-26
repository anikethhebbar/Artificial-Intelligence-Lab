# Initializing sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Union of sets
print("Union: ", A.union(B))

# Intersection of sets
print("Intersection: ", A.intersection(B))

# Difference of sets
print("Difference (A - B): ", A.difference(B))
print("Difference (B - A): ", B.difference(A))

# Checking if a set is a subset of another set
print("Is A a subset of B: ", A.issubset(B))

# Checking if a set is a superset of another set
print("Is A a superset of B: ", A.issuperset(B))
