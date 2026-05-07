## The Highest number in the list pile is the bone of contention and we see this well. take a manupulation of values with the recusive function but how(we'll find out)
#  My solution is one that drew knowledge from the last implemenataion


def find_highest(arr: list, highest: int = 0, index: int = 0):
    # base case
    if len(arr) == index:
        return highest  ### i had returned zero instead of the highest value i had found

    if highest < arr[index]:
        highest = arr[index]

    return find_highest(
        arr, highest, index + 1
    )  ## I never returned the call on the recursive case


print(find_highest([1, 3, 7, 3, 9]))

## this will easily be O(n)

## AI optimized version

## Now this is more deep and precise.. its almost as if i over complicate things
## But before i blow my self up lets get into it


def find_highest_2(arr: list, index: int = 0):
    if len(arr) == 0:
        raise ValueError("This array can not be empty")
    ## base case
    if len(arr) - 1 == index:
        return arr[index]

    highest_rest = find_highest_2(arr, index + 1)

    return max(arr[index], highest_rest)


print(find_highest_2([1, 2, 33, 44, 2]))

# This is easily O(n) on bothe space and time complexity