from stats import count_words, count_chars, parse_char_dict


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    import sys
    if not (len(sys.argv) == 2):
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)


    path = sys.argv[1]
    book = get_book_text(path)
    wordcount = count_words(book)
    char_count = parse_char_dict(count_chars(book))
    

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    for entry in char_count:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry['num']}")

main()