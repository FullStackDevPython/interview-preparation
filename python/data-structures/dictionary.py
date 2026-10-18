"""
What is a dictionary in Python?
A dictionary is a mutable collection of key value pairs. 
Each kay must be unique and hashable, and it is used to look up its value.
Since python 3.7, dictionary preserve insertion order

Each key must be unique and immutable,

"""

d = {
    "name" : "Bob",
    "age" : 25,
    "city" : "Nagpur"
}

print(d["name"])

print(d)
print(d)
d.get("city")
d.get("phone", "N/A")
