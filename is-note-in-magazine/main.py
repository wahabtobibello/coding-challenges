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
                matched -= 0
    
    return matched == 0
            
        
