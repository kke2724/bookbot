def word_counter(text):
        word_list = text.split()
        return len(word_list)
"""
Function that takes in a string, splits it into a list of strings separated by space,
then return the length of the words in the new list.
"""

def char_counter(text):
	char_count = {} 			  # Creates a blank dictionary.
	lowered_txt = text.lower()    # Lowers all alphabetical chars from the input.
	
	for c in lowered_txt:		  # For every char in the now lowered string,
		if c not in char_count:	  # If the current char doesn't exist in the char_count dict,
			char_count[c] = 1	  # then add the char in it as a key with a value of 1.
		else: char_count[c] += 1  # Else, increment the value of that char (key) in the dict.

	return char_count			  # Returns updated dict with unique chars and its counts.
"""
Function that takes in a string, lowers the characters, and returns the count of characters.
"""

def sort_count(dictionary):
	list = []										# Creates a blank list.

	for char in dictionary:							# For each entry in the dict (combination of key and value, i.e. {'e': 38})
		count = dictionary[char]					# Creates a variable that holds the value of a key of the current index.
		if char.isalpha():							# If the current key is an alphabetical char,
			list.append({"char":char,"num":count})	# append the combination of the char (key) and its count (value) as a dict item
													# into 'list', specifically defining the name of the key and its value as "char" and "num", respectively.
		else: continue								# If it's not an alphab char, then ignore the if-block and move onto the next index of the for-loop.
	
	list.sort(reverse=True, key=lambda char: char["num"])
	# Sorts the now updated 'list' into an ascending order (due to reverse) but sorted on "num" element of each item.
	"""
	NOTE 1: key=lambda x: x[y]
				- 'key' is a default condition to select which to base the sorting on.
				- 'lambda' is a Python function that directs the 'key' to a specific part of a list.
				- 'char:' after lambda is a temp. variable used to refer to an item in a list.
				-  char["num"] is the sorting specification. It could be used with indexes, i.e. char[0], char[2], etc.
	NOTE 2: <list>.sort() sorts a list in a descending order (from lowest to greatest) or in an alphabetical order by default.
	"""
	return list										# Returns the sorted 'list'.

"""
Function that takes in a dictionary, lowers the characters, and returns the count of characters.
"""

def common_word_counter(text):  # Function that counts the top 20 commonly appeared words in a book.

	lowered_text = text.lower() # Lowers all characters of the input.

	dict_word_count = {} 		# Creates an empty dict.

	list_avoid = [				# Creates a list of common prepositions and conjunctions to be ignored in the count.
		"am", "an", "and", "are", "as", "at", "be", "but", "by", "can", "cannot", "do",
		"each", "for", "from", "had", "has", "hasnt", "have", "he", "her", "hers", "him",
		"his", "i", "ie", "if", "in", "into", "is", "it", "its", "may", "me", "must", "my",
		"not", "of", "on", "or", "our", "ours", "ourselves", "she", "so",	"such",	"the",
		"their", "them", "themselves", "they", "this", "that", "to", "us", "was", "we",
		"were", "what", "when", "where", "which", "who", "why", "will", "you", "your",
		"yours", "ye", "thou", "did", "does", "having", "shall", "with", "mr", "ms", "mrs",
		"all", "been", "could", "would", "should", "no", "very", "said", "there", "here",
		"than", "much", "more", "less", "any"
	]

	list_cleaned_text = []						# Creates an empty list.

	for char in lowered_text:					# For each char in the 'lowered_text',
		if char.isalpha():						# if the char is alphabetical, then
			list_cleaned_text.append(char)		# append the char into the list created above.
		else:									# otherwise if it's not alphabetical,
			list_cleaned_text.append(' ')		# append it as a blank.

	processed_text = "".join(list_cleaned_text)	# Creates string that holds all words without numerical or special characters.

	word_list = processed_text.split()			# Splits the above string into a list.

	for w in word_list:							# For each word in the 'word_list',
		if w in list_avoid or len(w) == 1:		# if the current word is in the 'list_avoid' or if is a single character,
			continue							# skip this if-block.
		else:
			dict_word_count[w] = dict_word_count.get(w, 0) + 1
		"""
		Otherwise, within the dict that was created earlier in this function ('dict_word_count'),
		append a key into it, key being the current word (w), and the value being 1.

		NOTE: The .get() or <dictionary>.get(<key>, 'default value if not found') is a Python method to retrieve a value from a dictionary.
		It prevents a program from crashing with a KeyError if the key you're looking for isn't in the dictionary and returns an arbitrary value instead. 
		"""

	list_sorted_word_count = sorted(dict_word_count.items(), key=lambda item: item[1], reverse=True)
	"""
	1. Creates a new list.
		NOTE: 'sorted()' always returns a list.
	
	2. The list is populated by contents of a dictionary called 'dict_word_count' each of which are accessed as a pair of (key, value) tuple.
		NOTE: <dictionary>.items() makes a dictionary iterable and accessible as tuples so that BOTH components of each dict entry (key, value)
		can be referenced and called-in TOGETHER.

		Example:
			active_quests = {
				"Retrieve Ancient Scroll": "60% Complete",
				"Defeat the Goblin King": "Not Started",
				"Gather 5 Moonpetal Flowers": "3/5 Collected",
				"Help the Village Elder": "Completed"
			}

			print("\nYour Active Quests:")
			for quest_title, progress in active_quests.items():
				print(f"Quest: '{quest_title}' - Status: {progress}")

			# Output:
			# Your Active Quests:
			# Quest: 'Retrieve Ancient Scroll' - Status: 60% Complete
			# Quest: 'Defeat the Goblin King' - Status: Not Started
			# Quest: 'Gather 5 Moonpetal Flowers' - Status: 3/5 Collected
			# Quest: 'Help the Village Elder' - Status: Completed
	
	3. key=lambda item: item[1] points to the 2nd index of each items in the tuple (in our case, the count of words)

	4. reverse=True: Allows the sort to be in an ascending order.
	If this option is removed, by default, the list will be sorted in a ascending order.
	"""
	
	return list_sorted_word_count	# Returns the word count sorted by count in a descending order as a list.
