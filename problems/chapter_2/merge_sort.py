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

 	http://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif
'''

import math

INPUT = [5, 2, 4, 6, 1, 8, 3, 7]
EXPECTED_RESULT = [1, 2, 3, 4, 5, 6, 7, 8]

def merge(A, start, mid, end):
	''' Where:
		- A is an array.
		- start, mid and end are indecies into the array such that 
		start <= mid <= end
		- start is the 0th index, mid is the middle, and end is the last (nth) 
		of the array.
	'''
	# create left and right arrays from the original array
	left_array = A[start:mid]
	right_array = A[mid:end]

	# loop variables for keeping track
	left_index = 0 # keep track of the left index
	right_index = 0 # keep track of the right index

	# this is where the actual sorting is peformed
	for k in range(start, end):
		''' Explination of the if statement:
			You need to handle the case when one of the lists is empty. Consider:
				left_array = {1,2}, right_array = {3,4}, A = {}
			Your first loop iteration will check the first element of both lists and decide it needs to use the first list, leaving you with:
				list 1 = {2}, list 2 = {3,4}, merged = {1}
			Your second loop iteration will check the first element of both lists and decide it needs to use the first list again, leaving you with:
				list 1 = {}, list 2 = {3,4}, merged = {1,2}
			Your third loop iteration will check the first element of both lists and barf because there is no first element in the first list.

			So, you first check to see if the right index is larger than the length of the right array. This would mean that the right list is empty, 
			and that you should use the value in the left array. 
			If that's not the case, jump into the OR statement.
			If the left index is less than the length of the left array, this tells you that the left array isn't empty yet. So you've made your check.
			Then, you perform the actual comparison of elements in those arrays, to see which is bigger.
		'''
		if right_index >= len(right_array) or (left_index < len(left_array) and left_array[left_index] < right_array[right_index]):
			A[k] = left_array[left_index] # the element at the left index is smaller.
			left_index = left_index + 1 # and move onto the next element in the left array
		else: # otherwise the right element is smaller
			A[k] = right_array[right_index]
			right_index = right_index + 1 # move onto the next element in the right array


def merge_sort(A, start, end):
	''' Sort the elements in the subarray A[p...r].
		- if end - start <= 1, then the subarray has at most one lement and is 
		therefore already sorted (eg 1-1=0).
		- otherwise, another middle index is computed and two subarrays are 
		formed, and the process continues.
		- each of the array halves are merged by the merge subroutine.
	'''
	if end - start > 1: # if the array isn't made of a single element
		mid = int((start + end) / 2) # middle point
		merge_sort(A, start, mid) # left half
		merge_sort(A, mid, end) # right half
		merge(A, start, mid, end) # merge the halves


def main():
  # sort an entire array with merge-sort
  merge_sort(INPUT, 0, len(INPUT))
  assert INPUT == EXPECTED_RESULT
  print INPUT

if __name__ == '__main__':
  main()