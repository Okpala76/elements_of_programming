# Problem 15.1: Write a function that takes as input the root of a binary tree whose
# nodes have a key field, and returns true iff the tree satisfies the BST property. pg. 145


import heapq


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder_list(node: BST, result):
    if node is None:
        return None

    left = inorder_list(node.left, result)
    result.append(node.value)
    right = inorder_list(node.right, result)

    return result


# complexity
# Time O(n) every node visited
# Space O(n) result


def is_sorted(arr: list[int]):
    max_heap = []

    for value in arr:
        if not max_heap:
            heapq.heappush(max_heap, -value)
        else:
            current_max = -max_heap[0]
            if value >= current_max:
                heapq.heappush(max_heap, -value)
            else:
                return False
    return True


# complexity
# Time O(n log n) one time iteration through and the push everytime
# Space O(n) the heap


def is_sorted_n(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True


# complexity better that the heap implementation
# O(n)
# O(1)


def is_BST(node: BST):
    bst_list = inorder_list(node, [])
    return is_sorted_n(
        bst_list
    )  ## we could also use the python method; return arr == sorted(arr)


# complexity
# Time O(n log n) the sort is the greatest time opiawuni
# Space O(n) the arr number is the max space used per time


## Optimization

# the waste is sorting, or checking if is sorted which takes same time
# we could compare on the iteration start through the tree stack on recursion


def is_BST_op(node):
    def ranger(node: BST, lower: int, upper: int):
        if node is None:
            return True

        if not (lower <= node.value <= upper):
            return False

        return ranger(node.left, lower, node.value) and ranger(
            node.right, node.value, upper
        )

    return ranger(node, float("-inf"), float("inf"))


# complexity
# Time O(n)
# Space O(n)

# Algorithmic pattern
# The pattern is:
# Recursive DFS with valid range constraints

# Personal lesson from this problem:
# A BST is not a local parent-child rule.
# It is a global ancestor-boundary rule.
#  Each node must obey every ancestor constraint that brought us there.

if __name__ == "__main__":
    a = BST(5)
    b = BST(3)
    c = BST(7)
    d = BST(2)
    e = BST(4)
    f = BST(6)
    g = BST(8)

    a.left = b
    a.right = c

    b.left = d
    b.right = e
    c.left = f
    c.right = g

    print(is_BST_op(a))
