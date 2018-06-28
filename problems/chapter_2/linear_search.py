def linear_search(search_target, expected_output):
	INPUT = [5, 2, 4, 6, 1, 3]
	obtained_output = 'nil'
	for index, value in enumerate(INPUT):
		if value == search_target:
			obtained_output = index
			break 

	assert expected_output == obtained_output
	print obtained_output



def main():
	linear_search(1, 4)
	linear_search(2, 1)
	linear_search(700, 'nil')

if __name__ == '__main__':
  main()
