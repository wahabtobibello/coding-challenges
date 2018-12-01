def urlify(str):
    urlified_str_arr = []
    for char in str:
        if char == ' ':
            urlified_str_arr.append('%20')
        else:
            urlified_str_arr.append(char)
    return ''.join(urlified_str_arr)


print(urlify('Mr John Smith'))
