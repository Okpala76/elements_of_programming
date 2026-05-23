# This solution had me look at the three understanding of recursion
#  that opened me up to the understading of recursion and how it helps me cook...
#  so unlike other solution where I had seen the concepts before this was diff coz
#  I thought it through using the recursion method i had learnt
# i.e is base case and recursion case
# the base case was ease a bit and it also informed me how the recursion case will look.. what do i mean?
# I knew that the base case will be when the current list becomes
# the len of the arr so an append to the result will have to happen
# and this lead me to the undersatnding that a back track will be
#  required hence the pop on every call
# then the recursion state which is straight forward


def generate_all_permutation(arr: list):
    result: list[list] = []

    def backtracking(index: int, current_list: list):
        # base case
        if len(arr) == index:
            return result.append(current_list.copy())

        ## recursive case
        for i in range(len(arr)):
            if arr[i] not in current_list:
                current_list.append(arr[i])
                backtracking(index + 1, current_list)
                current_list.pop()

    backtracking(0, [])
    return result


print(generate_all_permutation(["a", "b", "c", "d"]))


def generate_all_permutation_optimization(n: list):
    result: list[list] = []
    used: list = [False] * len(n)

    def backtracking(index: int, current_list: list):
        ## base case
        if index == len(n):
            result.append(current_list.copy())
            return

        ## recursive case
        for i in range(len(n)):
            if used[i]:
                continue

            used[i] = True

            current_list.append(n[i])

            backtracking(index + 1, current_list)

            current_list.pop()

            used[i] == False


# for loop → O(n) --> O(n)
# check → O(n) --> O(1)

# Total → O(n^2) --> O(n)
