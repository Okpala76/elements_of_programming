# 11.3 Compute the median of online data
# You want to compute the running median of a sequence of numbers. The sequence
# is presented to you in a streaming fashion—you cannot back up to read an earlier
# value, and you need to output the median after reading in each new element.
# Problem 11.3: Design an algorithm for computing the running median of a sequence.
# The time complexity should be O(log n) per element read in, where n is the number
# of values read in up to that element.


## Brute force will be a few steps

# Hold a list that will return held streams --- already a bad omen
# calcualte median off the sorted stream list
# print the median


from shutil import move

from more_itertools import side_effect


def sort_und_median(stream_list):
    stream_list = sorted(stream_list)

    if len(stream_list) % 2 == 0:
        return (
            stream_list[len(stream_list) // 2]
            + stream_list[(len(stream_list) // 2) - 1]
        ) / 2
    return stream_list[(len(stream_list) // 2)]


def median_online_data(stream: list):
    # O(n) space complexity
    stream_list = []

    # O(n) time
    for data in stream:
        # O(1) time
        stream_list.append(data)
        # (n^2 log n) time because of compounding sorts
        print(sort_und_median(stream_list))


# Time Complexity  O(n**2 Log n)
# Space Comlexity  O(n)

## Optimized approach
# concept is the use of two heaps
# one for the right side and the other for the left side
# a max on the left and a min on the right
# this develops a direct access to the middle value

import heapq


def median_online_data_op(stream):
    left = []
    right = []

    for data in stream:
        # Invariant 1
        if not left or data <= -left[0]:
            heapq.heappush(left, -data)
        else:
            heapq.heappush(right, data)

        # Invariant 2
        if (len(left) - len(right)) > 1:
            moved = -heapq.heappop(left)
            heapq.heappush(right, moved)

        elif len(right) > len(left) + 1:
            moved = heapq.heappop(right)
            heapq.heappush(left, -moved)

        # Step 3: Compute median
        if len(left) == len(right):
            median = ((-left[0]) + right[0]) / 2

        elif len(left) > len(right):
            median = -left[0]

        else:
            median = right[0]

        print(median)


## Complexity
# Each heapq.heappush operation: O(log n)

# Each heapq.heappop operation: O(log n)

# For each element, you do at most 2 pushes and 2 pops (when rebalancing)

# Overall for n elements: O(n log n)
# Space = O(n)

if __name__ == "__main__":
    ## Brute force
    median_online_data_op([10, 2, 3, 15, 15])
