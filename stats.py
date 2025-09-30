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

def common_word_counter(text):

	lowered_text = text.lower()

	dict_word_count = {}

	list_avoid = [
		"a", "about", "above", "across", "after", "afterwards", "again", "against",
		"all", "almost", "alone", "along", "already", "also", "although", "always",
		"am", "among", "amongst", "amount", "an", "and", "another", "any", "anyhow",
		"anyone", "anything", "anyway", "anywhere", "are", "around", "as", "at", "back",
		"be", "became", "because", "become", "becomes", "becoming", "been", "before",
		"beforehand", "behind", "being", "below", "beneath", "beside", "besides", "between",
		"beyond", "both", "bottom", "but", "by", "call", "can", "cannot", "could", "co",
		"con", "couldnt", "de", "describe", "detail", "do", "done", "down", "due", "during",
		"each", "eg", "eight", "either", "eleven", "else", "elsewhere", "empty", "enough", "etc",
		"even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen",
		"fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty",
		"found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has",
		"hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon",
		"hers", "herself", "him", "himself", "his", "how", "however", "hundred", "i", "ie",
		"if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself",
		"keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may",
		"me", "meanwhile", "might", "mine", "more", "moreover", "most", "mostly", "move", "much",
		"must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next",
		"nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere",
		"of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others",
		"otherwise", "our", "ours", "ourselves", "out", "over", "own", "part", "per", "perhaps",
		"please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems",
		"serious", "several", "she", "should", "show", "side", "since", "six", "sixty", "so",
		"some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still",
		"such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves",
		"then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon",
		"these", "they", "thick", "thin", "third", "this", "those", "though", "three", "through",
		"throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards",
		"twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very",
		"via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever",
		"where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever",
		"whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose",
		"why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours",
		"yourself", "yourselves", "ye", "thou", "did", "does", "having", "shall"
	]

	list_cleaned_text = []

	for char in lowered_text:
		if char.isalpha():
			list_cleaned_text.append(char)
		else:
			list_cleaned_text.append(' ')

	processed_text = "".join(list_cleaned_text)

	word_list = processed_text.split()

	for w in word_list:
		if w in list_avoid or len(w) == 1:
			continue
		else:
			dict_word_count[w] = dict_word_count.get(w, 0) + 1

	sorted_word_count = sorted(dict_word_count.items(), key=lambda item: item[1], reverse=True)

	return sorted_word_count
