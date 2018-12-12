"""
Homework #4 Lists
"""

myUniqueList = []
myLeftovers = []

def add(value):
	global myUniqueList
	global myLeftovers

	if value not in myUniqueList:
		myUniqueList.append(value)
		return True
	else:
		myLeftovers.append(value)
		return False

print(add("hi"))
print(add("hi"))
print(add(44))