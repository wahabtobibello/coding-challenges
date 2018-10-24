def is_palindrome(word):
    word_len = len(word)
    for i in range(word_len // 2):
        if word[i] != word[word_len - i - 1]:
            return False
    return True

print(is_palindrome('level'))
print(is_palindrome('levels'))