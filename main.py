def permutation_substring_search(pattern, test):
    result = []
    pattern_char_countdown = {}
    matched = 0
    pattern_size = len(pattern)
    test_size = len(test)

    for char in pattern:
        if char in pattern_char_countdown:
            pattern_char_countdown[char] += 1
        else:
            pattern_char_countdown[char] = 1
            matched += 1

    for i in range(pattern_size):
        if test[i] in pattern_char_countdown:
            pattern_char_countdown[test[i]] -= 1
            if pattern_char_countdown[test[i]] == 0:
                matched -= 1

    if matched == 0:
        result.append(0)

    for i in range(pattern_size, test_size):
        if test[i - pattern_size] in pattern_char_countdown:
            if pattern_char_countdown[test[i - pattern_size]] == 0:
                matched += 1
            pattern_char_countdown[test[i - pattern_size]] += 1

        if test[i] in pattern_char_countdown:
            pattern_char_countdown[test[i]] -= 1
            if pattern_char_countdown[test[i]] == 0:
                matched -= 1

        if matched == 0:
            result.append(i - pattern_size + 1)

    return tuple(result)


print(permutation_substring_search(
    "abc", "cdbcadbcadbacdcabcdcabdcabdacbdcacbdcabdadcacbdcbadcabdcadcbd"))
