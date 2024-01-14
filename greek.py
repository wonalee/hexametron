"""
somewhere down the line, if there is vowels,
diftongs becomes a concern

TODO:
- which diftongs do we have? (all of them)

def isDiftong(something?):
	#TODO
"""

def isGreekExtended(letter):
	# Checks if letter is within the Unicode Greek Extended block (polytonic orthography)
	return ord(letter) in range(0x1F00, 0x1FFF + 1)

def isGreekMonotonic(letter):
	# Checks if letter corresponds to monotonic orthography
	return ord(letter) in range(0x0386, 0x03CE + 1)

# TODO: is there a way to remove diacritics?
# 1. remove diacritics from all letters in greek extended block
# 2. there will be overlaps, but we have all our vowels from that
# 3. write tests to check if diacritic removal is working as we intend
def isGreekMonotonicVowel(letter):
	return letter in 'ΆΈΉΊΌΎΏΐΑΕΗΙΟΥΩΪΫάέήίΰαεηιουωϊϋόύώ'

def isVowel(letter):
	if isGreekExtended(letter):
		# Unicode Greek Extended is guaranteed to be a vowel
		return True
	elif isGreekMonotonic(letter) and isGreekMonotonicVowel(letter):
		return True

	# is not vowel
	return False
