def permutations(word):
    word_len = len(word)
    if word_len == 1:
        return [word]

    result = []
    first_char = word[0]
    perm_of_others = permutations(word[1:])
    for perm in perm_of_others:
        for i in range(word_len):
            result.append(perm[:i] + first_char + perm[i:])
    return result

print(permutations('tobiloba'))
