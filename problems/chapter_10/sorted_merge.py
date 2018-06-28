"""Sorted Merge.
		You are given two sorted arrays A and B where A has a large enough buffer at
		the end to hold B. Write a method to merge B into A in sorted order.
		Thoughts:
		- well, we know mergesort does exactly this in it's merge function, so we
		can use that as a starting point.
"""

def merge(a, b):
	if a[-1] > b[0]:
		return -1
	a_pointer = len(b)  # start a_pointer at the first None element.
	for i in range(len(b)):
		a[a_pointer] = b[i]
		a_pointer += 1
	return a


def main():
	# Contrived; in python we can just call append() on a list.
	a = [1, 2, 3, 4, None, None, None, None]
	b = [5, 6, 7, 8]
	expected = [1, 2, 3, 4, 5, 6, 7, 8]
	got = merge(a, b)
	assert expected == got

	a = [5, 6, 7, 8,]
	b = [1, 2, 3, 4,]
	expected = -1
	got = merge(a, b)
	assert expected == got

if __name__ == '__main__':
	main()