# Problem 8.4: Implement a function which takes as input a pointer to the head of a
# postings list L, and returns a copy of the postings list. Your function should take O(n)
# time, where n is the length of the postings list and should use O(1) storage beyond
# that required for the n nodes in the copy. You can modify the original list, but must
# restore it to its initial state before returning.


## Brute force


# Stage 1
# Here we created the Posting Node
# Made to have posting and next defauted to None
class PostingListNode:
    def __init__(
        self,
        value: int,
        posting: "PostingListNode | None" = None,
        next: "PostingListNode | None" = None,
    ):
        self.posting = posting
        self.next = next
        self.value = value


# Stage 2
# This was to copy the first or main list
# We aimed to do this by creating a PostListNode with the values of the main list
# This way we only collect the value while creating a new instace of a node in memory
def copy_a_linked_list(head: PostingListNode):
    dummy_head_copy = PostingListNode(0)
    dummy_head_copy_tail = dummy_head_copy
    current = head

    while current is not None:
        dummy_head_copy_tail.next = PostingListNode(current.value)
        dummy_head_copy_tail = dummy_head_copy_tail.next
        current = current.next
    ## Remember to push the dummy head forward to the main head
    copied = dummy_head_copy.next

    ## Stage 3
    # Here we aim to transverse the the main and the copied list simultaneously as we locate the postings and then
    # record them for the copied list
    copied_current = copied
    current = head

    while current is not None:
        target = current.posting
        # The special variables will transverse from the head over and over every time we locate a
        # posting and align it in the copied list
        special_current = head
        special_copied = copied
        # the while loop that will locate the target by transversing the main list
        # and looking to find the target and once found having being going simultanouesly
        # with the copied hence the will be at the same spot hence holding the current copied's target as well
        while target != special_current:
            special_current = special_current.next
            special_copied = special_copied.next
        # So we come here and point the current copied node to its posting node
        copied_current.posting = special_copied

        # then we next the coppied current to the next node as well as
        # the transversing current which is a pointer from the main list
        copied_current = copied_current.next
        current = current.next

    return copied


## Optimized approach
# This takes a very clever approach where we shall nest the copy into the main and then derive it's postings
# then go ahead to seperate it


def optimized_copy_a_linked_list(head: PostingListNode):
    if head is None:
        return None

    current = head
    ## Stage one
    # Here we intertwing the two lists to create another larger list where we have a node mix of
    # Main node --> copied node
    # A --> A' --> B --> B'
    while current:
        fwd = current.next
        current.next = PostingListNode(current.value)
        current.next = fwd
        current = fwd

    ## Stage two
    ## Here we take it a step further where we udpdate the copied nodes with there postings or jump pointers
    # with ref from the main list nodes
    mixed_list = head

    while mixed_list:
        copied = mixed_list.next
        if mixed_list.posting:
            copied.posting = mixed_list.posting.next
        mixed_list = copied.next

    ### Part 3
    ## Here we then seperate the two of them from one another and go ahead to return the copied list
    completed_mixed_list = head

    # copied_list_head = PostingListNode(0)
    # copied_list = copied_list_head

    copied_head = head.next

    # while completed_mixed_list.next:
    while completed_mixed_list:
        copied = completed_mixed_list.next

        completed_mixed_list.next = copied.next

        if copied.next:
            copied.next = copied.next.next

        completed_mixed_list = completed_mixed_list.next

        # fwd = completed_mixed_list.next
        # completed_mixed_list.next = fwd.next
        # copied_list.next = fwd
        # completed_mixed_list = completed_mixed_list.next
        # copied_list = copied_list.next

    return copied_head.next


### Lesson from this problem:
### Sometimes the fastest lookup is not a hashmap — sometimes you temporarily change
### the structure so the answer becomes one pointer away.
