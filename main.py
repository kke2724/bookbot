import sys
from stats import word_counter
from stats import char_counter
from stats import sort_on
from stats import sort_count

def get_book_text(filepath):
	with open(filepath) as fp:
		return fp.read()

def main():
	if len(sys.argv) == 1:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		book_path = sys.argv[1]

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	print("----------- Word Count ----------")

	text = get_book_text(f"{book_path}")

	num_words = word_counter(text)

	print(f"Found {num_words} total words.")
	print("--------- Character Count -------")

	dict_num_chars = char_counter(text)

	list_sorted = sort_count(dict_num_chars)

	for dict in list_sorted:
		print(f"{dict["char"]}: {dict["num"]}")

	print("============= END ===============")

main()
