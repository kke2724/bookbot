import sys
from stats import word_counter
from stats import char_counter
from stats import sort_count
from stats import common_word_counter

def get_book_text(filepath):
	with open(filepath) as fp:
		return fp.read()
"""
Function that takes in a file path (of a book in .txt file) and returns the entire content as as tring.
"""

def main():												# Within the root of this file, this program expects a user to input python3 main.py <path_to_book>.
	if len(sys.argv) == 1:								# If a user entered just the main.py with no file path,
		print("Usage: python3 main.py <path_to_book>")	# the program throws this error message then
		sys.exit(1)										# exits the program.
	else:
		book_path = sys.argv[1]							# Assigns the file path to 'book_path' var.

	print("============ BOOKBOT ============")
	print(f"\nAnalyzing book found at {book_path}...")
	print("\n----------- Word Count ----------")

	text = get_book_text(f"{book_path}")				# Assigns the entire .txt file data as a string to 'text' var.

	num_words = word_counter(text)						# Runs 'text' through the 'word_counter' function and assigns the count of words into 'num_words' var.

	print(f"\nFound {num_words} total words.")
	print("\n--------- Top 20 Common Words -------")

	list_sorted_word_count = common_word_counter(text)	# Assigns a list of pair of (word, count) to a 'list_sorted_word_count' var.

	for word, count in list_sorted_word_count[:20]:		# For each word and count in the above list (up to 20),
		print(f"\n{word}: {count}")						# print each items.

	print("\n--------- Character Count -------")

	dict_num_chars = char_counter(text)					# Assigns a dict of pair of (char, count) to a 'dict_num_chars' var.

	list_sorted = sort_count(dict_num_chars)			# Assigns a list of pair of (char, count) but with only alphabetical chars.

	for dict in list_sorted:
		print(f"{dict["char"]}: {dict["num"]}")

	print("\n============= END ===============")

main()	# Triggers the main() function.
