# #Problem 9.1: Design a stack that supports a max operation, which returns
#  the maximum value stored in the stack, and throws an exception if the stack is empty. Assume
# elements are comparable. All operations must be O(1) time. If the stack contains n
# elements, you can use O(n) space, in addition to what is required for the elements
# themselves.


# This problem basically stipulates that
# - we need a max value at O(1)
# - throws an exception if the stack is empty
# - assume elements are comparable?
# - all operations must be O(1) i.e pop, append, getMax, peek at head
# - i belive the in addition to ... are the static proces that add to that
#   process but does not affect time or space complexity

## BRUTE FORCE
#   In brute force we are going to do the no brainer and iterate over teh stack to get max


class Max_API_stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if self.stack is None:
            return "This stack is empty"
        return self.stack.pop()

    def append(self, value):
        self.stack.append(value)

    def getMax(self):
        # This is a simple python illustration
        # max(self.stack)
        # - - - - - - - - - - - - - - - -
        # This is a more elaborate one to show transversing through
        # the stacks to find max (more descriptibe of teh O(n) phenomenon)

        max_value = 0
        for i in self.stack:
            max_value = max(max_value, i)
        return max_value

    def peek(self):
        return self.stack[len(self.stack) - 1]


max_stack = Max_API_stack()
max_stack.append(6)
max_stack.append(2)
max_stack.append(4)
max_stack.append(10)

print(max_stack.getMax())

### This is the optimized implementation
# O(1) at all values


class Max_API_stack_optimized:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def pop(self):
        if self.stack is None:
            raise IndexError("This stack is empty")
        self.max_stack.pop()
        return self.stack.pop()

    def append(self, value):
        self.stack.append(value)

        if not self.max_stack:
            self.max_stack.append(value)
        else:
            current = self.max_stack[-1]
            self.max_stack.append(max(current, value))

    def getMax(self):
        # Now the bone of contention, how do make this O(1)?
        ## handle if there has being no appending
        if len(self.max_stack) == 0:
            raise IndexError("No values in stack yet")

        return self.max_stack[-1]

    def peek(self):
        if not self.stack:
            raise IndexError("There is nothing to peek")
        return self.stack[len(self.stack) - 1]


max_stack_op = Max_API_stack_optimized()
max_stack_op.append(6)
max_stack_op.append(2)
max_stack_op.append(4)
max_stack_op.append(10)

print(max_stack_op.getMax())
