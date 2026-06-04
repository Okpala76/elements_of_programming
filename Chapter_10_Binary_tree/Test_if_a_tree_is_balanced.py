# Exciting one we are now in the BST
# funny how we are getting here now after using this man for so long already
# recursion is his baby by the way and there two are lovers
# apparently there is a guy called Morris that makes use of pointers to help mitigate the
# space consumption that comes with recursion
#
#
#
#
# Now lets get into it for test opiawuni
#
# 10.1 Test if a binary tree is balanced
# A binary tree is said to be balanced if for each node in the tree, the difference in the
# height of its left and right subtrees is at most one. A perfect binary tree is balanced,
# as is a complete binary tree. A balanced binary tree does not have to be perfect or
# complete
# Image of a balanced tree is found in this folder
#
# BRUTE FORCE APPROACH


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def height(node):
    ## Base Case
    if node is None:
        return -1

    ## recursive case
    left = height(node.left)
    right = height(node.right)

    return 1 + max(left, right)


def is_balanced(node):

    if node is None:
        return True

    left = height(node.left)
    right = height(node.right)

    if abs(left - right) > 1:
        return False

    return is_balanced(node.left) and is_balanced(node.right)


a = BST("A")
b = BST("B")
c = BST("C")
d = BST("D")
e = BST("E")
f = BST("F")

a.left = b
a.right = c

b.left = d
b.right = e
e.left = f  ## comment this and print for false return

print(is_balanced(a))
