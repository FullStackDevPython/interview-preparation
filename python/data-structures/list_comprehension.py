"""
Q: What is list comprehension in Python?
A: List comprehension is a compact way to create new lists in Python. 
It allows you to generate a new list by applying an expression to each item in an existing iterable 
(like a list, tuple, or string) and optionally filtering the items based on a condition.
It replaces the need for using loops and the append() method to build a new list.
Basic syntax of list comprehension is:
new_list = [expression for item in iterable if condition]
"""

# Example
squares = []
for i in range(10):
    squares.append(i**2)
print(squares)

# Using list comprehension
squares = [i**2 for i in range(10)]
print(squares)

even_numbers = [i for i in range(20) if i % 2 == 0]
print(even_numbers)

odd_numbers = [i for i in range(20) if i % 2 != 0]
print(odd_numbers)

labels = ['even' if i % 2 == 0 else 'odd' for i in range(10)]
print(labels)



pairs = []
for x in [1, 2, 3]:
    for y in ['a', 'b', 'c']:
        pairs.append((x, y))
print(pairs)

pairs = [(x, y) for x in [1, 2, 3] for y in ['a', 'b', 'c']]
print(pairs)