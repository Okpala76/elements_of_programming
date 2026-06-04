## Thinking:
## This is a reduction problem.
##
## The goal is to recursively call the summation function on
## smaller and smaller versions of the array until there is
## nothing left to process.
##
## Every recursive call reduces the problem size by one element.


def summation_of_array(arr: list):

    ## BREAKPOINT 1
    ## Entering the function.
    ## Observe the current state of arr.

    ## Base case
    ## Once the array is empty there is nothing left to add.
    if len(arr) == 0:
        return 0

    ## BREAKPOINT 2
    ## Before the recursive call.
    ##
    ## Notice that:
    ## arr[0] is kept for later.
    ## arr[1:] becomes the smaller problem.
    ##
    ## We are saying:
    ## "Add the first value to the sum of everything else."

    ## Recursive case
    return arr[0] + summation_of_array(arr[1:])


print(summation_of_array([1, 2, 3, 4, 5, 4, 9]))

## Initial thought:
## This looks like O(n) because we visit every element once.

## Correction:
## This is actually O(n²) time complexity.
##
## Why?
##
## Because slicing is not free.
##
## Every call creates a brand new array:
##
## arr[1:]
##
## Example:
##
## [1,2,3,4,5]
## -> creates [2,3,4,5]
##
## [2,3,4,5]
## -> creates [3,4,5]
##
## [3,4,5]
## -> creates [4,5]
##
## etc.
##
## The total copying work becomes:
##
## n + (n-1) + (n-2) + ... + 1
##
## Which equals O(n²).


## Better approach:
##
## Instead of creating new arrays,
## keep the original array and move an index.
##
## We reduce the problem logically rather than physically.
##
## This avoids slicing completely.


def summation_of_arrays(arr: list, index=0):

    ## BREAKPOINT 1
    ## Observe current index.
    ## Observe current value being processed.

    ## Base case
    ## Once index reaches the length of the array
    ## there are no more elements left.
    if index == len(arr):
        return 0

    ## BREAKPOINT 2
    ## Before recursive call.
    ##
    ## We keep arr[index]
    ## and move forward one position.

    ## Recursive case
    return arr[index] + summation_of_arrays(arr, index + 1)


print(summation_of_arrays([1, 2, 3, 4, 5, 4, 9]))


## Complexity
##
## Time Complexity: O(n)
## Space Complexity: O(n)
##
## Time becomes O(n) because we no longer
## create new arrays on every recursive call.
##
## The only extra memory comes from the
## recursion call stack.


# summation([1,2,3,4])
# │
# ├── 1 + summation([2,3,4])
# │
# │   ├── 2 + summation([3,4])
# │   │
# │   ├── 3 + summation([4])
# │   │   │
# │   │   ├── 4 + summation([])
# │   │   │   │
# │   │   │   └── 0
