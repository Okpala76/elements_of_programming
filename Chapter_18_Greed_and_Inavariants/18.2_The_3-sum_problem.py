# Problem 18.2: Design an algorithm that takes as input an array A and a number t,
# and determines if A 3-creates t.

# A = [1, 3, 5, 7]
# t = 11

# 1 + 1 + 1 = 3
# 1 + 1 + 3 = 5
# 1 + 1 + 5 = 7
# 1 + 1 + 7 = 9
# 1 + 3 + 3 = 7
# 1 + 3 + 5 = 9
# 1 + 3 + 7 = 11

# So simply put check if the problem if 3 sums of values in the list can give you a target value
# our boader check
# - if the min value in A * 3 is greater than target 1+1+1 > 2 so 2 can never go
# - if the max value in A * 3 is lesser than target 7+7+7 < 24 so 7 will never go


# BRUTEFORCE

# Greed Algo: the sumation of three values must be within the bound of the list values 3 summed


def three_sum(A: list, t: int, k: int = 3) -> bool:
    if not A:
        return False
    # bound_cases
    if max(A) * k < t or min(A) * k > t:
        return False

    def helper(count: int, summer: int) -> bool:
        if count == k:
            return summer == t

        for i in range(len(A)):
            if helper(count + 1, summer + A[i]):
                return True
        return False

    return helper(0, 0)


# Complexity
# Time O(n^k) now it is raise to power k because we make n decision k times so this expontial but we know the exponent
# Space O(k) the stack depth = O(1) because we know the stack dept from the begining as k , and k is a constant so with compleity rule we have
# O(1)

# pattern = exhaustive search+ backtracking
# invariant = the summer is the sum count of values of A already read - we derived this from the helper aritty
# Bounds invariant: the target must remain between the minimum and maximum sums reachable from the current branch


# OPTIMIZATION

# we solve using a more technical approach
# here we convert 3-sum to 2-sum
# and then we reduce the target
# this helps us reduce the problem before solving it


def three_sum_op(A: list, t: int) -> bool:
    if not A:
        return False

    def has_two_sum(A: list, remaining_target: int) -> bool:  # O(n)
        left = 0
        right = len(A) - 1

        while left <= right:
            if A[left] + A[right] == remaining_target:
                return True
            elif A[left] + A[right] < remaining_target:
                left += 1
            else:
                right -= 1
        return False

    def has_three_sum(A: list, t: int) -> bool:

        remaining_target = t
        sorted_A = sorted(A)  ## n log n

        for value in sorted_A:  # O(n^2)
            remaining_target -= value

            if has_two_sum(A, remaining_target):  # O(n)
                return True

        return False

    return has_three_sum(A, t)


## Complexity
#  Time = O(n^2)
#  Space = O(1) but the sort create a new stuff O(n)

# pattern = reduce and iterate --> sort + fix one value + two pointers
# invariant = eliminate the left and right poniters based on the remaining_target opiawuni

# When a problem asks for three values, fixing one value can reduce it
# to a simpler two-value problem. Sorting then turns blind searching into controlled elimination.

if __name__ == "__main__":
    print(three_sum_op([2, 4, 2], 8))
