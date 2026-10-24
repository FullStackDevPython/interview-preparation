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

t = "  Python is a programming language.  "
print(t.strip())  # Removing leading and trailing whitespace
print(t.lstrip())  # Removing leading whitespace
print(t.rstrip())  # Removing trailing whitespace
print(t.upper())  # Converting to uppercase
print(t.lower())  # Converting to lowercase
print("a,b,c".split(','))  # Splitting the string into a list
print("apple,oranges,grapes".split(','))
op = " ".join(["Python", "is", "awesome"])
print(op)  # Joining a list of strings into a single string
print("Python is awesome".replace("awesome", "great"))  # Replacing a substring
t2=t.replace("is","an")
t2.strip()
print(t2)  # Printing the modified string
print(t2.find("P"))  # Finding the index of a substring
print(t.isalpha())  # Checking if all characters are alphabetic
print(t2.isdigit())  # Checking if all characters are digits
print("abc".isalpha())  # Checking if all characters are alphabetic
print("123".isdigit())  # Checking if all characters are digits

#f-strings (formatted string literals) are a way to embed expressions inside string literals, 
# using curly braces {}.

name, age = "John", 25
print("My name is john and I am 25 years old.")  # Old way of formatting strings
print(f"My name is {name} and I am {age} years old.")  # New way of formatting strings