# Python Basics

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
