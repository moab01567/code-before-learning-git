def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(" ")
	return words

def sort_words(words):
	"""sorts the words"""
	return sorted(words)

def print_first_word(words):
	"""printing the first word after popping off."""
	word = words.pop(0)
	print(word)


def sort_sentence(sentence):
	"""takes in full sentence and return the sorted word"""
	sentence = break_words(sentence)
	return sort_words(sentence)

def print_first_and_last(sentence):
	"""print the first and last word of the sentens"""
	sentence_list = break_words(sentence)
	print_first_word(sentence_list)
	print_last_word(sentence_list)

