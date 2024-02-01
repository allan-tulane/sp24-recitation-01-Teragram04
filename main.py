"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###


def linear_search(mylist, key):
  """ done. """
  for i, v in enumerate(mylist):
    if v == key:
      return i
  return -1


def binary_search(mylist, key):
  """ done. """
  return _binary_search(mylist, key, 0, len(mylist) - 1)


def _binary_search(mylist, key, left, right):
  if right >= left:
    middle_val = (left + right) // 2

    #If the key is the middle number, return it
    if key == mylist[middle_val]:
      return middle_val

    #Otherwise, if the middle value is less than the key, search the right half and repeat
    elif key < mylist[middle_val]:
      return _binary_search(mylist, key, left, middle_val - 1)

    #Otherwise, if the middle value is greater than the key, search the left half and repeat
    elif key > mylist[middle_val]:
      return _binary_search(
          mylist, key, middle_val + 1,
          right)  #use left and right as beginning and end list indices.

  else:
    return -1
  """
  Recursive implementation of binary search.

	Params:
    mylist....list to search
    key.......search key
    left......left index into list to search
    right.....right index into list to search

	Returns:
    index of key in mylist, or -1 if not present.
	"""


def time_search(search_fn, mylist, key):
  t0 = time.time() * 1000
  search_fn(mylist, key)
  return time.time() * 1000 - t0
  """
	Return the number of milliseconds to run this
	search function on this list.

	Note 1: `search_fn` parameter is a function.
	Note 2: time.time() returns the current time in seconds. 
	You'll have to multiple by 1000 to get milliseconds.

	Params:
	  sort_fn.....the search function
	  mylist......the list to search
	  key.........the search key 

	Returns:
	  the number of milliseconds it takes to run this
	  search function on this input.
	"""


def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
  #Create a list to store the tuple results
  results = []
  i = 0

  for i in range(len(sizes)):
    results.append(
        (sizes[i], time_search(linear_search, range(int(sizes[i])), -1),
         time_search(binary_search, range(int(sizes[i])), -1)))
    #results.append(time_search(binary_search, sizes[i], -1))
  return results
  """
	Compare the running time of linear_search and binary_search
	for input sizes as given. The key for each search should be
	-1. The list to search for each size contains the numbers from 0 to n-1,
	sorted in ascending order. 

	You'll use the time_search function to time each call.

	Returns:
	  A list of tuples of the form
	  (n, linear_search_time, binary_search_time)
	  indicating the number of milliseconds it takes
	  for each method to run on each value of n
	"""
  ### TODO

  ###


def print_results(results):
  """ done """
  print(
      tabulate.tabulate(results,
                        headers=['n', 'linear', 'binary'],
                        floatfmt=".3f",
                        tablefmt="github"))


print_results(compare_search())
