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
	# at most one character (in the middle) can have an odd count.
	s = s.lower()
	character_table = {}
	for char in s:
		if char in character_table:
			character_table[char] += 1
		else:
			character_table[char] = 1
	
	seen_odd = False
	for k,v in character_table.iteritems():
		if v % 2 != 0:
			if seen_odd == True:
				return False
			seen_odd = True
	return True


# 1.5 One Away
def OneAway(s1, s2):
	# Edits allowed: insert, remove, replace.

	def isOneReplace(s1, s2):
		found_difference = False
		for x in xrange(0, len(s1) - 1):
			if s1[x] != s2[x]:
				if found_difference:
					return False
				found_difference = True
		return True

	def isOneInsertion(s1, s2):
		"""Can you insert a character into s1 to make s2?
			- Move through the strings, comparing each character.
			- If the character doesn't match, check the position in 
			the string we are at by looking at the index. If they are
			the same, then this is the first insertion and that is
			allowed. Move to the next character by increasing the 
			index in that string.
			- If another comparison doesn't match, the indexes will
			be compared and found to differ. This means there will be
			more than one insertion edit needed to be done to s1 to
			make s2, so we return false.
		"""
		index1 = 0
		index2 = 0
		while (index2 < len(s2)) and (index1 < len(s1)):
			if s1[index1] != s2[index2]:
				if index1 != index2:
					return False
				index2 += 1
			else:
				index1 += 1
				index2 += 1
		return True

	# Decide which checks should be called based on string length.
	if len(s1) == len(s2):
		# Must be a replacement.
		return isOneReplace(s1, s2)
	elif len(s1) + 1 == len(s2):
		# Must be an insertion.
		return isOneInsertion(s1, s2)
	elif len(s1) - 1 == len(s2):
		# Must be a removal. Same as insertion but reversed.
		return isOneInsertion(s2, s1)

	return False


# 1.6 String compression.
def StringCompression(s):
	prev = None
	count = 1
	compression = ''
	for char in s:
		if prev == char:
			count += 1
		else:
			compression += char
			compression += str(count)
			count = 1
			prev = char
	print compression
	return compression


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
	assert PalindromePermuation('Tact Cooa') == True
	assert PalindromePermuation('Tact zzz') == False

	# 1.5
	assert OneAway('pale', 'ple') == True
	assert OneAway('pale', 'bale') == True
	assert OneAway('pale', 'bake') == False

	# 1.6
	assert StringCompression('aabbcccccaaa') == 'a2b1c5a3'  # fix a count

if __name__ == '__main__':
	main()
