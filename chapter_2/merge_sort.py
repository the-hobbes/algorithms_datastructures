''' 
	Merge sort, a divide and conquer algorithm using recursion for sorting
 	- o(n) time
 	Idea:
 	You have two piles of cards face up on the table. These piles are sorted, 
 	with the smallest cards on top. We want to merge the two piles into a single
 	sorted ouput file, face down (biggest on the top). 
 	Choose the smaller of the two cards on top of the face-up piles, remove it 
 	from its pile, and place it in top of the output pile face-down. Repeate 
 	until one input pile is empty, then put the remaining pile and put it face
 	down on the output pile.
 	In the following, a sentinal value is added to each pile so that the 
 	algorithm doens't have to perform a check to see if a pile is empty. 
'''

import math

INPUT = [5, 2, 4, 6, 1, 3]
SENTINAL = None

def merge(A, p, q, r):
	''' Where:
		- A is an array.
		- p, q, and r are indecies into the array such that p <= q <= r
		- p is the start (0th), q is the middle, and r is the end (nth) of the
		arry.
		Assume:
		- A[p..q] and A[q+1..r] are sorted.
	'''
	# compute the length of the subarrays A[p..q] and A[q+1..r]
	n1 = (q - p) + 1
	n2 = r - q 

	# create left and right arrays from the original array, using the lengths
	# computed as slice indecies. Also add the sentinal value to each array
	left_array = A[: n1]
	right_array = A[n2 + 1 :] # TODO(pheven): fix the messup here

	left_array.append(SENTINAL)
	right_array.append(SENTINAL)

	i = 0
	j = 0
	for k in range(p, r):
		if left_array[i] <= right_array[j]:
			A[k] = left_array[i] # if the left element is smaller, choose it
			i = i + 1 # and move onto the next element in the left array
		else: # otherwise the right element is smaller
			A[k] = right_array[j]
			j = j + 1 # move onto the next element in the right array


def merge_sort(A, p, r):
	''' Sort the elements in the subarray A[p...r].
		- if p >= r, then the subarray has at most one lement and is therefore
		already sorted (the start index is greater than the end index, or they
		are the same).
		- otherwise, another middle index is computed and two subarrays are 
		formed, and the process continues.
		- each of the array halves are merged by the merge subroutine.
	'''
	if p < r: # if the array isn't made of a single element
		q = int(math.floor((p + r) / 2)) # middle point
		merge_sort(A, p, q) # left half
		merge_sort(A, q + 1, r) # right half
		merge(A, p, q, r) # merge the halves


def main():
  # sort an entire array with merge-sort
  merge_sort(INPUT, 0, len(INPUT) -1)
  print INPUT

if __name__ == '__main__':
  main()