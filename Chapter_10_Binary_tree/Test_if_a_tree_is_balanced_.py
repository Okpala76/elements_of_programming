# Exciting one we are now in BT
# funny how we are getting here now after using this man for so long already
# recursion is his baby by the way and there two are lovers
# apparently, there is a guy called Morris that makes use of pointers to help mitigate the
# space consumption that comes with recursion
#
#
#
#
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
        self.left: "BST | None" = None
        self.right: "BST | None" = None


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
c.right = g  ## comment this and print for false return

if __name__ == "__main__":

    def get_height(node):
        ## Base Case
        if node is None:
            return -1

        ## recursive case
        left = get_height(node.left)
        right = get_height(node.right)

        return 1 + max(left, right)

    def is_balanced(node):

        if node is None:
            return True

        left = get_height(node.left)
        right = get_height(node.right)

        if abs(left - right) > 1:
            return False

        return is_balanced(node.left) and is_balanced(node.right)

    print(is_balanced(a))

    # Time O(n^2)
    # SPace  o(n)

    ### Optimized code
    def is_balanced_op(node: BST | None):
        ## base case
        if node is None:
            return (-1, True)

        ## recursive case
        left_node = is_balanced_op(node.left)
        right_node = is_balanced_op(node.right)

        get_height = 1 + max(left_node[0], right_node[0])

        if not (left_node[1] and right_node[1]):
            return (get_height, False)

        balanced = abs(left_node[0] - right_node[0]) <= 1

        return (get_height, balanced)

    print(is_balanced_op(a)[1])

    ### Agorithm pattern Post-Order Transversal
    # Time O(n) every node is visited
    # Space O(n) every node is visted by recursion.

    # AI Optimized

    def is_balanced_ai(node: BST) -> bool:
        def check_balance(current):
            if current is None:
                return (-1, True)

            left_get_height, left_balanced = check_balance(current.left)
            if not left_balanced:
                return (0, False)

            right_get_height, right_balanced = check_balance(current.right)
            if not right_balanced:
                return (0, False)

            balanced = abs(left_get_height - right_get_height) <= 1
            get_height = 1 + max(left_get_height, right_get_height)

            return (get_height, balanced)

        return check_balance(node)[1]
