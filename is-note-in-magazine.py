def is_source(note, magazine):
    note_word_count = {}
    matched = 0
    for word in note:
        if word in note_word_count:
            note_word_count[word] += 1
        else:
            note_word_count[word] = 1
            matched += 1

    for word in magazine:
        if word in note_word_count:
            note_word_count[word] -= 1
            if note_word_count[word] == 0:
                matched -= 1
            if matched == 0:
                return True
    return False


print(is_source(['kill', 'you', 'i'],
                ['the', 'fashion', 'kill', 'will', 'the', 'industry', 'i', 'love', 'this', 'you', 'need', 'this']))
