# Python Data Structures

Progress is tracked in [study-log.md](../../progress/study-log.md).

---

## Lists

**Q: What is a list in Python?**
An ordered, mutable collection of items. Items can be of any type, duplicates are allowed, and each item is accessed by its index position starting from zero.

### Covered in [lists.py](lists.py)

```python
nums = [10, 20, 30, 20]   # create a list (duplicates allowed)
nums.append(40)           # add to the end -> [10, 20, 30, 20, 40]
nums[3] = 40              # update by index (mutable) -> [10, 20, 30, 40, 40]
nums[4] = 50              # update last item -> [10, 20, 30, 40, 50]
```

### Key Points
- Ordered: items keep their insertion order.
- Mutable: items can be changed in place.
- Indexing starts at 0.
- `append()` adds an item at the end; assigning by index only works for positions that already exist.

### Common Mistakes
- Assigning to an index that doesn't exist raises `IndexError: list assignment index out of range`. Use `append()` to grow a list. Note that `nums[4] = 50` in `lists.py` only works because `nums.append(40)` ran first, so index 4 exists.

### Still To Cover
- Negative indexing and slicing
- `insert`, `extend`, `remove`, `pop`, `sort`, `reverse`
- List comprehensions
- Copying lists (shallow vs deep)

---

## Tuples

**Q: What is a tuple in Python?**
An ordered, immutable collection of items. Once created, its elements cannot be added, removed, or changed. Duplicates are allowed.

### Covered in [tuples.py](tuples.py)

```python
coords = (3, 4)
x, y = coords        # unpacking -> x = 3, y = 4
print(coords[1])     # indexing works -> 4
# coords[0] = 9      # TypeError: tuples are immutable
# coords.append(5)   # AttributeError: no append on tuples
single = (7,)        # trailing comma -> a tuple
not_tuple = (7)      # no comma -> just the int 7
```

### Key Points
- Ordered and immutable.
- Unpacking assigns each element to a variable.
- A one-item tuple needs a trailing comma: `(7,)`.

### Common Mistakes
- `(7)` is an `int`, not a tuple. The comma makes the tuple, not the parentheses.
- Trying to modify a tuple raises `TypeError`.

### Still To Cover
- Tuples as dictionary keys / set members (hashable)
- Tuple vs list: when to use which
- Named tuples

---

## Sets

**Q: What is a set in Python?**
An unordered, mutable collection of unique items. Items can be any (hashable) type, but duplicates are not allowed.

### Covered in [sets.py](sets.py)

```python
unique_nums = {10, 20, 30, 20}   # duplicate 20 is dropped -> {10, 20, 30}
unique_nums.add(40)              # add an item -> {10, 20, 30, 40}
unique_nums.discard(20)          # remove if present, no error if missing -> {10, 30, 40}
```

### Key Points
- Unordered: no indexing, and the print order isn't guaranteed.
- Unique: duplicates are removed automatically.
- Mutable: items can be added and removed.
- `discard()` is safe if the item is missing; `remove()` raises `KeyError`.

### Common Mistakes
- `{}` creates an empty dict, not an empty set. Use `set()`.

### Still To Cover
- Union, intersection, difference
- Membership test speed (average O(1))
- Removing duplicates from a list with `set()`
- Sets of unhashable items (why lists can't be members)

---

## Dictionaries

_Not started yet._
