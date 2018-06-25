"""MergeSort.
		Runtime: O(n log n). Memory depends.
		Efficient, recursive algorithm.   
		Divide the dataset in half and sort each half. Then, merge the
		sorted halves back together. Each of those halves has the same sorting 
		algorithm to it. Eventually, you are merging just two single-element arrays.
		Merge is the portion that does the heavy lifting in this algorithm.
"""

def merge(left, right):
	"""Merge each half.
			Create a pointer for each half, then run through each, comparing elements
			from the halves and adding them to the "merged" data structure in sorted
			order.

			Once we run out of elements in one of the halves, then append the 
			remaining elements to the merged list.
	"""
	merged = []
	left_index = 0
	right_index = 0
	while (left_index<len(left) and right_index<len(right)):
		if left[left_index] <= right[right_index]:
			# The left is the smaller (or equal) one, so add it to the merged array.
			merged.append(left[left_index])
			# Now move the left index up a spot.
			left_index += 1
		else:
			# The element at the right index must be bigger.
			merged.append(right[right_index])
			right_index += 1
	# Once we've compared all the elements in the left and right halves, its time
	# to move anything remaining in either of the halves into the merged list. The
	# indecies will already be incremented to their latest positions after the
	# comparison in the while() loop was made.
	merged += left[left_index:]
	merged += right[right_index:]
	return merged
	
def MergeSort(data):
	"""Recursive merge sort.
			Since [] is a mutable data structure we don't have to do the return calls,
			but it makes it easier to reason about the left and right sub lists.
	"""
	if len(data) <= 1:
		return data
	middle = int(len(data) / 2)
	left = MergeSort(data[:middle])
	right = MergeSort(data[middle:])
	return merge(left, right)


def main():
	data = [5, 4, 2, 1, 6 , 8, 7, 3, 0, 9]
	expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	received = MergeSort(data)
	assert expected == received

if __name__ == '__main__':
	main()
