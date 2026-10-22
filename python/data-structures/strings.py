"""
Q: What is a string in Python?
A string is an ordered immutable sequence of characters.
Immutable means that once a string is created, it cannot be changed.
One cannot change a character in a string,
Every change creates a new string object. 
Strings can be created using single quotes, double quotes, 
or triple quotes for multi-line strings.
"""

s = "Python"
print(s)
print(s[0])  # Accessing the first character
print(s[-1])  # Accessing the last character
print(s[0:4])  # Slicing the string
#s[included:excluded:step]
print(s[0:6:2])  # Slicing with a step
print(len(s))  # Length of the string
print(s[-1:0:-1])  # Reversing the string
print(s[::-1])  # Reversing the string using slicing

reverse = ''
for char in s:
    # print(char[0])
    print("sequence:", reverse)
    reverse = char + reverse
print(reverse)