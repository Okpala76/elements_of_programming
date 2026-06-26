# Problem 14.2: Given a set of n events, how would you determine the maximum
# number of events that take place concurrently?

# this want us to return a count of the maximum number of overlapping events

# we reason for with invariants, what makes a range overlap

# example  (0,5), (3,6)
# (1) start_1 < start_2
# (2) end_1 > start_2

# once we have this invariants btw values we are golden

# hence, BRUTE_FORCE


def render_a_calender_concurrent_count(events: list[tuple[int, int]]):
    max_event = 0

    for event in events:
        count = 0
        s_1, e_1 = event

        for j in events:
            if event == j:
                continue
            s_2, e_2 = j

            if s_1 <= e_2 and s_2 <= e_1:
                count += 1

        max_event = max(max_event, count)

    return max_event


# Complexity
# Time = O(n^2)
# Space = O(1)


def render_a_calender_concurrent_count_op(events: list[tuple[int, int]]):
    max_count = 0

    endpoints = []

    for start, end in events:
        endpoints.append((start, 1))
        endpoints.append((end, -1))

    # Now we want to sort and also ensure that start comes
    # before end in a case where we compare start and end of same value
    # i.e (5, 1) and (5, -1) we need the latter first i.e (5, -1) first, the endpoint first

    endpoints.sort(
        key=lambda x: (
            # this is basically saying sort by x as the key where x[0] is the primary sort while -x[1] is the sec sort
            x[0],  # primary sort
            -x[1],  # secondary sort -- for when prmary is similar
        )
    )
    # Start event: (5, 1)

    # End event: (5, -1)

    # The secondary sort key -x[1] transforms them:

    # Start: -1 (from -(1))

    # End: 1 (from -(-1))

    # Since -1 < 1, the start event comes first in the sorted order.

    count = 0

    for time, type in endpoints:
        if type == 1:
            count += 1
            max_count = max(count, max_count)
        else:
            count -= 1

    return max_count


# PS the line  endpoints.sort(key=lambda x: (x[0], -x[1])) can be better written as
#   def sort_key(item):
#     time, event_type = item
#     return (time, -event_type)

# endpoints.sort(key=sort_key)


# Complexity
# Time = O(n log n) the sorting process
# Space = O(n) the enpoint array

# This is the:

# Sweep line algorithm

# Or more beginner-friendly:

# Sort events by time, then walk from left to right while maintaining an active count.

if __name__ == "__main__":
    events = [(1, 5), (3, 7), (8, 12), (5, 11), (12, 15)]
    print(render_a_calender_concurrent_count_op(events))
