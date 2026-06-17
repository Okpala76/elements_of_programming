# Black Ninja defincatly need redo for op
#  This problem tries wants us to firnd the kth term or values from two lists merge
#  So say we have list A and B it wants the kth term of the resultant be term
#
# Brute force pseudo code will be


def search_in_two_sorted_lists(A, B, k):
    idx_a = 0
    idx_b = 0

    C = []
    while idx_a < len(A) and idx_b < len(
        B
    ):  # A[idx_a] and B[idx_b]  No dey use values for conditional use barriers or limits
        if A[idx_a] >= B[idx_b]:
            C.append(B[idx_b])
            idx_b += 1
        else:
            C.append(A[idx_a])
            idx_a += 1

    if idx_a < len(A):
        C.extend(A[idx_a:])

    if idx_b < len(B):
        C.extend(B[idx_b:])

    return C[k - 1]


# complexity
# Time: O(n)
# Space: O(n)


def search_in_two_sorted_lists_slight_op(A, B, k):
    a = b = 0
    count = 0

    while a < len(A) and b < len(B):
        if A[a] <= B[b]:
            current = A[a]
            a += 1
        else:
            current = B[b]
            b += 1

        count += 1

        if count == k:
            return current

    while a < len(A):
        current = A[a]
        a += 1
        count = +1
        if count == k:
            return current

    while b < len(B):
        current = B[b]
        b += 1
        count += 1
        if count == k:
            return current

    return None


# complexity
# Time: O(k)
# Space: O(1)


def search_in_two_sorted_lists_op(A, B, k, a_start=0, b_start=0):

    # A exhausted
    if a_start >= len(A):
        return B[b_start + k - 1]

    # B exhausted
    if b_start >= len(B):
        return A[a_start + k - 1]

    # smallest remaining element
    if k == 1:
        return min(A[a_start], B[b_start])

    half = k // 2

    a_step = min(half, len(A) - a_start)
    b_step = min(half, len(B) - b_start)

    a_pivot = A[a_start + a_step - 1]
    b_pivot = B[b_start + b_step - 1]

    if a_pivot <= b_pivot:
        return search_in_two_sorted_lists_op(
            A,
            B,
            k - a_step,
            a_start + a_step,
            b_start,
        )
    else:
        return search_in_two_sorted_lists_op(
            A,
            B,
            k - b_step,
            a_start,
            b_start + b_step,
        )


# Complexity
# Time O(log k)
# Space O(log k) can be one if we use an iterative approach


if __name__ == "__main__":
    print(search_in_two_sorted_lists_slight_op([1, 5], [5, 8, 10], 5))
