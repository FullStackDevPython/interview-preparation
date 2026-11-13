"""
Check if a string is a palindrome.
"""
palindrome = "MOM,wow,nitin,"
s="racecar"
def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    print(s ,"==", s[::-1])
    return s == s[::-1]
          

print(is_palindrome(s))  # Output: True

# s[start:stop:step] slicing the string
# s[included:excluded:step]