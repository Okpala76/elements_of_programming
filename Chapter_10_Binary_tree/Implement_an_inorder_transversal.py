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

from Test_if_a_tree_is_balanced_ import BST, a

a = BST("4")
b = BST("2")
c = BST("6")
d = BST("1")
e = BST("3")
f = BST("5")
g = BST("7")

a.left = b
a.right = c

b.left = d
b.right = e
c.left = f
c.right = g  ## comment this and print for false return


def inorder_transversal(root: BST):
    if root is None:
        return None

    left = inorder_transversal(root.left)  # none
    print(root.value)
    right = inorder_transversal(root.right)


# print("This is recursive")
# inorder_transversal(a)

# Complexity
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
        )  # the right is the last article because?   we are doing an inorder transversal LR'R


# print("This is stack")
# inorder_transversal_stack(a)

# Complexity
# Time O(n) all nodes visited atleast once
# Space O(n)

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
# - O(1) space

# This guy would use a man called Morris transversal
# an in genius way to use ur tree as a stack or memory


def inorder_transversal_op(node: BST):
    current = node

    # Because our base case will have current end at None
    while current:
        # We can boldly move right because we know the only situation where
        # right will be None will be the end
        # if its not the end it will be pointing back to a prev current
        if current.left is None:
            print(current.value)
            current = current.right  # we return the current to a prev current

        else:
            predecessor = current.left

            # so transverse till you meet the end of the right nodes(the rightmost Node)
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right

            # this is the dicovery leg- here we find the IP(inorder predecessor)
            # and by pointing it to current we now have a way back to that guy
            # we can then go ahead to move the current left ward
            # remember inorder == LR'R
            if predecessor.right is None:
                predecessor.right = current
                current = current.left
            # so what will make it through the first condition will mean this is a second visit
            # to the right-most value in the left subtree(that is the def of IP)
            # therefore we should be looking to detach the pointer to the former head
            else:
                predecessor.right = None
                print(current.value)
                current = current.right


# print("This is the morris transversal")
# inorder_transversal_op(a)

# Complexity
# Time O(n)
# Space O(1)


class BST_parent:
    def __init__(self, value):
        self.value = value
        self.left: "BST_parent | None" = None
        self.right: "BST_parent | None" = None
        self.parent: "BST_parent | None" = None


a = BST_parent(4)
b = BST_parent(2)
c = BST_parent(6)
d = BST_parent(1)
e = BST_parent(3)
f = BST_parent(5)
g = BST_parent(7)

a.left = b
a.right = c
b.parent = a
c.parent = a

b.left = d
b.right = e
d.parent = b
e.parent = b

c.left = f
c.right = g
f.parent = c
g.parent = c


def inorder_transversal_parent(node: BST_parent):
    if not node:
        return

    curr = node
    prev = None

    while curr:
        # if we are going to the left
        if prev == curr.parent:
            if curr.left:
                prev = curr
                curr = curr.left
            else:
                print(curr.value)
                prev = curr
                curr = curr.right if curr.right else curr.parent
        # when coming back from the left
        elif prev == curr.left:
            print(curr.value)
            prev = curr
            curr = curr.right if curr.right else curr.parent
        else:
            # prev == curr.right
            prev = curr
            curr = curr.parent


print("This is the parent pointer traversal")
print(inorder_transversal_parent(a))

# Complexity
# Time : O(n) we visit all nodes at least
# Space: O(1) we hold only variables
