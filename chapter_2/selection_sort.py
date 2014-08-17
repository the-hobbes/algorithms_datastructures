'''
	Selection sort, an in place comparision sort.
	o(n^2) 
	- inefficient like insertion sort on long lists
	- worse than insertion sort on small lists
'''

UNSORTED_ELEMENTS = [5, 2, 4, 6, 1, 3]
EXPECTED_RESULT = [1, 2, 3, 4, 5, 6]

def selection_sort():
	'''
		Find the smallest element in the unsorted sublist.
		Exchange that smallest element with the leftmost unsorted element in the list.
		Move the sublist boundaries one element to the right.
	'''
	
	for index, element in enumerate(UNSORTED_ELEMENTS): # enumerate is one way to go about looping with indecies in python
		min_element_index = index # assume min element is the first element

		# test against elements [index +1, ..., UNSORTED_ELEMENTS.length] to find the smallest
		for sub_index in range(index, len(UNSORTED_ELEMENTS)):# range is another way to go about looping with an index
			if (UNSORTED_ELEMENTS[sub_index] < UNSORTED_ELEMENTS[min_element_index]):
				# if this element is less, then it is the new minimum
				min_element_index = sub_index

		if min_element_index != index:
			UNSORTED_ELEMENTS[index], UNSORTED_ELEMENTS[min_element_index] = UNSORTED_ELEMENTS[min_element_index], UNSORTED_ELEMENTS[index]

	assert EXPECTED_RESULT == UNSORTED_ELEMENTS
	print UNSORTED_ELEMENTS


def main():
  selection_sort()

if __name__ == '__main__':
  main()