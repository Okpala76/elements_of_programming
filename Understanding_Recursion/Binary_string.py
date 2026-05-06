###the brute force is also not possible we cant tell number of iterations before hand   WRONG.. see reason below
#
# hence  brute force attempt , i thing fo base case first and that would be a situation wher ethe current list has same lent as the n numer  at that point we know that list is complete
#
#  and anything asides that we would loop through until our while increasing curent value till we get  current value over the 1 size
#


def binary_possiblities(n: int):
    result = []

    def backtracking(index: int, current_list: list):
        if len(current_list) == n:
            result.append(
                current_list.copy()
            )  ## This was missing in my solution and i missed it .copy() this as make my returned values an empty array becase i did. pop later
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


# Alternative implementation


def binary_possiblities(n: int):
    result = []

    def backtracking(current_list: str):
        if len(current_list) == n:
            result.append(current_list)
            return

        backtracking(current_list + "0")
        backtracking(current_list + "1")

    backtracking("")

    return result


print(binary_possiblities(2))


## Quick thinking correction this is the brute force becasue it goes through every iteration to thet the values just that it did it using loop


## For big(O) when we store result values we have (n* 2^n)
#
# but here we have
#
def generate_binary(n):

    def helper(current):

        if len(current) == n:
            print(current)
            return

        helper(current + "0")
        helper(current + "1")

    helper("")


generate_binary(2)

# here we dont save the binary before return we just go ahead to print continually till exaustion
# just like concatianation or slcing is an o(n) in time for execution also is storying an copying
# hence why we have O(n*2^2) instead on O(2^n)
