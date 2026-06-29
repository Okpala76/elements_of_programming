# Problem 15.3: How would you build a BST of minimum possible height from a
# sorted array A?

# This problem is a reverse of the list BST to tree
# but also arrange the tree to return the minimum height .. balanced filled from the left to the right

# To do the brute force we will need to go through the the list so many times and araange it over and over again till
# we get a minimun height
#
# but we already know that sorted list is a balanced BST tree inorderly transversed
#
# Therefore the mid point of the tree will be the idea node head to retuen us a balanced tree with minimum height

from Test_if_tree_head_is_BST import BST


def build_bst_from_a_sorted_array(A: list) -> BST:

    def builder(left: int, right: int) -> BST:
        if left > right:
            return None

        mid = left + (right - left) // 2

        root = BST(A[mid])

        root.left = builder(left, mid - 1)

        root.right = builder(mid + 1, right)

        return root

    return builder(0, len(A) - 1).value


if __name__ == "__main__":
    print(build_bst_from_a_sorted_array([1, 2, 3, 4, 5, 6, 7]))
