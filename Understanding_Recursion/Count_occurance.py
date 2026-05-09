## The thinking behind this is that i have seen it already so many times because we are simply going to go through each index recursivly and the have a counter hold the amout of times we see a value
## this is going to be O(n) for both time and space
## But i cant shake the feeling of an optimization on the horizon (it is for the itrative implementation)


def count_occurance(string: str, value: str, count: int = 0, index: int = 0):
    ## base case
    if len(string) == index:
        return count

    if string[index] == value:
        count += 1

    ## recursive case
    return count_occurance(string, value, count, index + 1)


## def would have a proper optimization
print(count_occurance("banana", "a"))


## the iterative optimization
def iterative_count_occurance(string: str, value: str):
    count = 0

    for char in string:
        if value == char:
            count += 1

    return count


print("this is the iterative version", iterative_count_occurance("banana", "a"))
