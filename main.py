import sys

from stats import wc, charcount, ordered

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    numWords = wc(get_book_text(f'{sys.argv[1]}'))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {numWords} total words")
    print("--------- Character Count -------")
    dictionary = (ordered(charcount(get_book_text(f'{sys.argv[1]}'))))
    
    for i in dictionary:
        print(f"{i['char']}: {i['num']}")

    print("============= END ===============")

main()
