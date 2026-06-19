# Problem 13.2: You are required to write a method which takes an anonymous letter
# L and text from a magazine M. Your method is to return true iff L can be written
# using M, i.e., if a letter appears k times in L, it must appear at least k times in M.

# Basically saying that we have two texts and we want to know if L the constructee, can be constructed by the values(letters)
# in M constructor

# say we have L = "i love you"
# can we contruct that from M = "i love uyo"?

# the answser is yes but if it was L = "madagascar" so the answer will be NO


# Brute force


def is_letter_constructible_brute_force(L: str, M: str) -> bool:
    used = set()

    for char_l in L:
        if char_l == " ":
            continue

        found = False

        for j in range(len(M)):
            if j not in used and char_l == M[j]:
                used.add(j)
                found = True
                break

        if found is False:
            return False

    return True


# Complextity
# Time is O(L * M)
# and worst case we have
# L == M
# therefore
# Time = O(n^2)
# Space = O(n) the set holds all indexs of M


# Optimized


def is_letter_constructible_op(L: str, M: str) -> bool:
    char_count = {}

    # Count characters available in magazine M
    for char in M:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Spend characters needed by letter L
    for char in L:
        if char == " ":
            continue

        if char not in char_count or char_count[char] == 0:
            return False

        char_count[char] -= 1

    return True


# Complexity
# Time = O(l+m) going through all M and the going through all M

# Time complexity is O(l + m), where:
# l = length of the letter
# m = length of the magazine
#
# We do not simplify to O(n) unless we define n as the total input size,
# or unless l and m are known to be about the same size.
# Space : O(m) the dictionary holding all values on m
