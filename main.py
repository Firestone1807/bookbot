import sys
if len(sys.argv) == 2: 
    from stats import get_num_words
    from stats import count_letters
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)