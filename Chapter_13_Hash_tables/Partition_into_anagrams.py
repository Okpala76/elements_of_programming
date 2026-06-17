## Problem 13.1: Write a function that takes as input a dictionary of English words,
# and returns a partition of the dictionary into subsets of words that are all anagrams
# of each other

# Step 1 (Define problem statement)
# This problem want for us to get a dictionary of word and return there anagrams in groups
#
# Step 2 (identify symbols)
# - Dictionary: a group of words
# - Partition: a divide of the words
# - Subset: a divide of teh words into similar groups
# - Anagram: a word that has the same number count and same letters

# Step three (Small example)
# [me, you, em, uyo]
# This is the should give us an output of
# [[me, em], [you, uyo]]
#
# Step 4 (walk through the example):
#
# Step 5 ( Brute-Force example)


#     subset = set()

#     for word in words:
#         sorted_word = "".join(sorted(word))
#         subset.add(sorted_word)

#     final_words: list[list] = []

#     for ref in range(len(subset)):
#         final_words[ref] = []
#         for word in words:
#             if "".join(sorted(word)) == subset[ref]:
#                 final_words[ref].append(word)


# above is a failed attempt, why did it fail
# we can't instatiate a list with a list like as seen above
# you cant index pick a value from a set like from a list it has a diff structure

# thats basically it

## Brute force take two


def are_anagram(word1: str, word2: str):
    return sorted(word1) == sorted(word2)  # O(k log k) where k = word length


def partition_into_anagrams(words):
    result = []
    used = set()

    for i in range(len(words)):
        ## O(n)

        if i in used:
            continue

        current_words = [words[i]]
        used.add(i)

        for j in range(i + 1, len(words)):
            if j not in used and are_anagram(words[i], words[j]):
                # O(n^2)
                current_words.append(words[j])
                used.add(j)
        result.append(current_words)

    return result


# Time: O(n² × k log k) where:
#   n = number of words
#   k log k = (for the anagram check)
# Space: O(n)


def partition_into_anagrams_op(words):

    sorted_list: dict[list] = {}

    for word in words:

        sorted_word = "".join(sorted(word))  ## log k

        if sorted_word not in sorted_list:
            sorted_list[sorted_word] = []

        sorted_list[sorted_word].append(word)

    return list(sorted_list.values())


# Time = O(n * k log k)
# Space = O(n)


if __name__ == "__main__":
    words = ["me", "you", "em", "uyo"]
    print(partition_into_anagrams_op(words))
