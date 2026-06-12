# 12.2 Search a cyclically sorted array
# An array A of length n is said to be cyclically sorted if the smallest element in the
# array is at index i, and the sequence hA[i], A[i+1], . . . , A[n−1], A[0], A[1], . . . , A[i−1]i
# is sorted in increasing order, as illustrated in Figure 12.2 on the next page.
# Problem 12.2: Design an O(log n) algorithm for finding the position of the smallest
# element in a cyclically sorted array. Assume all elements are distinct. For example,
# for the array in Figure 12.2 on the facing page, your algorithm should return 4. pg. 135

## This is a sweet and important problem now right of the bat it look simple
# find the smallest value until you try to do it with the binary tree and you find out that u dont have a reference
# to compare with so logic comes in


## Brute Force method


def smallest_value_in_cycle_array(cycle_array: list):
    smallest_value = 0

    for idx in range(len(cycle_array)):
        if cycle_array[idx] < cycle_array[smallest_value]:
            smallest_value = idx
    print(smallest_value)


# Complexity
# Time O(n)
# space O(1)


def smallest_value_in_cycle_array_op(cycle_array: list):
    L = 0
    R = len(cycle_array) - 1

    while L < R:
        M = L + (R - L) // 2

        if cycle_array[M] > cycle_array[R]:
            L = M + 1
        else:
            R = M

    print(R)


## Why does this work?
# because we are consistently look for the split boundary and that is the point where
# L == R, using with this algorithm.
# This means if R is away from m where M is < (lesser)
# then we need to bring R closer to the green zone
# if we have where M is > R then R we need to bring L closer coz even M is outside the green area.

# Complexity
# Time Log m
# Space O(1)


if __name__ == "__main__":
    # Brute force
    smallest_value_in_cycle_array_op([2, 3, 4, 5, 1])
