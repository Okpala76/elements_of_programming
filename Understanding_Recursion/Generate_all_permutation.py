## This solution had me look at the three understand of recursu=ion that opened me up to the understading of recursion and how it helps me cook... so unlike other solution where i had see the concepts before this was diff coz i thought it through using the recursion methd i had learnt
## i.e is base case and recursion case
## the base case was ease a bit and it also informed me how the recursion case will look.. what do i mean?
## i new that the base case will be when the current list becomes the len of the arr so an append to the result will have to happen
## and the  this lead me to the undersatnding that a back track will be required hence the pop on every call
## then the recursion state which is straight forward


def generate_all_permutation(arr: list):
    result = []

    def backtracking(index: int, current_list: list):
        # base case
        if len(arr) == index:
            return result.append(current_list.copy())

        for i in range(len(arr)):
            if arr[i] not in current_list:
                current_list.append(arr[i])
                backtracking(index + 1, current_list)
                current_list.pop()

    backtracking(0, [])
    return result


print(generate_all_permutation(["a", "b", "c"]))
