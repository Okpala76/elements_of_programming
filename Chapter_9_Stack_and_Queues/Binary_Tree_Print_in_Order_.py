# ## Problem 9.2: Given the root node r of a binary tree, print all the keys at r and its
# descendants. The keys should be printed in the order of the corresponding nodes’
# depths. Specifically, all keys corresponding to nodes of depth d should appear in a
# single line, and the next line should correspond to keys corresponding to nodes of
# depth d + 1. You cannot use recursion. You may use a single queue, and constant
# additional storage. For example, you should print

# 314
# 6 6
# 271 561 2 271
# 28 0 3 1 28
# 17 401 257
# 641
# for the binary tree in Figure 10.1 on Page 57.

## This problem wants us to go through a binary tree and print every level of the BinaryTreeNode
# as a line
#
# | ------------ 0
# | ------------ 1
# | ------------ 2
# | ------------ 3
# | ------------ 4

# Refer to Binary tree image to find solutions for clarity


## Brute force

# For the brute force we are going build an height transverser or getter and
# build a breath transverser and then call them overlapping each other to get our
# desired result


from collections import deque


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# First we write a height getting function


def tree_height(node):
    if node is None:
        return -1

    tree_left_height = tree_height(node.left)  # -1
    tree_right_height = tree_height(node.right)  # -1

    return 1 + max(tree_left_height, tree_right_height)
    ## the final height will give us a height less than the actual height


# Compelexity
# Time O(n) we are going to visit every node
# Space O(n) as we recursively call


def print_node_at_depth(node: BinaryTreeNode, depth: int):
    if node is None:
        return
    ## base case
    if depth == 0:
        print(node.value, end=" ")  # we and end=(" ") because print by default adds
        return  # to it end "\n" and that create a new line and
        # since we are looking for a straight
        # line return of a depth return, we do end
        # =(" ") so it just give a space

    print_node_at_depth(node.left, depth - 1)
    print_node_at_depth(node.right, depth - 1)


# compexity
# Time : O(n)
# space : O(n)

## We do the line above so depth only returns value in the depth line


def binary_tree_print_in_order_brute_force(root: BinaryTreeNode):

    height = tree_height(root)

    for h in range(height + 1):

        print_node_at_depth(root, h)

        print()


## This is
# Time O(n*h)
# in the worst case where we have a single line but have 1 left 2 left 3
# h = n
# Time is O(n^2)
# Space O(n) because of recursion

a = BinaryTreeNode("A")
b = BinaryTreeNode("B")
c = BinaryTreeNode("C")
d = BinaryTreeNode("D")
e = BinaryTreeNode("E")

a.left = b
a.right = c

b.left = d
b.right = e

binary_tree_print_in_order_brute_force(a)


## Now lets go to the optimized approach
# What we do here will feel like magic but yakubu manage !!

# we would use a deque package(basically an inbuilt python que)
# count queue size
# process exactly that many nodes
# print newline
# continue


def binary_tree_print_in_order_optimized(root):
    if root is None:
        raise IndexError("This node does not exist")

    queue = deque([root])

    while queue:

        lenght = len(queue)

        for _ in range(lenght):

            current = queue.popleft()

            print(current.value, end=(" "))

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        print()


print("This is the optimized bit")

binary_tree_print_in_order_optimized(a)

## complexity
# Time O(n)
# Space (n)
