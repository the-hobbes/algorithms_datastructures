"""Binary search.
		Locate an element in a sorted array. 
		Compare element x to the midpoint of the array. if x is > the midpoint, then
		search the right half of the array. If x < the midpoint, we search the left
		half of the array. If x == midpoint, then we return true. Repeat this
		process until we've located the element or are searching lists of length 1.
"""

def BinarySearch(data, searchterm):
	midpoint = int(len(data) / 2)
	if data[midpoint] == searchterm:
		return True
	if len(data) <= 1:
		# Our list is 1 element long, but we haven't found the term after the check.
		return False
	elif searchterm > midpoint:
		BinarySearch(data[midpoint:], searchterm)
	else:
		BinarySearch(data[:midpoint], searchterm)


def main():
	data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	searchterm = 8
	expected = True
	got = BinarySearch(data, searchterm)
	assert got == expected

	data = [1, 2, 3, 4, 5, 6, 7, 9]
	expected = False
	got = BinarySearch(data, searchterm)
	assert got == expected

	data = []
	expected = False
	got = BinarySearch(data, searchterm)
	assert got == expected
