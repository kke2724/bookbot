import sys
from stats import word_counter
from stats import char_counter
from stats import sort_on
from stats import sort_count
from stats import common_word_counter

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
	print()
	print(f"Analyzing book found at {book_path}...")
	print()
	print("----------- Word Count ----------")
	print()

	text = get_book_text(f"{book_path}")

	num_words = word_counter(text)

	print(f"Found {num_words} total words.")
	print()
	print("--------- Top 20 Common Words -------")
	print()

	sorted_word_count = common_word_counter(text)

	for word, count  in sorted_word_count[:20]:
		print(f"{word}: {count}")

	print()
	print("--------- Character Count -------")
	print()

	dict_num_chars = char_counter(text)

	list_sorted = sort_count(dict_num_chars)

	for dict in list_sorted:
		print(f"{dict["char"]}: {dict["num"]}")

	print()
	print("============= END ===============")

main()
