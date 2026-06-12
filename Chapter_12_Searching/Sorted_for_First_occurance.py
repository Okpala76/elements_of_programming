# This is a new chapter and it is pretty exiting with its invariants
# it is always a sorted list and we will observe a binary_Search
# and draw some similarites with it and the binary search tree

# this is also only going to look at at static data and not stream ing like the
# last guy heap

# we are also going to see a guy call general search and we discuss matters
# around when how to think when we search
# REMINDER: DO AN EPISODE THAT INTRODUCES THIS CHAPTER AND YOUR UNDERSTAND
# OF THE pre-concepts(i am forgeting a word here)


# Problem 12.1: Write a method that takes a sorted array A and a key k and returns
# the index of the first occurrence of k in A. Return −1 if k does not appear in A. For
# example, when applied to the array in Figure 12.1 your algorithm should return 3 if
# k = 108; if k = 285, your algorithm should return 6.

# a sorted list is actally ordered in acending order as a inorder tree is as well
# and that is the beautiful as well that helps us see thus array as a tree more readly

# Task :
# find the first occurance of a search key(the value u are looking for)
# there might be many but we need the first

# so the solution is a eye to eye starer
# the first left we find as the key is the first one , issue is that we transverse
# the middle first before the left so How do we cook


# Brute Force
def sorted_first_occurance(t, A):

    for idx, value in A:
        if value == t:
            return idx

    return -1


# Complexity
# Time: O(n) because we go through all in values in the list i worst case
# Space: O(1) we store nothing except the variables we use


def sorted_first_occurance_op(t, A):
    L = 0
    R = len(A) - 1

    target_find = -1

    while L <= R:
        M = L + (R - L) // 2

        # if A[R] == t and target_find > R: ## this is necessary usless because if even if we find it there, we will
        #                                   ##  still to a full recursion before we can confrim it to be the first one.
        #     target_find = R

        # if A[M] == t and target_find > M:
        #     target_find = M

        # if A[L] == t:
        #     return L ### a debt with gpt

        if t > A[M]:
            L = M + 1

        elif t < A[M]:
            R = M - 1
        else:
            target_find = M
            R = M - 1

    print(target_find)

# Method
# Binary search variant
# Standard binary search stops immediately when it finds A[M] == k and returns that index. It assumes:

# There's only one occurrence, OR
# Any occurrence is fine
# This variant continues searching even after finding a match because it needs the first occurrence.

# complexity
# Time = Log n
# space O(1)

if __name__ == "__main__":

    sorted_first_occurance_op(5, [1, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9, 9])
