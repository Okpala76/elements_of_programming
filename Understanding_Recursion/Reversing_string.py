## The brute force first


import re


def brute_force_reversing_string(s: str):
    result = ""
    for x in range(len(s) - 1, -1, -1):
        result += s[x]


## Thinking
## recursive apparc=oach will have us add the first letter recursively to the the recursive call of the rest of the string that is [1::]
# the sequnce contiunois untill we have a single char string the we return hat and have a golden day 


def recursive_reverse_string(s: str):
    ## base case
    if len(s) <= 1:
        return s
    return recursive_reverse_string(s[1::]) + s[0]


print(recursive_reverse_string("cat"))


## The big o of the bruteforce is  n^2 becase we do string concetination and that creates the sting every time it cncs it
## the big O of the recursion also has the the same big(n^2 becase we do concactetion on all steps )