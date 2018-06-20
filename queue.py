class Queue(object):
	"""Implementation of a FIFO queue."""

	class _Node(object):
		data = None
		next = None
		
		def __init__(self, data=None):
			self.data = data
	
	def __init__(self):
		# Pointers to both ends of the queue.		
		self.first = None
		self.last = None

	def Enqueue(self, item):
		"""Add an item to the end of the list =>[n1, n2, n3]."""
		n = self._Node(data=item)
		if self.last:  # Is last initialized?
			self.last.next = n
		self.last = n
		if not self.first:  # Is first initialized?
			self.first = self.last
		
	def Dequeue(self):
		"""Remove the first item in the list [n1, n2, n3] =>."""
		if not self.first:
			raise ValueError("Empty Queue")
		d = self.first.data
		self.first = self.first.next
		if not self.first:  # There are no more nodes.
			last = None
		return d

	def Peek(self):
		"""Return the top of the queue."""
		if not self.first:
			raise ValueError("Empty Queue")
		return self.first.data

	def IsEmpty(self):
		"""Is the queue empty?"""
		return self.first == None

	def PrintQueue(self):
		q = []
		if not self.first:
			raise ValueError("Empty Queue")
		current = self.first
		while current:
			q.append(current.data)
			current = current.next
		q.reverse()
		print '=>[%s]=>' % ', '.join(q)


def main():
	q = Queue()
	q.Enqueue('a')
	q.Enqueue('b')
	q.Enqueue('c')
	q.Enqueue('d')
	q.PrintQueue()
	# [d, c, b, a] =>
	assert q.Peek() == 'a'
	q.Enqueue('e')
	# [e, d, c, b, a] =>
	assert q.Dequeue() == 'a'
	q.Dequeue()
	q.Dequeue()
	q.Dequeue()
	q.Dequeue()
	assert q.IsEmpty()
	try:
		q.Dequeue()
	except ValueError as ve:
		print "Test passed, we got: %s" % ve


if __name__ == '__main__':
	main()
		