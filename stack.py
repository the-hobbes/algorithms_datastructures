class Stack(object):
	""" Stack == LIFO, stack of dinner plates."""

	class _StackNode(object):
		def __init__(self, data, next):
			self.data = data
			self.next = next

	def __init__(self, data=None, next=None):
		self.top = self._StackNode(data, next)

	def Pop(self):
		"""Remove the top item."""
		if self.top == None:
			raise ValueError("Empty Stack")
		temp = self.top.data
		self.top = self.top.next
		return temp

	def Push(self,item):
		"""Add an item to the top of the stack."""
		t = self._StackNode(data=item, next=self.top)
		self.top = t

	def Peek(self):
		"""Return the top of the stack."""
		return self.top.data

	def IsEmpty(self):
		"""No more items left in the stack?"""
		return self.top == None


def main():
	stk = Stack('a')
	stk.Push('b')
	stk.Push('c')
	stk.Push('d')
	assert stk.Peek() == 'd'
	stk.Pop()
	stk.Pop()
	assert stk.Peek() == 'b'
	stk.Pop()
	stk.Pop()
	try:
		stk.Pop()
	except ValueError as ve:
		print "Test passed, we got an %s" % ve
	assert stk.IsEmpty() == True
	stk.Push('e')
	assert stk.Peek() == 'e'


if __name__ == '__main__':
	main()