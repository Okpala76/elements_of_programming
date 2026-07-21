#  19.3_Transform-one_string_to_another
#  Given a dictionary D and two strings s and t, write a function to
# determine if s produces t. Assume that all characters are lowercase alphabets. If
# s does produce t, output the length of a shortest production sequence; otherwise,
# output −1.


# This is a classic one, why?
# vertices  the wrong and it s changes to the right word
# edges the variation btw the ast and the next word on the sequence
# no weighted
# implcit

# Brute force will not use and patterns first


from math import inf


def differs_by_one(first: str, second: str) -> bool:
    if len(first) != len(second):
        return False

    differences = 0

    for first_char, second_char in zip(first, second):
        if first_char != second_char:
            differences += 1

            if differences > 1:
                return False

    return differences == 1


def string_transform_brute_force(
    s: str,
    t: str,
    D: set[str],
) -> int:
    words = set(D)

    if len(s) != len(t):
        return -1

    if s not in words or t not in words:
        return -1

    if s == t:
        return 0

    current_path = {s}

    def helper(current: str) -> float:
        if current == t:
            return 0

        shortest = inf

        for candidate in words:
            if candidate in current_path:
                continue

            if not differs_by_one(current, candidate):
                continue

            current_path.add(candidate)

            remaining_steps = helper(candidate)

            if remaining_steps != inf:
                shortest = min(shortest, 1 + remaining_steps)

            # Backtrack so another route may use candidate.
            current_path.remove(candidate)

        return shortest

    result = helper(s)

    return -1 if result == inf else int(result)


# Complexity
# This is exponential we have l = words in the dictionary
# O(n^n) * O(w) for word comparison
# a safe place to base it is O(n^n)

# Space
# The set D is spaced the number of words
# O(w)

from collections import deque
from string import ascii_lowercase


def string_transform(
    s: str,
    t: str,
    D: set[str],
) -> int:
    words = set(D)

    if len(s) != len(t):
        return -1

    if s not in words or t not in words:
        return -1

    if s == t:
        return 0

    queue = deque([(s, 0)])

    # Removing a word means it has been visited.
    words.remove(s)

    while queue:
        current_word, transformations = queue.popleft()

        characters = list(current_word)

        for index in range(len(characters)):
            original_character = characters[index]

            for new_character in ascii_lowercase:
                if new_character == original_character:
                    continue

                characters[index] = new_character
                candidate = "".join(characters)

                if candidate not in words:
                    continue

                # Mark visited immediately when adding to the queue.
                words.remove(candidate)

                if candidate == t:
                    return transformations + 1

                queue.append((candidate, transformations + 1))

            # Restore the character before processing the next position.
            characters[index] = original_character

    return -1


# Complexity
# Time l = lent of each word, d = number of words
# we go l * 26 for each check
# then l*26 * d
# hence we have dl
# but time to process( contruct and cache each code

##### characters[index] = new_character
#####                 candidate = "".join(characters)

#  is  another O(l) hence l*l l^2
# so we record dl^2
# why not 24dl^2? becase complexity does not regard constants


if __name__ == "__main__":
    D = {
        "cat",
        "cot",
        "cog",
        "dog",
    }
    print(string_transform("cat", "dog", D))
