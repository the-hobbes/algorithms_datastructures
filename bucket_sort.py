"""Bucket sort.
		Runtime: Best case, when data is distrubted between buckets perfectly, is
		O(n+k), where n is the length of the array and k is the number of buckets.
		Worst case is O(n^2), when all the elements are allocated to the same 
		bucket.

		In this algorithm, buckets are created to put elements into. Then, some
		sorting algorithm is applied to each bucket to sort the elements there.
		Finally, we combine all the elements in the buckets to get a sorted array.
"""

from collections import defaultdict

def InsertionSort(data):
	"""Sort like playing cards in your hand.
			Build the sorted array in-place, shifting elements out of the way if
			necessary to make room as you go.
			- Call the first element in the array "sorted".
			- Repeat until all are sorted:
				- Look at the next unsorted element, insert into the "sorted" portion by
				shifting the requisite number of elements.
	"""
	# The first thing we see is a 1 element array at position 0, so we skip it.
	for i in range(1, len(data)):
		# Set the element we are currently sorting aside.
		current_element = data[i]
		# Set its place in the array aside as well.
		index = i
		# While we haven't reached the beginning of the list and the position to the
		# left of the element we are currently sorting is larger than that 
		# element...
		while index > 0 and data[index - 1] > current_element:
			# Move the element in the current position over by 1. For example, if this
			# is the first pass, we move 54 into the position held by 26 (this is why
			# we need to set aside the current element, to save it as its location is
			# overwritten).
			data[index] = data[index - 1]
			# Move the pointer to the index over one to the left as well.
			index = index - 1
		# We've finished shifting everything over (we're out of the while loop), so
		# swap the saved element into the decremented index. For example on the 
		# first iteration, 26 goes into the 0th position of the list.
		data[index] = current_element

def BucketSort(data):
	sorted_list = []
	# Do this to avoid the multiple references to the same list you get with:
	# buckets = [] * len(data)
	# See https://bit.ly/2Mqfp9z
	buckets = [[] for _ in range(len(data))]
	# Distribute the elements to their buckets.
	for i in range(0, len(data)):
		index = int(data[i] * len(data)) % len(data)
		buckets[index].append(data[i])
	for x in range(0, len(buckets)):
		# Sort each subbucket.
		InsertionSort(buckets[x])
		for y in buckets[x]:
			# Add each element from the sorted subbucket to the final list.
			sorted_list.append(y)
	return sorted_list


def main():
	# Test insertion sort.
	data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
	expected = [17, 20, 26, 31, 44, 54, 55, 77, 93]
	InsertionSort(data)
	assert data == expected

	# Test bucket sort.
	# This data is poorly distributed.
	data = [5, 4, 2, 1, 6 , 8, 7, 3, 0, 9]
	expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	received = BucketSort(data)
	assert expected == received

	# This data is well distributed.
	data = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
	expected = [0.1234, 0.3434, 0.565, 0.656, 0.665, 0.897]
	received = BucketSort(data)
	assert expected == received

if __name__ == '__main__':
	main()
