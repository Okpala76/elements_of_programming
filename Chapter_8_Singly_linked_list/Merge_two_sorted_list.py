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
        if first_list[i] > first_list[i + 1]:
            first_list[i], first_list[i + 1] = first_list[i + 1], first_list[i]

    return first_list


print(merge_two_sorted_list([1, 6], [2, 3, 4]))
# print(merge_two_sorted_list([], []))


# this solution was done using bubble sort and will be an o(1)
# space implenattion coz we used the same varable that was passed in
# and this is also O(n) time complexity coz with increase in the variable 
# input there is a corresponding increase in run time.


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
