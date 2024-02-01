# CMPS 2200  Recitation 01

**Name (Team Member 1):**__Margaret Parsons_  
**Name (Team Member 2):**_________________________

In this recitation, we will investigate asymptotic complexity. Additionally, we will get familiar with the various technologies we'll use for collaborative coding.

To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`. All tests are in `test_main.py`.

## Install Python Dependency

We need Python library of "tabulate" to visualize the results in a good shape. Please install it by running 'pip install tabulate' or 'pip install -r requirements.txt' in Shell Tab of Repl.  

## Running and testing your code

- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Comparing search algorithms

We'll compare the running times of `linear_search` and `binary_search` empirically.

`Binary Search`: Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

- [x] 1. **In `main.py`, the implementation of `linear_search` is already complete. Your task is to implement `binary_search`. Implement a recursive solution using the helper function `_binary_search`.**

- [x] 2. **Test that your function is correct by calling from the command-line `pytest test_main.py::test_binary_search`**

- [x] 3. **Write at least two additional test cases in `test_binary_search` and confirm they pass.**

- [x] 4. **Describe the worst case input value of `key` for `linear_search`? for `binary_search`?**

The worst case input value of 'key' for 'linear_search' would be the value at the end of the list, as it must search through all the elements in order. The worst case input value of 'key' for 'binary_search' would be a value at the beginning or the end, as it would have to continue to branch out until it reaches the extremes.

- [x] 5. **Describe the best case input value of `key` for `linear_search`? for `binary_search`?** 

The best case 'key' input value for 'linear_search would be the first element on the list. The best case 'key' input value for 'binary_search' would be the middle value, as that is what is initially checked.

- [x] 6. **Complete the `time_search` function to compute the running time of a search function. Note that this is an example of a "higher order" function, since one of its parameters is another function.**

- [x] 7. **Complete the `compare_search` function to compare the running times of linear search and binary search. Confirm the implementation by running `pytest test_main.py::test_compare_search`, which contains some simple checks.**

- [x] 8. **Call `print_results(compare_search())` and paste the results here:**

|            n |   linear |   binary |
|--------------|----------|----------|
|       10.000 |    0.004 |    0.005 |
|      100.000 |    0.006 |    0.003 |
|     1000.000 |    0.067 |    0.005 |
|    10000.000 |    0.769 |    0.014 |
|   100000.000 |   92.808 |    0.021 |
|  1000000.000 |  497.339 |    0.023 |
| 10000000.000 | 5115.395 |    0.058 |

- [x] 9. **The theoretical worst-case running time of linear search is $O(n)$ and binary search is $O(log_2(n))$. Do these theoretical running times match your empirical results? Why or why not?**

I think the theoretical worst-case run times listed above match my empirical results for linear search, but not for binary search. The worst case result of linear search is O(n), which means that as the number of elements that need to be searched increases, the time it takes will also increase. Linear search can be seen exhibiting this behavior in the above chart.

For binary search (log_2(n)), as the number of elements to be sorted increases, the time it takes stays relatively stable, instead of increasing like it would in the worst-case scenario.

- [x] 10. Binary search assumes the input list is already sorted. Assume it takes $\Theta(n^2)$ time to sort a list of length $n$. Suppose you know ahead of time that you will search the same list $k$ times.
      
  + What is worst-case complexity of searching a list of $n$ elements $k$ times using linear search? **The worst case run time is Theta(n^2) + K * O(n). This is the time it takes to sort the list plus the worst-case run time for a linear search (O(n)) multiplied by the number of times you search the same list**
    
  + For binary search? **For binary search it would be Theta(n^2) + K * (log(n)). Add the amount of time it takes to sort the list to log(n) (the worst case runtime) and multiply it by the number of times you iterate through the list.**
    
  + For what values of $k$ is it more efficient to first sort and then use binary search versus just using linear search without sorting? **K=1? Generally, binary search with a time complexity of O(log(n)) will be much quicker than linear search and O(n).**
