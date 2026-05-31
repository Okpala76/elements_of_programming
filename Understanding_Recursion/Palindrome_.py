## This solution requires us to look at the indexing
#  at opposite ends of the string to see
# if it has talling values at those indics


def palindrome(s: str, index: int = 0):

    # BREAKPOINT 1
    # At this junction we check if the string has any value at all in the first place
    if len(s) == 0:
        raise ValueError("this string bears no values")

    # BREAKPOINT 2
    # Now we call or return true here because if  our index gets
    # to this depth(middle floored) in the tree(or array) then this is a palindrome
    if index == (len(s) // 2):
        return True

    # BREAKPOINT 3
    # This point compare the index and its opposite if they are similar
    # and this make the previous step make more sense coz we are check for similarities
    # from the back and the front of the array
    if s[index] == s[-(index + 1)]:

        # BREAKPOINT 4
        # here we call the function again so we can move our index forward and check
        # opposite index if they are similar
        return palindrome(s, index + 1)

    else:
        # BREAKPOINT 5
        return False


print(palindrome("heseh"))


##This was a very intrestiing one if you ask me and chat gpt did not say single thing about its optimiation
## O(n) for both space and time complexity


# palindrome("heseh", 0)
# │
# ├─ compare h == h ✓
# │
# └── palindrome("heseh", 1)
#     │
#     ├─ compare e == e ✓
#     │
#     └── palindrome("heseh", 2)
#         │
#         ├─ index == len(s)//2
#         │
#         └─ return True