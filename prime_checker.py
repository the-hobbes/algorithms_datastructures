"""Check the primality of a number."""

import math

def isPrimeNaive(number):
	"""Iterate from 2 to number - 1, checking for divisibility."""
	if number <= 2:
		print number
	for i in range(2, number): # range excludes last
		if number % i == 0:
			return False
	return True

def isPrime(number):
	"""Iterate only up to square root of number."""
	if number <= 2:
		print number
	for i in range(2, int(math.sqrt(number))):
		if number % i == 0:
			print('No, %d is divisible by %d' % (number, i))
			return False
	return True


def main():
	assert isPrimeNaive(7) == True
	assert isPrimeNaive(24) == False
	assert isPrime(7) == isPrimeNaive(7)
	assert isPrime(111) == False
	assert isPrime(479) == True

if __name__ == '__main__':
	main()