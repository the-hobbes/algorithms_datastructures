"""Compute fibonacci using memoization."""

cache = {}
def fibs(n):
	if n == 1 or n == 2:
		return n
	elif n in cache:
		return cache[n]
	else:
		cache[n] = fibs(n - 1) + fibs(n - 2)
	return cache[n]

# lru_cache available in python 3.
# from functools import lru_cache
# @lru_cache(maxsize=1000)
# def lruFibs(n):
# 	if n == 1 or n == 2:
# 		return n
# 	else:
# 		return fibs(n - 1) + fibs(n - 2)

def fibsNoGlobal(n, cache={0:1,1:1}):
    if n in cache: 
    	return cache[n]                                                                                 
    val = fibsNoGlobal(n-1, cache) + fibsNoGlobal(n-2, cache)                                                                        
    cache[n] = val                                                                                                 
    return val    

def main():
	expected = []
	for i in range(1, 10001):
		val = fibs(i)
		expected.append(val)
		print('fibs of %d : %d' % (i, val))
	
	obtained = []
	for i in range(1, 10001):
		val = fibsNoGlobal(i)
		obtained.append(val)
	assert expected == obtained

	# lru_cache works in python 3.
	# for i in range(1, 10):
	# 	print('fibs of %d : %d' % (i, lruFibs(i)))


if __name__ == '__main__':
	main()
