# 17.1 Count the number of score combinations
# In an American football game, a play can lead to 2 points (safety), 3 points (field
# goal), or 7 points (touchdown). Given the final score of a game, we want to compute
# how many different combinations of 2, 3, and 7 point plays could make up this score.
# For example, if W = {2, 3, 7}, four combinations of plays yield a score of 12:
# − 6 safeties (2 × 6 = 12),
# − 3 safeties and 2 field goals (2 × 3 + 3 × 2 = 12),
# − 1 safety, 1 field goal and 1 touchdown (2 × 1 + 3 × 1 + 7 × 1 = 12), and
# − 4 field goals (3 × 4 = 12).
# Problem 17.1: You have an aggregate score s and W which specifies the points that
# can be scored in an individual play. How would you find the number of combinations
# of plays that result in an aggregate score of s? How would you compute the number
# of distinct sequences of individual plays that result in a score of s?


# s = 12
# W = [2, 3, 7]

# The combination just speaks of the play score that will amout to the target , not withstanding the sequence of events(order for which the happend. We sort so we dont mix up count of play visually)

# The combinations are:

# [2, 2, 2, 2, 2, 2]
# [2, 2, 2, 3, 3]
# [2, 3, 7]
# [3, 3, 3, 3]

# The Sequence speaks of the possible sequences, these different combinations(above) could be executed in
# #1 only in one possible sequence because it's all twos
# #2 we see 2s and 3s and we see that the possible amount diff sequences we could have is (n)! / ((first play)! * (second play)!)...
# #3 Same here(from number 2) that formula is the killer

# The sequences are
# [2, 2, 2, 2, 2, 2] -> 1 sequence
# [2, 2, 2, 3, 3] -> 5! / (3! * 2!) = 10 sequences    ## This line is so profound
# [2, 3, 7] -> 3! = 6 sequences
# [3, 3, 3, 3] -> 1 sequence


## Brute force
def brute_force_combinations(score: int, plays: list[int]) -> int:
    count = 0

    def helper(index: int, remaining: int):
        nonlocal count

        if index == len(plays):
            if remaining == 0:
                count += 1
            return

        play_score = plays[index]

        max_times = remaining // play_score

        for times in range(max_times + 1):

            helper(index + 1, remaining - times * play_score)

    helper(0, score)
    return count


brute_force_combinations(12, [2, 3, 7])


# Complexity
#  Time = n ^ m
#  where n score , m is the lenght of the plays list or play types
#  Space = O(m)


#  So this function looks to return the sequence count by going through stacks of the height (score//lowest play_mark) and finding where the three play return a 0(meaning that there is a sequence there ) arre truning a one count
def brute_force_sequences(score: int, plays: list[int]) -> int:
    if score == 0:
        return 1

    if score < 0:
        return 0

    total = 0

    for play in plays:
        total += brute_force_sequences(score - play, plays)

    return total


brute_force_sequences(12, [2, 3, 7])


# Complexity
# Time: exponential -- continous recalulation of same elements in three ways
# e.g
# # s = 12
# W = [2, 3, 7]
# ways(2), ways(3), ways(7)

# Space: O(s / min(W)) This is so because the minumum value dividing the score will give us the stack depth
# for an example
# s = 12
# W = [2, 3, 7]

# min(W) = 2 so stack dept will be 6
# 12 -> 10 -> 8 -> 6 -> 4 -> 2 -> 0
# 12 / 2 = 6 == O(s / min(W))


def count_score_combinations(score: int, plays: list[int]) -> int:
    dp = [0] * (score + 1)

    dp[0] = 1

    for play in plays:
        for current_score in range(play, score + 1):
            dp[current_score] += dp[current_score - play]

    return dp[score]


# Complexity
# Time |W|* n worst case is n^2 wgen |w| == n
# Space = O(n)


def count_score_sequences(score: int, plays: list[int]) -> int:
    dp = [0] * (score + 1)

    dp[0] = 1

    for current_score in range(1, score + 1):
        for play in plays:
            if current_score >= play:
                dp[current_score] += dp[current_score - play]

    return dp[score]


print(count_score_combinations(12, [2, 3, 7]))  # 4
print(count_score_sequences(12, [2, 3, 7]))  # 18

# Complexity
# Time = O(n* |w|) worst case is n^2
# Space = O(n)

# Alogo pattern
# Dynamic Programming

# More specifically:

# Unbounded coin change DP

# “Unbounded” means each play score can be used as many times as needed.
