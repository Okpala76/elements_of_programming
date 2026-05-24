# Problem 8.3: Given a reference to the head of a singly linked list L, how would you
# determine whether L ends in a null or reaches a cycle of nodes? Write a function
# that returns null if there does not exist a cycle, and the reference to the start of the
# cycle if a cycle is present. (You do not know the length of the list in advance.) pg. 119


## This is a more straight forward on from my first look perspective,
# I immediatlt saw that
#  - this is a boolen output
#  - this is going to be cyclic if
#                           - the next of the last node == the first node of the list
#                           - the transverserss next value does not gives a null value

# Hence my solution
from Merge_two_sorted_list import build_linked_list
from Reverse_a_singly_linked_list import ListNode


def build_cyclic_linked_list(
    head: ListNode,
    cycle_index: int,
) -> ListNode:

    if head is None:
        return None

    current = head
    cycle_start = None

    index = 0

    while current.next is not None:

        if index == cycle_index:
            cycle_start = current

        current = current.next
        index += 1

    # handle tail itself being cycle start
    # so after transversing in the above while loop the index value will hold the traditional index of the last value,
    # hence if that is the same index we pass as our cycle index then index value will be at it we just need to point current to it
    # .. which is what we do

    if index == cycle_index:
        cycle_start = current

    # hence we go ahead to point the current which at this point has to be the value at the last index and point it from none to the cycle_start value
    current.next = cycle_start

    # then we return the head value so that it returns the list as edited from its head
    return head


def is_cyclic(head: ListNode):

    seen_nodes: list[ListNode] = []
    current = head

    while current is not None:
        if current in seen_nodes:

            return current

        seen_nodes.append(current)
        current = current.next

    return None


# Test Case 1: Purely linear list
normal_linked_list = build_linked_list([1, 2, 3])
print(
    "this is the brutiest force",
    is_cyclic(normal_linked_list),
)  # Output: False

# Test Case 2: A completely separate cyclic list
another_list = build_linked_list([4, 5, 6])
cyclic_list = build_cyclic_linked_list(another_list, 1)
print("this is the brutiest force", is_cyclic(cyclic_list))

## So we create a linked list twice because a linked list is mutable and can't be reused over operations after being mutated just like a list being instanciated and the being poped or append to
## Optimzation is
# # Time O(n)  while loop and search
# Space: O(n) growing seen_nodes


def is_cyclic_set_optimized(head: ListNode):

    seen_nodes: list[ListNode] = set()
    current = head

    while current is not None:
        if current in seen_nodes:
            return current

        seen_nodes.add(current)
        current = current.next

    return None


# Test Case 1: Purely linear list
normal_linked_list = build_linked_list([1, 2, 3])
print(
    "This is the set optimized example", is_cyclic_set_optimized(normal_linked_list)
)  # Output: False

# Test Case 2: A completely separate cyclic list
another_list = build_linked_list([4, 5, 6])
cyclic_list = build_cyclic_linked_list(another_list, 1)
print("This is the set optimized example", is_cyclic_set_optimized(cyclic_list))

## we have an optimization that uses set since sets are built of hash tables and we are making use of unique values in Nodes we can effectively use this and make our optimazaton
# Time O(n) while loop, search is na hashed by using a set so that is O(1)
# Space: O(n) growing seen_nodes


# One thing I learnt is that always remember that Nodes are unique values on there own not just the content.. more like classes

## Now lets cook the floyd opawuni
## Floyd's Cycle Detection (Tortoise and Hare)
## Slow and Fast pointer


def flodys_slow_fast_pointer(head: ListNode):

    slow = head
    fast = head

    ## we do while fats and fast.next becase that is the
    # only point where fast.next.next will exist
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            break
    ## because if the while loop fail means that
    #  a None must have been found in fast.next or fast.next.next
    else:
        return None

    slow = head

    while slow is not fast:
        fast = fast.next
        slow = slow.next
    ## because at this point slow will become the cyclic start point
    return slow


## This the solution take the Complexity of
# Time = O(n)
# Space = O(1)

# Test Case 1: Purely linear list
normal_linked_list = build_linked_list([1, 2, 3])
print(
    "This is the floys optimized example", flodys_slow_fast_pointer(normal_linked_list)
)  # Output: False

# Test Case 2: A completely separate cyclic list
another_list = build_linked_list([4, 5, 6])
cyclic_list = build_cyclic_linked_list(another_list, 1)
print("This is the floyds optimized example", flodys_slow_fast_pointer(cyclic_list))
