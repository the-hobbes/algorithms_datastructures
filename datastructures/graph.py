"""A graph represented by an adjacency list."""

class Graph(object):
	"""You'll want a graph class.
			Unlike a tree, you can't necessarily reach all
			other nodes from a single node.
	"""
	def __init__(self):
		self.nodes = []

	def GetGraph(self):
		h = {}
		for i in range(0, len(self.nodes)):
			for x in range(0, len(self.nodes[i].children)):
				h.setdefault(i, []).append(self.nodes[i].children[x].name)
		return h


class Node(object):
	def __init__(self, name):
		self.name = name
		self.children = []


def main():
	n0 = Node(0)
	n1 = Node(1)
	n2 = Node(2)
	n3 = Node(3)
	n0.children.append(n1)
	n1.children.append(n2)
	n2.children.append(n0)
	n2.children.append(n3)
	n3.children.append(n2)
	g = Graph()
	g.nodes = [n0, n1, n2, n3]
	# Node two has an undirected edge to node 3.
	expected = {
		0: [1],
		1: [2],
		2: [0, 3],
		3: [2]
	}
	assert g.GetGraph() == expected


if __name__ == '__main__':
	main()