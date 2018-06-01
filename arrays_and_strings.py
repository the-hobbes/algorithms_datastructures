# 1.1 Is unique
def IsUnique(s):
	srted = sorted(s)
	for i in range(0, len(srted) - 1):
		if srted[i] == srted[i+1]:
			return False
	return True


# 1.2 Check permutation
def CheckPermutation(s1, s2):
	if len(s1) != len(s2):
		return False
	s1 = sorted(s1)
	s2 = sorted(s2)
	for x in xrange(1, len(s1)):
		if s1[x] != s2[x]:
			return False
	return True


# 1.3 URLify
def URLify(s, l):
	new_s = []
	for x in xrange(0, l):
		if s[x] == ' ':
			new_s.append('%20')
		else:
			new_s.append(s[x])
	return ''.join(new_s)


# 1.4 Palindrom permutation
def PalindromePermuation(s):
	def GeneratePermutations(s):
		pass
	def GeneratePalindromes(s):
		pass

	is_palindrome = False
	permutations = GeneratePermutations(s)
	palindromes = GeneratePermutations(permutations)
	if len(palindromes) > 0: is_palindrome = True
	return (is_palindrome, 'permutations: %s' % ', '.join(permutations))


def main():
	# 1.1
	assert IsUnique('xxapdfrrgcg433fdx') == False
	assert IsUnique('abcdefghijklmnop') == True

	# 1.2
	assert CheckPermutation('abcdef', 'ghijklmnop') == False
	assert CheckPermutation('abcdef', 'adbecf') == True

	# 1.3
	assert URLify('Mr John Smith    ', 13) == 'Mr%20John%20Smith'

	# 1.4
	assert PalindromePermuation('Tact Coa') == (True, 'permutations: taco cat, atco cta')

if __name__ == '__main__':
	main()
