# Problem 15.2: Write a function that takes a BST T and a key k, and returns the first
# entry larger than k that would appear in an inorder traversal. If k is absent or no
# key larger than k is present, return null. For example, when applied to the BST in
# Figure 15.1 you should return 29 if k = 23; if k = 32, you should return null.


# This problem wants to give us a balue k and a BST and the have us
# - check for k in the tree and if k is found hoav us find the first value
# greater than k


# Brute force
from Test_if_tree_head_is_BST import BST, inorder_list, a


def larger_than_k(node: BST, k: int):
    bst_list = inorder_list(node, [])
    i = 0

    while i < len(bst_list):
        if bst_list[i] == k:
            break
        i += 1
    else:
        return None

    if i + 1 < len(bst_list):
        return bst_list[i + 1]
    else:
        return None


def larger_than_k_op(node: BST, k: int):
    found_k = False
    larger = 0

    while node:
        if k < node.value:
            larger = node.value
            node = node.left

        elif k > node.value:
            node = node.right

        if k == node.value:
            found_k = True

            node = node.right

    if found_k:
        return first_larger.value if first_larger else None

    return None


if __name__ == "__main__":
    print(larger_than_k_op(a, 6))
