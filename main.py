from stats import *
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1) 

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(total_word_count(sys.argv[1]))
    print("--------- Character Count -------")
    sorted_list = sorted_chars(sys.argv[1])
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


    #print(get_book_text(sys.argv[1]))
    #print(total_char_appearance(sys.argv[1]))


main()

