## Thinking: This is a reduction problem .. so this it to recursively call the summtion funtionon smaller versions or reduced version of the array
def summation_of_array(arr: list):
    ## base case
    if len(arr) == 0:
        return 0
    ## recursion case
    return arr[0] + summation_of_array(arr[1::])


print(summation_of_array([1, 2, 3, 4, 5, 4, 9]))

## this is an O(n) and brute force becasue it goes through every variable to attain final answer


## Correction after AI look up

## this actually O(n^2) because we are slicing the problem and concacatinating
## in this line     return arr[0] + summation_of_array(arr[1::])

## Now the work around it is the use of the universal arritty and that mutates as recursion does.


def summation_of_arrays(arr: list, index=0):
    ## base case
    if index == len(arr):
        return 0

    ## recursive case
    return arr[index] + summation_of_arrays(arr, index + 1)

## This removes the need for slicing and returns us
## O(n) for both space and time complexity
