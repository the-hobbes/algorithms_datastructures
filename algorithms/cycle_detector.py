"""
	Write a function to detect if a circular list of adjacent indexes 
	forms a complete cycle.
	- ask what a circular list of adjacent indexes are
	- ask what a complete cycle is
"""

def isCompleteCycle(arr):
	visited = []
	pos = 0

	# for x in xrange(pos, len(arr)):
	# 	if pos in visited:
	# 		return False
	# 	visited.append(pos)
	# 	pos = (pos + arr[pos]) % len(arr)
	# return True

	while True:
		if pos in visited:
			return False
		visited.append(pos)
		pos = (pos + arr[pos]) % len(arr)
		if pos == 0:
			break
	return True


def main():
	a = [2, 2, -1]
	assert isCompleteCycle(a) == True
	b = [2, 2, 0]
	assert isCompleteCycle(b) == False
	c = [1]
	assert isCompleteCycle(c) == True

if __name__ == '__main__':
	main()