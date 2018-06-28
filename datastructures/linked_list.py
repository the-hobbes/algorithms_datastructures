class Node(object):
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next


class LinkedList(object):
	def __init__(self, head=None):
		self.head = head
		self.length = 1

	@property
	def size(self):
		return self.length

	def insert(self, node):
		# new_head -> old_head -> next...
		old_head = self.head
		self.head = node
		self.head.next = old_head
		self.length += 1

	def search(self, data):
		current = self.head
		while current:
			if current.data == data:
				return current.data
			current = current.next
		return None

	def delete(self, data):
		# head-> --deleteme-- -> next
		current = self.head
		previous = current
		while current:
			if current.data == data:
				previous.next = current.next
				self.length -= 1
				break
			previous = current
			current = current.next

def main():
	node_a = Node('a')
	node_b = Node('b')
	node_c = Node('c')
	node_d = Node('d')
	ll = LinkedList(node_a)

	assert ll.size == 1
	ll.insert(node_b)
	ll.insert(node_c)
	ll.insert(node_d)
	assert ll.size == 4

	assert ll.search('b') == 'b'
	assert ll.search('d') == 'd'
	assert ll.search('c') == 'c'

	ll.delete('c')
	assert ll.size == 3
	assert ll.search('c') == None

	print '***All tests pass**'


if __name__ == '__main__':
	main()
		
