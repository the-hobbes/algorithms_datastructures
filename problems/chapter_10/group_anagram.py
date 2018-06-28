"""Group anagram.
		Write a method to sort an array of strings so that all the anagrams are next
		to each other.
		Questions to ask:
		- define an anagram? A word, phrase, or name formed by rearranging the 
		letters of another, such as cinema, formed from iceman.
		- give an example of sample input and expected output? 
			input: [hodor, dog, cinema, god, iceman]
			output: [cinema, iceman, dog, god, hodor]
		Initial thoughts: Generating/checking permutations is O(!n) time. Let's not
		do that. Instead, perhaps we could sort each string, and compare those to
		determine if two strings are anagrams.
		So, naive approach would be to iterate through the list, sort each string,
		then search through the rest of the list for another sorted string that
		matches.
		A better approach might be to do the sorting of the list in place, doing 
		something like insertion sort, where we set aside an element and shift the
		rest down, then insert it. This is still O(n^2).
"""

def groupAnagram(data):
	for current_element_index in range(len(data) - 1):
		sorted_current_element = sorted(data[current_element_index])
		for x in range(current_element_index + 1, len(data) - 1):
			if sorted_current_element == sorted(data[x]):
				set_aside = data[current_element_index + 1]
				data[current_element_index + 1] = data[x]
				data[x] = set_aside
	return data


def main():
	data = ['hodor', 'dog', 'cinema', 'god', 'iceman']
	expected = ['hodor', 'dog', 'god', 'cinema', 'iceman']
	got = groupAnagram(data)
	assert expected == got


if __name__ == '__main__':
	main()