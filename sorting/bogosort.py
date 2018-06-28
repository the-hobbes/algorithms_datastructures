import random
import time


def is_sorted(data):
	for i in range(len(data) - 1):
		if data[i] > data[i + 1]:
			return False
	return True

def bogosort(data):
	while not is_sorted(data):
		random.shuffle(data)
	return data


def main():
	data = [5, 4, 2, 1, 6 , 8, 7, 3, 0, 9]
	t0 = time.time()
	bogosort(data)
	t1 = time.time()
	bogotime = t1 - t0

	# Python uses a sorting algorithm called Timsort
	# https://en.wikipedia.org/wiki/Timsort
	t2 = time.time()
	sorted(data)
	t3 = time.time()
	timsorttime = t3 - t2

	assert timsorttime < bogotime
	
	

if __name__ == '__main__':
	main()