def word_counter(text):
        word_list = text.split()
        return len(word_list)

def char_counter(text):
	char_count = {}
	lowered_txt = text.lower()
	for c in lowered_txt:
		if c not in char_count:
			char_count[c] = 1
		else: char_count[c] += 1

	return char_count

def sort_count(dictionary):

	list = []

	for char in dictionary:
		count = dictionary[char]

		if char.isalpha() == True:
			list.append({"char":char,"num":count})

		else: continue

	list.sort(reverse=True, key=sort_on)

	return list

def sort_on(items):
	return items["num"]
