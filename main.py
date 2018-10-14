def check_perm(pattern, test):
    result = []
    pattern_char_countdown = {}
    matched = 0
    s = len(pattern)
    b = len(test)

    for char in pattern:
        if char in pattern_char_countdown:
            pattern_char_countdown[char] += 1
        else:
            pattern_char_countdown[char] = 1
            matched += 1

    for i in range(s):
        if test[i] in pattern_char_countdown:
            pattern_char_countdown[test[i]] -= 1
            if pattern_char_countdown[test[i]] == 0:
                matched -= 1

    if matched == 0:
        result.append(0)

    for i in range(s, b):
        if test[i - s] in pattern_char_countdown:
            if pattern_char_countdown[test[i - s]] == 0:
                matched += 1
            pattern_char_countdown[test[i - s]] += 1

        if test[i] in pattern_char_countdown:
            pattern_char_countdown[test[i]] -= 1
            if pattern_char_countdown[test[i]] == 0:
                matched -= 1

        if matched == 0:
            result.append(i - s + 1)

    return tuple(result)


print(check_perm("abc", "cdbcadbcadbacdcabcdcabdcabdacbdcacbdcabdadcacbdcbadcabdcadcbd"))
