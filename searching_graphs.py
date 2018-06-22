"""Depth first search and breadth first search, in graphs."""

class Node(object):
	def __init__(self, name):
		self.name = name
		self.children = []

class Graph(object):
	def __init__(self):
		self.nodes = []

	def GetGraph(self):
		h = {}
		for i in range(0, len(self.nodes)):
			for x in range(0, len(self.nodes[i].children)):
				h.setdefault(i, []).append(self.nodes[i].children[x].name)
		return h

	def DepthFirstSearch(self, node, visited=None):
		found = False
		if visited == None: visited = []
		if node is None: return visited
		visited.append(node.name)
		for n in node.children:
			if n.name not in visited:
				visited = self.DepthFirstSearch(n, visited)
		return visited

	def BreadthFirstSearch(self, node):
		raise NotImplementedError()


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
	expected = {
		0: [1],
		1: [2],
		2: [0, 3],
		3: [2],
	}
	assert g.GetGraph() == expected
	assert g.DepthFirstSearch(n0) == [0, 1, 2, 3]


if __name__ == '__main__':
	main()