# insertion sort, rewritten to sort arrays into nonincreasing order (decreasing order)


UNSORTED_ELEMENTS = [5, 2, 4, 6, 1, 3]
EXPECTED_RESULT = [6, 5, 4, 3, 2, 1]
OBTAINED_RESULT = []

def insertion_sort():
  for index, element in enumerate(UNSORTED_ELEMENTS):
    if not index == 0:
      key = UNSORTED_ELEMENTS[index] 
      target = index - 1

      while target >= 0 and UNSORTED_ELEMENTS[target] < key: # only change necessary. 
        UNSORTED_ELEMENTS[target + 1] = UNSORTED_ELEMENTS[target]
        target = target - 1
      UNSORTED_ELEMENTS[target + 1] = key

  OBTAINED_RESULT = UNSORTED_ELEMENTS
  assert OBTAINED_RESULT == EXPECTED_RESULT
  print OBTAINED_RESULT

def main():
  insertion_sort()

if __name__ == '__main__':
  main()
