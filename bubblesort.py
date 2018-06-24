"""Bubble Sort.
		Runtime: O(n^2). Memory: O(1)
		Naive sorting algorithm.
		Start at the beginning of the array, and swap the
		first two elements if the first is > second. Then,
		go to the next pair and so on, continuously making
		sweeps of the array until it is sorted. 

		In doing so, the smaller elements slowly bubble up
		 to the beginning of the list.
"""

def swap(data, idx):
	tmp = data[idx]
	data[idx] = data[idx + 1]
	data[idx + 1] = tmp
	return data

def BubbleSort(data):
	is_sorted = False
	while not is_sorted:
		is_sorted = True
		# len(data) - 1 because of i + 1.
		for i in range(0, len(data) - 1):
			if data[i] > data[i + 1]:
				data = swap(data, i)
				# Reset to false if we had to swap.
				is_sorted = False

	return data


def main():
	data = [5, 4, 2, 1, 6 , 8, 7, 3, 0, 9]
	expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	received = BubbleSort(data)
	assert expected == received

if __name__ == '__main__':
	main()
