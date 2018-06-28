"""Sparse search.
		Given a sorted array of strings that is interspersed with empty strings,
		write a method to find the location of a given string.
		Thoughts:
		- This would be straightforward if not for the empty strings; we could just
		use binary search. Instead, we can modify binary search to pick a non-empty
		index if we select an index for the midpoint that is empty.
		- We need to return the index of the found item, not just whether or not the
		item is present in the list.
"""
def midpoint(data):
	midpoint = int(len(data) / 2)
	if data[midpoint] != '':
		return midpoint
	num_elements_searched = 0
	while num_elements_searched <= len(data):
		midpoint = (midpoint + 1) % len(data)
		if data[midpoint] != '':
			return midpoint
		num_elements_searched += 1
	return -1

# def getMidpoint(data):
# 	midpoint = int(len(data) / 2)
# 	if data[midpoint] != '':
# 		return midpoint
# 	num_elements_searched = 0
# 	while num_elements_searched <= len(data):
# 		midpoint += 1 % (len(data))
# 		if data[midpoint] != '':
# 			return midpoint
# 		num_elements_searched += 1
# 	return -1

def sparseSearch(data, searchTerm):
	mid = midpoint(data)
	print len(data)  # this is 3
	print mid # this is 0. So it never hits a base case.
	if data[mid] == searchTerm:
		return mid
	if mid == -1 or len(data) <= 1:
		return -1
	elif searchTerm > data[mid]:
		# Search the right half.
		return sparseSearch(data[mid:], searchTerm)
	else:
		# Search the left half.
		return sparseSearch(data[:mid], searchTerm)


def main():
	# Remember, for binary search the array must be sorted.
	data = ['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', '']
	expected = 4
	got = sparseSearch(data, 'ball')
	assert got == expected

	expected = -1
	got = sparseSearch(data, 'hodor')
	assert got == expected
	# print midpoint(['', 'dad', '', '', '', '', '', '',])

if __name__ == '__main__':
	main()