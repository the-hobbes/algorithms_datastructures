"""Traversals.
	Inorder: left, root, right (A B C)
	Preorder: root, left, right (B, A, C)
	Postorder: left, right, root (A, C, B)
"""

class Node(object):
	"""Binary tree.
		- Each node has no more than two child nodes.
		- Binary search tree: a binary tree whose any subtree contains left
			nodes less than root nodes, which are less than right nodes.
	"""

	def __init__(self, data=None):
		self.data = data
		self.left = None
		self.right = None

	def Insert(self, value):
		# Value is <= the data of the current node.
		if value <= self.data:
			# If there is no left node yet...
			if not self.left:
				self.left = Node(value)
			else:
				# otherwise, get the left node to perform insert.
				self.left.Insert(value)
		# Value must be > than the data of the current node.
		else:
			if not self.right:
				self.right = Node(value)
			else:
				self.right.Insert(value)

	def Contains(self, value):
		if value == self.data:
			return True
		if value < self.data:
			if not self.left:
				return False
			else:
				return self.left.Contains(value)
		if value > self.data:
			if not self.right:
				return False
			else:
				return self.right.Contains(value)


	def InOrderTraversal(self, l=None):
		if l is None:
			# Default args evaluated only once: https://tinyurl.com/ydb5ug8x.
			l = []
		if self.left:
			self.left.InOrderTraversal(l)
		l.append(self.data)
		if self.right:
			self.right.InOrderTraversal(l)
		return l

	def PreOrderTraversal(self, l=None):
		if l is None:
			l = []
		l.append(self.data)
		if self.left:
			self.left.PreOrderTraversal(l)
		if self.right:
			self.right.PreOrderTraversal(l)
		return l

	def PostOrderTraversal(self, l=None):
		if l is None:
			l = []
		if self.left:
			self.left.PostOrderTraversal(l)
		if self.right:
			self.right.PostOrderTraversal(l)
		l.append(self.data)
		return l


def main():
	tree = Node(10)
	tree.Insert(5)
	tree.Insert(15)
	tree.Insert(8)
	assert tree.Contains(15) == True
	assert tree.Contains(7) == False
	print tree.InOrderTraversal()
	assert tree.InOrderTraversal() == [5, 8, 10, 15]
	assert tree.PreOrderTraversal() == [10, 5, 8, 15]
	assert tree.PostOrderTraversal() == [8, 5, 15, 10]

if __name__ == '__main__':
	main()