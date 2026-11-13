"""
Merge two lists into a dictionary in Python
"""

a = ["a", "b", "c"]
b = [1, 2, 3]
# c = dict(zip(a, b))
result={}

def merge_lists_to_dict(keys, values):
    if len(keys) != len(values):
        print("Keys and values lists must have the same length.")
        raise ValueError("Keys and values lists must have the same length.")
    for i in range(len(a)):
        print(i)
        result[a[i]] = b[i]
        print(result)
    return result

print(result)

print(merge_lists_to_dict(a,b))