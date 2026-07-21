# Problem 17.3: Design an algorithm for the knapsack problem that selects a subset of
# items that has maximum value and weighs at most w ounces. All items have integer
# weights and values.

# This problem explores a thief who need to make decison on the best items to pick, and he has a limit size he can carry
# hence has to select the best items with weight-value ratio

item_type = list[tuple[int, int]]


def the_knapsack_bruteforce(items: item_type, max_weight: int):
    best_sequence = []
    best_value = 0

    def helper(
        start_index: int = 0,
        curr_sequence: item_type = [],
        curr_value: int = 0,
        curr_weight: int = 0,
    ):
        nonlocal best_sequence, best_value

        # base case
        # a situation where the current value is greater tahn the best value found yet
        if curr_value > best_value:
            best_value = curr_value
            best_sequence = curr_sequence.copy()

        # recursion case
        # So we go through all the values of list a node point(thinking binary tree)

        for i in range(start_index, len(items)):
            item_weight, item_value = items[i]

            new_weight = curr_weight + item_weight

            if new_weight > max_weight:
                continue

            new_value = curr_value + item_value

            curr_sequence.append(items[i])

            helper(i + 1, curr_sequence, new_value, new_weight)

            curr_sequence.pop()

    helper()
    return (best_sequence, best_value)


# Complexity
# Time = O(2^n) because of the exponential recursion of every n item in the list
# Space = O(n * 2^n) now the above still holds true in the Space but n is comming from the continus copy that we do on possible every level deep we go(if the curr_sequnce is steady updated) so yea


# For memoisation we have to understand that our previous implementation does not allow for memoisation, memoisation is only applied to
# recursions that fit bill, one where there can be a repeat and the bruteforcr does not do that.

# here we are going to be applying the skip or take principle as memo is mostly seen in a binary recursion


def the_knapsack_memoisation(items: list[tuple[int, int]], max_weight: int) -> int:

    memo: dict = {}

    def helper(index: int = 0, remaining_weight: int = max_weight) -> int:
        state = (index, remaining_weight)

        # for when we have seen this state before in our tree
        if state in memo:
            return memo[state]

        # for when have the index reach its limit which is the len of items list(one could say the depth of the tree)
        if index == len(items):
            return 0

        item_weight, item_value = items[index]

        # The Skip

        skip = helper(index + 1, remaining_weight)

        # The take
        take = 0

        if item_weight <= remaining_weight:
            take = item_value + helper(index + 1, remaining_weight - item_weight)

        max_value = max(skip, take)

        memo[state] = max_value

        return max_value

    return helper()


# Complexity
# Time O(n *max_weight)
# Space O(n * max_weight)


if __name__ == "__main__":
    print(the_knapsack_memoisation(items=[(2, 3), (4, 5), (1, 5)], max_weight=5))
