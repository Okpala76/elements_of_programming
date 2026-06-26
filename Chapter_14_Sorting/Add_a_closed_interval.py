# # Problem 14.3: Write a function which takes as input an array A of disjoint closed
# # intervals with integer endpoints, sorted by increasing order of left endpoint, and an
# # interval I, and returns the union of I with the intervals in A, expressed as a union of
# # disjoint intervals.

# # This problem requires us to add a closed interval to a set of disjointed and sorted intervals,
# # in a sense a Union of U and I when i is a interval that will add a range to this Set


# def add_a_closed_interval(U: list[tuple[int, int]], I: tuple[int, int]):
#     result = []

#     count = 0
#     a = b = 0
#     Is, Ie = I

#     while count < len(U):
#         Us, Ue = U[count]

#         if Is <= Ue:
#             if Is <= Us:
#                 a = Is
#                 break
#             a = Us
#             break

#         count += 1
#     else:
#         return U.extend(I)

#     result.append(U[:count])

#     while count < len(U):
#         Us, Ue = U[count]

#         if Ie <= Ue:
#             b = Ue
#             count += 1
#             break
#     else:
#         return result.extend(a, Ie)

#     result.extend((a, b))
#     result.extend(U[count:])

#     return result


from locale import currency


def add_a_closed_interval(U: list[tuple[int, int]], I: tuple[int, int]):
    U.append(I)
    U.sort()

    result = []

    for interval in U:
        if not result:
            result.append(U[0])
        else:
            added_start, added_end = result[-1]
            current_start, current_end = interval

            if current_start <= added_end:
                result[-1] = (added_start, max(added_end, current_end))
            else:
                result.append(interval)

    return result


# complexity
# Time: O(n log n) because of the sort of U , the for is O(n)
# Space: O(n)
#


def add_a_closed_interval_op(U: list[tuple[int, int]], I: tuple[int, int]):

    i = 0

    Is, Ie = I
    result = []

    # we are looking for every interval outrightly less than the I's start
    while i < len(U) and U[i][1] < Is:
        result.append(U[i])

        i += 1

    # we want all intervals that overlap with the I's interval
    while i < len(U) and U[i][0] <= Ie:
        current_start, current_end = U[i]

        Is = min(current_start, Is)
        Ie = max(current_end, Ie)

        i += 1

    # Add the final merged interval. because we only need this one body
    result.append((Is, Ie))

    # we want all intervals that ar outrightly greater than I's interval
    result.extend(U[i:])

    return result


# PS : a way to always understand you code is this debugger tool

# Complexity
# Time: O(n) only one transversaly through the list i.e the i count
# the waste was the sorting
# Space: O(n) the result holder

# Algorithmic pattern
# This is a linear sweep / merge intervals pattern.

# Sorted algo rithms are not supposed to be hard.
# The big lesson here is: when input is already sorted, do not fight it.
# Split the world into before, overlap, and after.
# Most interval problems become easier once you name those three zones.

if __name__ == "__main__":
    U = [(0, 2), (3, 5), (7, 11)]
    I = (3, 10)

    print(add_a_closed_interval_op(U, I))
