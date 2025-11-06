def is_safe(assignment, var, value, constraints):
for neighbor in constraints[var]:
if neighbor in assignment and assignment[neighbor] == value:
return False
return True

def backtrack(variables, domains, constraints, assignment):
if len(assignment) == len(variables):
return assignment # All variables assigned

var = [v for v in variables if v not in assignment][0]

for value in domains[var]:
if is_safe(assignment, var, value, constraints):
assignment[var] = value
result = backtrack(variables, domains, constraints, assignment)
if result:
return result
del assignment[var] # backtrack
return None

def main():
variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']

domains = {
'WA': ['Red', 'Green', 'Blue'],
'NT': ['Red', 'Green', 'Blue'],
'SA': ['Red', 'Green', 'Blue'],
'Q': ['Red', 'Green', 'Blue'],

'NSW': ['Red', 'Green', 'Blue'],
'V': ['Red', 'Green', 'Blue'],
'T': ['Red', 'Green', 'Blue']
}

constraints = {
'WA': ['NT', 'SA'],
'NT': ['WA', 'SA', 'Q'],
'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
'Q': ['NT', 'SA', 'NSW'],
'NSW': ['Q', 'SA', 'V'],
'V': ['SA', 'NSW'],
'T': []
}

assignment = {}
solution = backtrack(variables, domains, constraints, assignment)

if solution:
print("Solution Found:")
for state, color in solution.items():
print(f"{state} → {color}")
else:
print("No solution exists.")

if __name__ == "__main__":
main()

