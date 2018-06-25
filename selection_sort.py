"""Selection sort.
		Runtime: O(n^2), memory: O(1).
		Find the smallest element by scanning through the data set, 
		then swap it with the front element. Find the second 
		smallest and move it, and so on until all elements are in place.	
"""

def swap(data, index1, index2):
	tmp = data[index1]
	data[index1] = data[index2]
	data[index2] = tmp
	return data

def SelectonSort(data):
	is_sorted = False
	while not is_sorted:
		is_sorted = True
		for i in range(0, len(data)):
			smallest = data[i]
			for x in range(i, len(data)):
				if smallest > data[x]:
					is_sorted = False
					smallest = data[x]
					data = swap(data, i, x)
	return data


def main():
	data = [5, 4, 2, 1, 6 , 8, 7, 3, 0, 9]
	expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	received = SelectonSort(data)
	assert expected == received

if __name__ == '__main__':
	main()