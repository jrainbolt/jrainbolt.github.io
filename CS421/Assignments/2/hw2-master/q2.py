# CS421: Natural Language Processing
# University of Illinois at Chicago
# Fall 2020
# Assignment 2
#
# Do not rename/delete any functions or global variables provided in this template and write your solution
# in the specified sections. Use the main function to test your code when running it from a terminal.
# Avoid writing that code in the global scope; however, you should write additional functions/classes
# as needed in the global scope. These templates may also contain important information and/or examples
# in comments so please read them carefully. If you want to use external packages (not specified in
# the assignment) then you need prior approval from course staff.
# This part of the assignment will be graded automatically using Gradescope.
# =========================================================================================================

import re



# Function to split a piece of text into sentences
# Arguments:
# text: A string containing input text
# Returns: sents (list)
# Where, sents (list) is a list of sentences that the text is split into
# Note that while this function works for most cases, it does not work in all scenarios;
# Can you think of any exceptions?
def get_sents(text):
	
	sents = re.split("[\n\.!?]", text)
	sents = list(filter(len, [s.strip() for s in sents]))
	return sents


# Function to split a sentence into a list of words
# Arguments:
# sent: A string containing input sentence
# Returns: words (list)
# Where, words (list) is a list of words that the sentence is split into
# Note that while this function works for most cases, it does not work in all scenarios;
# Can you think of any exceptions?
def get_words(sent):
	
	words = re.split(r"[^A-Za-z0-9-]", sent)
	words = list(filter(len, words))
	return words


# Function to get unigram counts
# Arguments:
# text: A string containing input text (may have multiple sentences)
# Returns: unigrams (dict)
# Where, unigrams (dict) is a python dictionary countaining lower case unigrams (words) as keys and counts as values
# Make sure that you convert all unigrams to lower case while counting e.g. "Police" and "police" are counted as the same unigram "police"
# You should use get_sents and get_words function to get sentences and words respectively, do not use any other tokenization mechanisms
def get_unigram_counts(text):
	# [Your code here]
	unigram = {}

	for token in text:
		unigram.add(token)

	# For sentence "If Police Police police police, who polices the Police Police?" it should return
	return {unigram}


# Function to get bigram counts
# Arguments:
# text: A string containing input text (may have multiple sentences)
# Returns: bigrams (dict)
# Where, unigrams (dict) is a python dictionary countaining lower case bigrams as keys and counts as values.
# Bigram keys must be formatted as two words separated by an underscore character
# For example, the bigram "Red car" is represented as "red_car" and the "Dark Horse" as "dark_horse"
# You should also respect the sentence boundaries, for example in the following text:
# "Can't repeat the past?... Why of course you can!", past_why should not be a bigram since there is
# a sentence boundary between the two words.
# Make sure that you convert all bigrams to lower case while counting e.g. "RED Car" and "red car" are counted as the same bigram "red_car"
# You should use get_sents and get_words function to get sentences and words respectively, DO NOT use any other tokenization mechanisms
def get_bigram_counts(text):
	# [Your code here]

	# For sentence "Old red car. Speeding.", it should return
	return {'old_red': 1, 'red_car': 1}


# Use the main function to test your code when running it from a terminal
# Sample code is provided to assist with the assignment, feel free to change/remove it if you want
# You can run the code from termianl as: python3 q5.py
# It should produce the following output:
#
# $ python3 q5.py
# First sentence: Gatsby believed in the green light, the orgastic future that year by year recedes before us
# Second sentence: It eluded us then, but that’s no matter-tomorrow we will run faster, stretch out our arms farther
# Words in first sentence: ['Gatsby', 'believed', 'in', 'the', 'green', 'light', 'the', 'orgastic', 'future', 'that', 'year', 'by', 'year', 'recedes', 'before', 'us']
# Unigram counts: {'police': 6, 'polices': 1, 'if': 1, 'who': 1, 'the': 1}
# Bigram counts: {'big_red': 1, 'red_car': 1}

def main():
	# Given an input text
	#text = """  Gatsby believed in the green light, the orgastic future that year by year recedes before us.
      #          It eluded us then, but that’s no matter-tomorrow we will run faster, stretch out our arms farther...
       #         And then one fine morning... So we beat on, boats against the current, borne back ceaselessly into the past."""
	
	text = open("ats.txt")
	#print(text.read())

	# We can convert it into a list of sentences using get_sents function
	sents = get_sents(text)
	print("First sentence: {0}".format(sents[0]))
	print("Second sentence: {0}".format(sents[1]))

	# Any sentence can then be converted into a list of wrods using get_words function
	words = get_words(sents[0])
	print("Words in first sentence: {0}".format(words))

	# Get unigram counts as
	counts = get_unigram_counts(text)
	print("Unigram counts: {0}".format(counts))


	#counts = get_bigram_counts(text)
	#print("Bigram counts: {0}".format(counts))

	print("closing file now")
	text.close()
	return 0


################ Do not make any changes below this line ################
if __name__ == '__main__':
	exit(main())
