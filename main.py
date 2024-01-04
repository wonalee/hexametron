import sys
"""
rules
    1. A foot can be made up of two long syllables (– –), a spondee; or a long and two short syllables, a dactyl (– υ υ).
    2. The first four feet can contain either one of them.
    3. The fifth is almost always a dactyl, and last must be a spondee/trochee (together forming an adonic). Exceptions can occur when a polysyllabic (especially Greek) name ends a verse.
"""

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
	print(line)
	# analyze
	# next: look at greek.py
