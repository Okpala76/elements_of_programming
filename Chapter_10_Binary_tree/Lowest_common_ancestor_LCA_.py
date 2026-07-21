# Problem 10.2: Design an efficient algorithm for computing the LCA of nodes a and
# b in a binary tree in which nodes do not have a parent pointer.

# What we wish to know
# Invariants
# Patterns
# Complexity

# first a function to find the path to each node and store that in a list

from Test_if_a_tree_is_balanced_ import BST, a, d, e


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
    if checker:
        return dir
    else:
        return IndexError("node not found in tree")


print(find_path(a, d))


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


## Complexity
# find path:
# Time O(n) Because this is BT and not BST we have to search all to find the node
# and worst case is that we go round the entire tree
# Space O(h) the worst case will have the list populated
# to values the height of the three as we append and pop


# LCA Complexity
# Time: O(n) but O(2n+ h) becuse we do path_find twice and then we iterate the tree a
# a third time to see where our paths align and that worst case is the lenght of the list
# Hence O(n) + O(n) + O(h) == O(n)

# Space: find path O(h) and O(1) == O(h)

# Final
# Time = O(n)
# Space = O(h)


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


# Bruteforce
# "How do I get from the root to each node?"

# Optimization
# "What useful information can each subtree return upward?"

# This is actually one of those EPI problems where the optimization is not mainly about Big-O time.
# Time is O(n) : as we go through the entire list once
# Space is O(n): recursion

if __name__ == "__main__":
    # print(lowest_common_ancestor(a, d, e).value)
    print(lowest_common_ancestor_op(a, d, e).value)
