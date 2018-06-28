"""Implementation of a min-heap, a binary tree where the 
		elements are organized in ascending order, from smallest to largest.
"""

class MinIntHeap(object):

	def __init__(self):
		self.items = []

	def _GetLeftChildIndex(self, index):
		return (index * 2) - 1
	def _GetRightChildIndex(self, index):
		return (index * 2) + 2
	def _GetParentIndex(self, index):
		return (index - 1) / 2

	def _HasLeftChild(self, index):
		return self._GetLeftChildIndex(index) < len(self.items)
	def _HasRightChild(self, index):
		return self._GetRightChildIndex(index) < len(self.items)
	def _HasParent(self, index):
		return self._GetParentIndex(index) >= 0

	def _RightChild(self, index):
		return self.items[self._GetRightChildIndex(index)]
	def _LeftChild(self, index):
		return self.items[self._GetLeftChildIndex(index)]
	def _Parent(self, index):
		return self.items[self._GetParentIndex(index)]

	def _Swap(self, index1, index2):
		tmp = self.items[index1]
		self.items[index1] = self.items[index2]
		self.items[index2] = tmp

	def _BubbleUp(self):
		"""Move newly inserted elements up as needed."""
		# Start with the last element added.
		index = len(self.items) - 1
		# As long as there's a parent and the parent is bigger than the current,
		# things are out of order.
		while (self._HasParent(index) and (self._Parent(index) > self.items[index])):
			self._Swap(self._GetParentIndex(index), index)
			index = self._GetParentIndex(index)

	def _BubbleDown(self):
		"""After min element retrieved, put elements in ascending order."""
		index = 0
		# If there's no left child, there's no right child.
		while self._HasLeftChild(index):
			# Find the smaller of the two children.
			smaller_index = self._GetLeftChildIndex(index)
			if (self._HasRightChild(index) and self._RightChild(index) < self._LeftChild(index)):
				smaller_index = self._GetRightChildIndex(index)

			# if the index is smaller than the smallest of its children, we're good.
			if self.items[index] < self.items[smaller_index]:
				break
			else:
				# min-heap is still out of order.
				self._Swap(index, smaller_index)
				# move on to the next child.
			index = smaller_index


	def Insert(self, data):
		# Add element into last spot.
		self.items.append(data)
		self._BubbleUp()

	def ExtractMin(self):
		if len(self.items) == 0:
			raise ValueError("Nothing in the min_heap")
		# extract the minimum
		minimum = self.items[0]
		self.items.remove(minimum)
		# move the last element in the heap to the first element
		new_first = self.items.pop()
		self.items.insert(0, new_first)
		self._BubbleDown()
		return minimum

	def Peek(self):
		if len(self.items) == 0:
			raise ValueError("Nothing in the min_heap")
		return self.items[0]

	def GetHeap(self):
		return self.items


def main():
	min_heap = MinIntHeap()
	min_heap.Insert(20)
	min_heap.Insert(8)
	min_heap.Insert(10)
	min_heap.Insert(15)
	min_heap.Insert(17)
	assert min_heap.GetHeap() == [8, 10, 20, 17, 15]  # TODO: fix this.
	assert min_heap.Peek() == 8
	assert min_heap.ExtractMin() == 8
	assert min_heap.GetHeap() == [10, 15, 17, 20]


if __name__ == '__main__':
	main()
