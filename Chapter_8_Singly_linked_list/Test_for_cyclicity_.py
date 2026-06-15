# Problem 8.3: Given a reference to the head of a singly linked list L, how would you
# determine whether L ends in a null or reaches a cycle of nodes? Write a function
# that returns null if there does not exist a cycle, and the reference to the start of the
# cycle if a cycle is present. (You do not know the length of the list in advance.) pg. 119

## This is a more straight forward from my first look perspective,
# I immediately saw that
#  - this is a boolen output
#  - this is going to be cyclic if
#                           - the next of the last node points to a node within the list
#                           - the transversers next value does not gives a null value

# Hence my solution
from Merge_two_sorted_list_ import build_linked_list
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

    # handle tail itself being the cycle_start
    # so after transversing in the above while loop the index value will hold the traditional index of the last value,
    # hence if that is the same index we pass as our cycle index then index value will be at it,
    #  we just need to point current to it
    # .. which is what we do

    if index == cycle_index:
        cycle_start = current
        current.next = cycle_start

    else:
        if cycle_start is None:
            raise IndexError("The selected index is out of bounds")
        current.next = cycle_start

    # then we return the head value so that it returns the list as edited from its head
    return head


# Brute force


def is_cyclic(head: ListNode):

    seen_nodes: list[ListNode] = []
    current = head

    while current is not None:
        if current in seen_nodes:
            return current

        seen_nodes.append(current)
        current = current.next

    return False


## So we create a linked list twice because a linked list is mutable and can't be reused over operations after being mutated just like a list being instanciated and the being poped or append to
## Optimzation is
# # Time O(n**2)  while loop and search
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


# One thing I learnt is that always remember that Nodes are unique
# values on there own not just the content.. more like classes

# complexity
# Time O(n) Set lookup is O(1) on average, so each node is checked once
# Space O(n) Storing all nodes

## Now lets cook the floyd opawuni
## Floyd's Cycle Detection (Tortoise and Hare)
## Slow and Fast pointer


def flodys_slow_fast_pointer(head: ListNode):

    slow = head
    fast = head

    ## we do while fast and fast.next because that is the
    # only point where we are sure fast.next.next is either a node or None
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            break
    ## because if the while loop fail means that
    #  a None must have been found in fast.next.next
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

if __name__ == "__main__":

    # Test Case 1: Purely linear list
    # normal_linked_list = build_linked_list([1, 2, 3])
    # print(
    #     "this is the brutiest force",
    #     is_cyclic(normal_linked_list),
    # )  # Output: False

    # Test Case 2: A completely separate cyclic list
    another_list = build_linked_list([4, 5, 6])
    # print(build_cyclic_linked_list(another_list, 2))

    cyclic_list = build_cyclic_linked_list(another_list, 2)
    print("Brute force: is this is list cyclic?", is_cyclic(cyclic_list))

    ## optimized
    # Test Case 1: Purely linear list
    # normal_linked_list = build_linked_list([1, 2, 3])
    # print(
    #     "This is the set optimized example", is_cyclic_set_optimized(normal_linked_list)
    # )  # Output: False

    # # Test Case 2: A completely separate cyclic list
    # another_list = build_linked_list([4, 5, 6])
    # cyclic_list = build_cyclic_linked_list(another_list, 1)
    # print("This is the set optimized example", is_cyclic_set_optimized(cyclic_list))

    ## we have an optimization that uses set since sets are built of hash tables and we are making use of unique values in Nodes we can effectively use this and make our optimazaton
    # Time O(n) while loop, search is na hashed by using a set so that is O(1)
    # Space: O(n) growing seen_nodes

    ## Floyds slow fast pointer

    # Test Case 1: Purely linear list
    # normal_linked_list = build_linked_list([1, 2, 3])
    # print(
    #     "This is the floys optimized example", flodys_slow_fast_pointer(normal_linked_list)
    # )  # Output: False

    # # Test Case 2: A completely separate cyclic list
    # another_list = build_linked_list([4, 5, 6])
    # cyclic_list = build_cyclic_linked_list(another_list, 1)
    # print("This is the floyds optimized example", flodys_slow_fast_pointer(cyclic_list))
