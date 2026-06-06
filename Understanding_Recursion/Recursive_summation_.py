# The idea behind this problem is to recognize a pattern.
#
# A nested list can contain:
# 1. Single values (integers)
# 2. Other lists
#
# Since a nested list is simply a smaller version of the same problem,
# recursion becomes a natural solution.


def recursive_summation_nested_list(l: list):
    total = 0

    for value in l:

        # If we encounter another list,
        # we have discovered the same problem again.
        if isinstance(value, list):
            total += recursive_summation_nested_list(value)

        # Otherwise, we have reached a value that can
        # be added directly to the total.
        else:
            total += value

    # Every recursive call eventually returns
    # the sum it calculated.
    return total


print(recursive_summation_nested_list([1, [2, 3], [4, [5]]]))

# Complexity
# Time O(n)
# Space O(n)


# recursive_summation([1, [2, 3], [4, [5]]])
# │
# ├── 1
# │
# ├── recursive_summation([2, 3])
# │   ├── 2
# │   └── 3
# │   → 5
# │
# └── recursive_summation([4, [5]])
#     ├── 4
#     └── recursive_summation([5])
#         └── 5
#     → 9
# │
# → 15
