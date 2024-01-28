import sys
import string
from src.greek import isVowel
"""
rules
    1. A foot can be made up of two long syllables (– –), a spondee; or a long and two short syllables, a dactyl (– υ υ).
    2. The first four feet can contain either one of them.
    3. The fifth is almost always a dactyl, and last must be a spondee/trochee (together forming an adonic). Exceptions can occur when a polysyllabic (especially Greek) name ends a verse.
"""

def removePunctuation(s):
	mapping = str.maketrans('', '', string.punctuation)
	return s.translate(mapping)

file_names = []

if len(sys.argv) > 1:
	file_names = sys.argv[1:]
else:
	print("Input needed")
	exit(1)

with open(file_names[0], "r") as file:
	#for line in file:
	#	print("line", line)
	line = file.readline()
	print("first line", line)

	# run on all letters in that line
	line = removePunctuation(line)
	print('no punctuation:', line)

	vowel_checks = []
	for word in line.split():
		word_vowels = []
		for character in word:
			word_vowels.append(isVowel(character))
		vowel_checks.append(word_vowels)
		print(word)
		print(word_vowels)
		print('========')

	# start considering next step, diftongs


	# analyze
	# next: look at greek.py
