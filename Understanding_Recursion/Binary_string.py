###the brute force is also not possible we cant tell number of iterations before hand
#
# hence  brute force attempt , i thing fo base case first and that would be a situation wher ethe current list has same lent as the n numer  at that point we know that list is complete
#
#  and anything asides that we would loop through until our while increasing curent value till we get  current value over the 1 size
#


def binary_possiblities(n: int):
    result = []

    def backtracking(index: int, current_list: list):
        if len(current_list) == n:
            result.append(current_list.copy()) ## This was missing in my solution and i missed it .copy() this as make my returned values an empty array becase i did. pop later 
            return
        current_value = 0
        while current_value < 2:
            current_list.append(current_value)
            backtracking(index + 1, current_list)
            current_list.pop()
            current_value += 1

    backtracking(0, [])

    return result


print(binary_possiblities(2))
