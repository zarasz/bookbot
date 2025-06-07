def count_words(text):
    return len(text.split())

def count_chars(text):
    map = {}
    for char in text:
        lchar = char.lower()
        if not lchar in map:
            map[lchar] = 0
        map[lchar] += 1
    return map

def sort_on(dict):
    return dict["num"]

def parse_char_dict(chars):
    list = []
    for char in chars:
        list.append({"char": char, "num": chars[char]})

    list.sort(key=sort_on, reverse=True)
    return list
            