"""Depth first search and breadth first search, in graphs."""


def DepthFirstSearch(graph, root, visited=None):
	"""Go deep.
			Explores possible vertices (from a supplied root) 
			down each branch before backtracking. Does two things:
			- Mark the current vertex as being visited.
			- Explore each adjacent vertex that is not included
				in the visited set.
	"""
	if visited is None:
		visited = set()
	visited.add(root)
	for new_root in graph[root] - visited:
		DepthFirstSearch(graph, new_root, visited)
	return visited
		

def BreadthFirstSearch(graph, root):
	"""Go wide.
			Search level by level, out from the root. Use a queue to
			save all the neighbors to visit.
	"""
	visited = set()
	queue = [root]
	while queue:
		vertex = queue.pop()
		if vertex not in visited:
			visited.add(vertex)
			queue.extend(graph[vertex] - visited)
	return visited


def main():
	graph = {
		# All nodes are connected.
		'A': set(['B', 'C']),
		'B': set(['A', 'D', 'E']),
		'C': set(['A', 'F']),
		'D': set(['B']),
		'E': set(['B', 'F']),
		'F': set(['C', 'E']),  # A cycle.
	}
	assert DepthFirstSearch(graph, 'C') == set(['E', 'D', 'F', 'A', 'C', 'B'])
	assert BreadthFirstSearch(graph, 'A') == set(['B', 'C', 'A', 'F', 'D', 'E'])

	graph2 = {
		# Directed graph.
		0: set([1, 4, 5]),
		1: set([3, 4]),
		2: set([1]),
		3: set([2, 4]),
		4: set([]),
		5: set([6, 7]),
		6: set([]),
		7: set([]),
	}
	# 0 has connections to each node in the graph.
	assert DepthFirstSearch(graph2, 0) == set([0, 1, 2, 3, 4, 5, 6, 7])
	# 3 has connections to 3, 2, 4 and 1
	assert BreadthFirstSearch(graph2, 3) == set([1, 2, 3, 4])
	# 2 has connections to 2, 1, 3, and 4
	assert BreadthFirstSearch(graph2, 2) == set([1, 2, 3, 4])
	# 5 has connections to itself, 6 and 7
	assert BreadthFirstSearch(graph2, 5) == set([5, 6, 7])


if __name__ == '__main__':
	main()