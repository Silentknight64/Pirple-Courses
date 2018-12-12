"""
Homework #3 If Statements
"""

# Compares the values, returns true if 2 of them are equal, false otherwise
def equality(a, b, c):
	# Converts all values to ints in case they are passed in as strings
	a = int(a)
	b = int(b)
	c = int(c)

	if a == b or a == c or b == c:
		return True
	else:
		return False 