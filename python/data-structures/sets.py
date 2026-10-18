"""
Q : What is a set in Python?
Answer : A set is an unordered, mutable collection of unique items. 
Items can be any type, but duplicates are not allowed.
"""

unique_nums = {10, 20, 30, 20}
print(unique_nums)
unique_nums.add(40)
print(unique_nums)
unique_nums.discard(20)
print(unique_nums)


a = {1,2,2,3,4}
print(a)
b = {4,5,6,7}
print(b)

print(a | b) #union
print(a & b) #intersection
print(a - b) #difference
print(b-a)

empty = set()
print(type(empty))

empty2 ={}
print(type(empty2))