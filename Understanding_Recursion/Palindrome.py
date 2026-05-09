## This solution requires us to look at the indexing at opposite ends of the string to see if it has talling values at those indics


def palindrone(s: str, index: int = 0):
    ## edge case
    if len(s) == 0:
        raise ValueError(" this string bears no values")
    ## base case
    if index == (len(s) // 2):
        return True
    ## recursive case
    if (
        s[index] == s[-(index + 1)]
    ):  ## I made an error of not adding one to th reverse index .. this was wrong because backward index [-3,-2,-1] is diff from forward [0,1,2]
        return palindrone(s, index + 1)
    else:
        return False


print(palindrone("heseeh"))


##This was a very intrestiing one if you ask me and chat gpt did not say single thing about its optimiation
## O(n) for both space and time complexity
