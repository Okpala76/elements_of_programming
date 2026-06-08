## Helper functions to help display answers
class ListNode:
    def __init__(self, data: int, next: "ListNode | None" = None):
        self.data = data
        self.next = next


## This baby helps us create a linked list
def build_linked_list(values: list[int]) -> ListNode | None:
    dummy_head = ListNode(0)
    tail = dummy_head

    for value in values:
        tail.next = ListNode(value)
        tail = tail.next

    return dummy_head.next


## this baby returns a list from the values of a linked list
def linked_list_to_list(head: ListNode | None) -> list[int]:
    values = []

    current_node = head
    while current_node is not None:
        values.append(current_node.data)
        current_node = current_node.next

    return values


# Problem 8.1: Write a function that takes L and F, and returns the merge of L and
# F. Your code should use O(1) additional storage—it should reuse the nodes from
# the lists provided as input. Your function should use O(1) additional storage, as
# illustrated in Figure 8.3. The only field you can change in a node is next.

# Bubble sort works by repeatedly comparing adjacent values.
#
# During each pass, the largest unsorted value "bubbles up"
# to its correct position at the end of the list.
#
# Once a value reaches its final position, we don't need to
# look at it again, so each subsequent pass examines one
# fewer element.

def merge_two_sorted_list(first_list: list, second_list: list):
    # edge cases
    if first_list == None and second_list:
        return second_list
    if second_list == None and first_list:
        return first_list
    if first_list == None and second_list == None:
        return []

    first_list = first_list + second_list
    
    # sort case
    for i in range(len(first_list) - 1):
        for j in range((len(first_list) - 1) - i):
            if first_list[j] > first_list[j + 1]:
                first_list[j], first_list[j + 1] = first_list[j + 1], first_list[j]

    return first_list
# So basically what this sort is doing is that it is bubbling up.
# the greatest value then excludes it at the top and bubbles up the next one.

# print(merge_two_sorted_list([1, 6], [2, 3, 4]))
print(merge_two_sorted_list([5, 6], [2, 3, 4]))
# print(merge_two_sorted_list([], []))


# Space Complexity: O(n + m)
# A new list is created containing all elements from both input lists.

# Time Complexity: O(n + m)
# One pass is made through the combined list.
# Note: this is not a complete bubble sort and does not always produce a sorted result.
# Now i have updated the full bubble sort implemnation and we have complexity as
# O(n+m)^2


## Now we must take into consideration that a we are dealing with a linked list 
# with a linked list
#  and what that means is that we are dealing with nodes


## BruteForce
def merge_two_sorted_node_list(first_list: ListNode, second_list: ListNode):

    values = []
    head = first_list

    while head:
        values.append(head.data)
        head = head.next

    head = second_list
    while head:
        values.append(head.data)
        head = head.next

    value.sort()

    ## now values are fully updated with the data.. we make it noded again

    dummy_head = ListNode(0)
    end = dummy_head.next

    for value in values:
        end.data = ListNode(value)
        end = end.next

    return dummy_head.next


## Optimized version
def merge_two_sorted_node_list(
    first_list: ListNode, second_list: ListNode
) -> ListNode | None:

    dummy_head = ListNode(0)
    tail = dummy_head

    while first_list is not None and second_list is not None:
        if first_list.data <= second_list.data:
            tail.next = first_list
            first_list = first_list.next
        else:
            tail.next = second_list
            second_list = second_list.next

        tail = tail.next

    tail.next = first_list if first_list is not None else second_list

    return dummy_head.next


## So what we did here was from 76 - 77 we instantiated a new node and gave it an intital , placeholder data
## then we went ahead to cook

## in line 79 we made it that when one of the lists are exhausted we will stop
## exhausted doing what?
## ehausted passing its value to the transversing tail
## Now based on the question we know that when one of the listes are exhausted the other list will have
## on value left in it hence why we also collect that with out very own transverser(tail) in line 89
## and the go ahead to return dummy_next becasue we have intatiated it with a placeholder head (0)

first_list = build_linked_list([2, 5, 9])
second_list = build_linked_list([3, 6, 7])


merged_list = merge_two_sorted_node_list(first_list, second_list)


print(linked_list_to_list(merged_list))
