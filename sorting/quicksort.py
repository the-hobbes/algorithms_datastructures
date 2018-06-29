"""Quick sort.
		Runtime: O(n log n) average, O(n^2) worst case. Memory is O(n log n). 
		- Pick a pivot element from the array.
		Walk through the array, swapping elements around such that all elements < 
		pivot come before all elements > pivot.
		- Repeat the process, appliying it to the left and right portions around the 
		pivot.
		Good visual explanation: https://www.youtube.com/watch?v=aQiWF4E8flQ
"""

def partition(data, left_pointer, right_pointer):
	"""Partition a list.
			Compare the pivot point to each element in the list.
			Divider, the first element in the list to begin with. Once we find an 
			element in the list thats less than the pivot, we swap that into the
			divider.
			Results in two lists: one greater than the pivot point, and  one less.
	"""
	dividing_point = left_pointer
	pivot = right_pointer

	# Compare the pivot to every element in the list
	for i in range(left_pointer, right_pointer):
		if data[i] < data[pivot]:
			# We need to swap the current element with the dividing point.
			data[i], data[dividing_point] = data[dividing_point], data[i]
			# We've swapped, so we need to increment dividing point to point to the
			# next element in the list.
			dividing_point += 1

	# We've compared and swapped all the elements in the parition. Take the pivot
	# and swap it with wherever the divider is right now.
	data[pivot], data[dividing_point] = data[dividing_point], data[pivot]
	# Return the new pivot point, which is the dividing point.
	return dividing_point  


def _QuickSort(data, left_pointer, right_pointer):
	"""Quicksort."""
	if left_pointer >= right_pointer:
		# Base case: one element left.
		return
	index = partition(data, left_pointer, right_pointer)
	# Call quicksort on both sides of the partition.
	_QuickSort(data, left_pointer, index - 1)  # left partition
	_QuickSort(data, index + 1, right_pointer)  # right partition

def QuickSort(data):
	left_pointer = 0
	right_pointer = len(data) - 1
	_QuickSort(data, left_pointer, right_pointer)

def main():
	data = [5, 4, 2, 1, 6 , 8, 7, 3, 0, 9]
	expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	QuickSort(data)
	assert expected == data


if __name__ == '__main__':
	main()
