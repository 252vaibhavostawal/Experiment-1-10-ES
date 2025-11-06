import itertools 
def solve_cryptarithmetic(equation): 
""" 
Solves a cryptarithmetic puzzle. 
e.g., "SEND + MORE = MONEY" 
""" 
# Split the equation into left-hand side (LHS) and right-hand side (RHS)  
lhs_str, rhs_str = equation.lower().replace(' ', '').split('=') 
lhs_words = lhs_str.split('+') 
# Collect all unique letters in the puzzle 
letters = set()
for char in word: 
letters.add(char) 
for char in rhs_str: 
letters.add(char) 
letters = list(letters) 
# Identify the first letters of each word (cannot be zero) 
first_letters = {word[0] for word in lhs_words}.union({rhs_str[0]}) 
# Generate all possible permutations of digits for the letters 
digits = range(10) 
for perm in itertools.permutations(digits, len(letters)): 
mapping = dict(zip(letters, perm)) 
# Check if any first letter is mapped to zero 
if any(mapping[char] == 0 for char in first_letters): 
continue 
# Evaluate the LHS and RHS with the current mapping 
try: 
lhs_value = sum(word_to_int(word, mapping) for word in lhs_words)  rhs_value = word_to_int(rhs_str, mapping) 
# If the equation holds true, print the solution 
if lhs_value == rhs_value: 
print(f"Solution found for '{equation}':") 
for letter, digit in mapping.items(): 
print(f" {letter} = {digit}") 
print(f" {lhs_value} = {rhs_value}") 
return True # Found a solution, exit 
except KeyError: 
# This can happen if a letter in the equation isn't in 'letters', 
# but our setup ensures all letters are included. 
pass 
print(f"No solution found for '{equation}'.") 
return False 
def word_to_int(word, mapping): 
"""Converts a word to its integer value based on the letter-digit mapping.""" 
 value = 0 
for char in word: 
value = value * 10 + mapping[char] 
return value 
# Example usage: 
solve_cryptarithmetic("SEND + MORE = MONEY") 
