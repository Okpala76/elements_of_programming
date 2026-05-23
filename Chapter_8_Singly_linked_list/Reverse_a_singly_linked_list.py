# Problem 8.2: Give a linear time, nonrecursive function, that reverses a singly linked
# list. The function should use no more than constant storage beyond that needed for
# the list itself.


class ListNode:
    def __init__(self, data: int, next: "ListNode | None" = None):
        self.data = data
        self.next = next


# so we want to take in a funtion that has a node that has it values arrange in ascending order

# solve the simplest problem
# 1 -> 2 -> None
# just switch the value at head with next and none remains we have 2,1, none just as we want it
#
# next we do  1-> 2 -> 3 -> None
# if  create another node list  then i add 1 point head and tail to it and point its next to None
# now when i get a new value(2) i will point head to it  and points its next to tail
# move tail to head
# then recurse
from Merge_two_sorted_list import linked_list_to_list, build_linked_list
## Brute force

def reverse_a_single_linked_list(linked_list: ListNode):
    result = []
    current = linked_list

    while current is not None:
        result.append(current.data)
        current = current.next

    result.reverse()

    return result


built_list = build_linked_list([1, 2, 4, 5, 6])

reversed_list = reverse_a_single_linked_list(built_list)

print(reversed_list)


## the optimized approach that allows you to cook is making use of pointers
# this approach allows you to think of the solution from a real memory POV and this allows you to make use of pointers for the solution
# if we look at this solution we see that a pointer direction change is the solution not data change, Hence
def optimized_reversed_a_singly_linked_list(linked_list: ListNode):
    prev = None
    current = linked_list

    while current is not None:
        ## we execute the change of the next pointer
        next_node = current.next
        current.next = prev
        # Now we have to move pointers accordingly
        prev = current
        current = next_node
    return linked_list_to_list(prev)


built_list = build_linked_list([1, 2, 3, 4, 5])

print(optimized_reversed_a_singly_linked_list(built_list))
