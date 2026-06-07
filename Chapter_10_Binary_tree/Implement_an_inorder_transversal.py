## Problem 10.3: Let T be the root of a binary tree in which nodes have an explicit
# parent field. Design an iterative algorithm that enumerates the nodes inorder and
# uses O(1) additional space. Your algorithm cannot modify the tree. pg. 130

# In this problem we do the inorder transversal with restrictions
# - No recursion
# - No Stack
# - O(1)

# But first we are going to start with the brute force
# of this solution

## we understand that inorder speaks to an order as Left --> root --> Right (LR'R)

# Brute Force

from Test_if_a_tree_is_balanced import BST, a


def inorder_transversal(root: BST):
    if root is None:
        return None

    left = inorder_transversal(root.left)
    print(root.value)
    right = inorder_transversal(root.right)


print("This is recursive")
inorder_transversal(a)

# this would be
# Time O(n)
# Space (n) balanced O(log(n))


## iterative 


def inorder_transversal_stack(root: BST):
    current = root
    stack = []

    # 1st iterative case
    while stack or current:

        # We want to first go to the leftest node
        while current:
            stack.append(current)
            current = current.left

        # want to print out values
        current = stack.pop()

        print(current.value)

        ## then we will go ahead to the visit the right

        current = (
            current.right
        )  # the right is the last articl because?   we are doing an inorder transversal LR'R


print("This is iterative")
inorder_transversal_stack(a)

# Complexity
# Time O(n) all nodes visited atleast once
# Space O(n)   growing stack in relaton to opiawuni

# push A
# push B
# push D

# pop D -> visit D

# pop B -> visit B

# push E

# pop E -> visit E

# pop A -> visit A

# push C

# pop C -> visit C


## Optimization now to stay with all constriants
# - No recursion
# - No Stack
# - O(1)


def inorder_transversal_op()