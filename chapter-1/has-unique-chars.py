def has_unique_chars(str):
    seen = {}
    for char in str:
        if char in seen:
            return False
        else:
            seen[char] = True
    return True


print(has_unique_chars('foo'))  # False
print(has_unique_chars('bar'))  # True
print(has_unique_chars('baz'))  # True
