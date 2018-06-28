'''
  insertion sort
  input: a sequence of n numbers {a1, a2, ..., aN)
  output: a permutation of the input sequence such that (a`1 <= a`2, <= ..., <= a1N)
  (lowest to highest)
  - o(n^2)
'''

UNSORTED_ELEMENTS = [5, 2, 4, 6, 1, 3]
EXPECTED_RESULT = [1, 2, 3, 4, 5, 6]
OBTAINED_RESULT = []

def insertion_sort():
  '''Insertion sort is similar to sorting a hand of cards.
     - we start with an empty hand, and draw a card
     - we add the card to the appropriate position in the hand by comparing it 
     to the cards already in the hand.
     - the hand is thus always sorted
     - it is an efficient algorithm for sorting small numbers of elements

     UNSORTED_ELEMENTS[1...index - 1] corresponds to the currently sorted hand
     UNSORTED_ELEMENTS[index + 1... n] corresponds to the cards still on the table
  '''

  # loop over all the elements starting with index 1 (skip the first one)
  for index, element in enumerate(UNSORTED_ELEMENTS):
    if not index == 0: # skip first index here
      key = UNSORTED_ELEMENTS[index] # set aside the current number we are working on sorting
      target = index - 1 # set aside the index of the number directly before it

      while target >= 0 and UNSORTED_ELEMENTS[target] > key: # while the index is still valid and the value of the element begin compared is still greater than our sorting target...
        UNSORTED_ELEMENTS[target + 1] = UNSORTED_ELEMENTS[target] # set the value of the element to the right of the target to the target, moving it to the right by 1
        target = target - 1 # decrement the target index to move to the next element in line to be sorted
      UNSORTED_ELEMENTS[target + 1] = key # once all the elements before it have been shifted properly, put the current number we are sorting into its correct place, right after the last target sorted

  OBTAINED_RESULT = UNSORTED_ELEMENTS
  assert OBTAINED_RESULT == EXPECTED_RESULT
  print OBTAINED_RESULT

def main():
  insertion_sort()

if __name__ == '__main__':
  main()
