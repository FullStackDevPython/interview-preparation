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
    for i in range(len(keys)):
        print(i)
        result[a[i]] = b[i]
        print(result)
    return result

print(result)

print(merge_lists_to_dict(a,b))


a = ["a", "b", "a"]
b = [1, 2, 3]


def group_values(a,b):
    result2 = {}
    for i in range(len(a)):
        key = a[i]
        if key in result2:
            result2[key].append(b[i])
        else:
            result2[key] = [b[i]]
    return result2

print(group_values(a,b))

def group_values_with_defaultdict(a,b):
    from collections import defaultdict
    result3 = defaultdict(list)
    for i in range(len(a)):
        result3[a[i]].append(b[i])
    return dict(result3)

print(group_values_with_defaultdict(a,b))

def group_values_with_setdefault(a,b):
    result4 = {}
    for key, value in zip(a,b):
        result4.setdefault(key, []).append(value)
    return result4