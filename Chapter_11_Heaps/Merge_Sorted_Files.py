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
