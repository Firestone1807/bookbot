import sys

def get_num_words(path):
    with open(path) as f:
        file_contents = f.read()
        file_contents = len(file_contents.split())
    return file_contents

def count_letters(path):
    letter_dict = {}
    with open(path) as f:
        file_contents = f.read()
        file_contents = file_contents.lower()
    for letter in file_contents:
        if letter not in letter_dict:
            letter_dict[letter] = 1
        elif letter in letter_dict:
            letter_dict[letter] += 1
    return letter_dict

def sort_results(num, counts, path):
    print(f"============ BOOKBOT ============\nAnalyzing book found at {path}...\n----------- Word Count ----------\nFound {num} total words\n--------- Character Count -------")
    for key in counts:
        print(f"{key}: {counts[key]}")




value1 = get_num_words(sys.argv[1])
value2 = count_letters(sys.argv[1])
sort_results(value1, value2, sys.argv[1])