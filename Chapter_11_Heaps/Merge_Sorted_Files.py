## This is a Heap, a BST list equvalient of a
# complete tree(completely filled from the left to the right)
# where the legs of parent is defined by 2i+1 and 2i+2

# Design an algorithm that takes a set of files containing stock trades
# sorted by increasing trade times, and writes a single file containing the trades appearing in the individual files sorted in the same order. The algorithm should use
# very little RAM, ideally of the order of a few kilobytes.

# A group of files, each have multiple trades, sorted from earliest time of execution
# to latest time of exceution
# We are tasked to arrange it so that it is one file, and is still sorted from
# earliest to latest
#
# Dont use too much ram means, dont sum it up and sort it in a single list that is so in-effcient
# in say 500 files with say average of 200 questions each.
#
#
# Brute_force
# Here we use a current list to hold the earliest values from each list(files)
# then then figure out the minimum from the current to be the next guy int the
# output list


# Small problem solution
from more_itertools import value_chain

from Chapter_10_Binary_tree.Test_if_a_tree_is_balanced import BST


def merge_sorted_files(A: list, B: list):
    while True:
        if not A:
            for _ in B:
                print(_)
            break
        elif not B:
            for _ in A:
                print(_)
            break
        elif A[0] == B[0]:
            print(A.pop(0))
        elif A[0] > B[0]:
            print(B.pop(0))
        elif A[0] < B[0]:
            print(A.pop(0))


# merge_sorted_files([1, 3, 4, 23], [4, 6, 7, 90])


## Brute Force


def Merge_sorted_files_bru(files: list[list]):
    # [[1,2,3,],
    #  [4,5,6],
    #  [7,8,9]]

    indices = [0] * len(files)

    while True:
        smallest_value = None
        smallest_file = None

        for file_index in range(len(files)):
            # We try to know if the list at the index in focus(file_index)
            # is already exhausted.
            if indices[file_index] >= len(files[file_index]):
                continue

            ## we find the exact head at that index
            current = files[file_index][indices[file_index]]

            # Because during this for-loop, we will visit all heads, so if we find
            # a smaller than we had found before we update smallest
            if smallest_value is None or current < smallest_value:
                smallest_value = current
                smallest_file = file_index

        ## if all has been exhausted
        if smallest_value is None:
            break

        print(smallest_value)

        # because now that we have printed its head we can then go ahead
        # to increase the indices list, so future iterations at line 63 will find its next index
        # line 63, say file one is pointing to index of O
        # if we find the smallest value in that file we call it the smallest file then
        # we increase its index from 0 = 1
        # so when we run 63 again we get 1 and so on till we exhaust the opiawuni

        indices[smallest_file] += 1


Merge_sorted_files_bru(
    [
        [
            1,
            2,
            3,
        ],
        [4, 5, 6],
        [7, 8, 9],
    ]
)


# as we can see the waste is massive
# we are calling recursion for every head find and every depth

# Hence
# complexity
# Time: O(nk)
# n is not the lists that we pass in but every value of every list
# Image have 1k lists
#
# and k is the number of lists we have
#
# Space: O(k)
# because our "indices" list will only create space for the list amount


## The optimized approach use heap / prirority list to cook
## we call it a K-Way Merge
# and the trick is in, what we pop() from the Heap
# we know we are to insert in the final sorted list,
# but how we know what list our pop() comes, so we know what file to add to the heap from, is the bone of contention

import heapq


def Merge_Sorted_files_op(files: list[list]):
    min_heap = []

    ## get all first boys into the heap
    for file_idx in range(len(files)):
        if len(files[file_idx]) > 0:
            heapq.heappush(min_heap, (files[file_idx][0], file_idx, 0))

    while min_heap:
        value, file_idx, index = heapq.heappop(
            min_heap
        )  ## Of course u need to define the list you are poping from

        print(value)

        next_index = index + 1

        if next_index < len(files[file_idx]):
            # as you have noticed a python heap workes with a normal list
            # and you declare the list every time u want to push into it
            heapq.heappush(min_heap, (files[file_idx][index], file_idx, index))


## Complexity
# Time O(n log k)
#   n because we go through every single trade in the file ,
#   log k because our heap use log k to process the sorted data stucture
# Space O(k)
#   because the min_heap uses a max space of k( number of files)


## Learning notes
# I learnt that boundary check should always be done with boundary variables rather than postion checks
# I learnt this pattern for the optimized is called K-way merge, Because it accepts a unspecified amount of
# entries is optimized for streaming algorithms
# I learnt to use the heapq model from python
#
