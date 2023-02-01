import re
def dnf(formula):
     # Base case: If the formula is a literal, return it as is
    if re.fullmatch(r'[A-Z]|~[A-Z]|()""', formula): return formula
    # Recursive case: If the formula is a compound statement, convert it to DNF
    if 'and' in formula or 'or' in formula:
        # Split the formula into its component parts
        parts = re.split(r'(?<=[^\w])or(?=[^\w])|(?<=[^\w])and(?=[^\w])',formula)
        print(f"parts: {parts}")
        # Convert each part to DNF
        dnf_parts = [dnf(part) for part in parts] 
        print(f"dnf_parts: {dnf_parts}")
        # Combine the parts using the appropriate logical operator 
        if 'or' in formula:
            return " or ".join(parts) 
        elif 'and' in formula:
            return " and ".join(parts)


def cnf(formula):
    # Base case: If the formula is a literal, return it as is
    if re.fullmatch(r'[A-Z]|~[A-Z]', formula): return formula
    
    # Recursive case: If the formula is a compound statement, convert it to CNF
    if 'and' in formula or 'or' in formula:
        # Split the formula into its component parts
        parts = re.split(r'(?<=\()or(?=\))|(?<=\()and(?=\))', formula) # Convert each part to CNF
        # cnf_parts = [cnf(part) for part in parts]
        # Combine the parts using the appropriate logical operator
        if 'and' in formula:
            return " and ".join(parts)
        elif 'or' in formula:
            return " or ".join(parts)

# Example usage
formula = "(A and B) or C or D"
cnf_formula = cnf(formula)
dnf_formula = dnf(formula)
print(cnf_formula) # Outputs: "A and B or C and D or"
print("Hello")
print(dnf_formula) # Outputs: "A and B or C and D or"