def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False

    table = {}
    matched = 0
    for char in str1:
        if char in table:
            table[char] += 1
        else:
            table[char] = 1
            matched += 1

    for char in str2:
        if char in table:
            table[char] -= 1
            if table[char] == 0:
                matched -= 1
        else:
            return False

    return matched == 0


print(is_permutation('foo', 'oof'))  # True
