# Problem 10.2: Design an efficient algorithm for computing the LCA of nodes a and
# b in a binary tree in which nodes do not have a parent pointer.

# What we wish to know
# Invariants
# Patterns
# Complexity

# first a function to find the path to each node and store that in a list

from tabnanny import check
from turtle import right

from Test_if_a_tree_is_balanced import BST

a = BST("A")
b = BST("B")
c = BST("C")
d = BST("D")
e = BST("E")
f = BST("F")
g = BST("G")


a.left = b
a.right = c

b.left = d
b.right = e
c.left = f
c.right = g


def find_path(root: BST, node: BST):
    dir = []

    def checker(current: BST):
        ## if we hit None
        if current is None:
            return False

        # check is its the node we are looking for
        if current is node:
            return True

        dir.append("L")
        if checker(current.left):
            return True
        else:
            dir.pop()

        dir.append("R")
        if checker(current.right):
            return True
        else:
            dir.pop()

        return False

    checker(root)
    return dir


def lowest_common_ancestor(root: BST, A: BST, B: BST):
    path_to_A = find_path(root, A)
    path_to_B = find_path(root, B)

    i = 0
    current = root

    while (i in range(len(path_to_B) - 1) or i in range(len(path_to_A) - 1)) and (
        path_to_A[i] == path_to_B[i]
    ):
        direct = path_to_A[i]

        if direct == "L":
            current = current.left
        if direct == "R":
            current = current.right

        i += 1

    return current


print(lowest_common_ancestor(a, d, g).value)


### Now let use seek optimization
## Post Order transversal
# Buttom up information Gathering


def lowest_common_ancestor_op(root: BST, A: BST, B: BST):
    current = root
    lca = None

    def helper(current):
        nonlocal lca

        if current is None:
            return 0

        left_count = helper(current.left)
        right_count = helper(current.right)

        self_count = 0
        if current == A or current == B:
            self_count += 1

        total = left_count + right_count + self_count

        if total == 2 and lca is None:
            lca = current

        return total

    helper(current)
    return lca


print(lowest_common_ancestor_op(a, d, e).value)


# Bruteforce
# "How do I get from the root to each node?"

# Optimization
# "What useful information can each subtree return upward?"

# This is actually one of those EPI problems where the optimization is not mainly about Big-O time.
