# 11.2 Compute the k closest stars
# Consider a coordinate system for the Milky Way, in which the Earth is at (0, 0, 0).
# Model stars as points, and assume distances are in light years. The Milky Way
# consists of approximately 1012 stars, and their coordinates are stored in a file in
# comma-separated values (CSV) format—one line per star and four fields per line, the
# first corresponding to an ID, and then three floating point numbers corresponding
# to the star location.

# Problem 11.2: How would you compute the k stars which are closest to the Earth?
# You have only a few megabytes of RAM.


# Basically we are tasked with getting all the stars in the milky way
# and returning just the ones closest to the earth
#
# Since earth is (0,0,0) we won't be needing any comparsion in our distance function


def distance(co_ordinates: tuple[int, int, int]):
    x, y, z = co_ordinates

    return x**2 + y**2 + z**2

    # The ideal equation is sqrt(x^2+y^2+z^2)
    # but we try to aviod the sqrt
    # i suspect for all the shenanigans around -+ as well as approximations


# Brute Force
# for this idea we would calcuate all star distances then store them in a list
# then sort select the top k ones
#


def the_kth_closest_stars(file: list[tuple[int, list[int]]], k: int):

    star_distances = []
    ## O(n)
    for id, star in file:
        d = distance(star)
        star_distances.append((id, d))

    # O(n log n)
    star_distances.sort(key=lambda x: x[1])

    # O(k)
    return star_distances[:k]


# # Test example
# stars1 = [
#     ("a", [10, 0, 0]),  # distance = 10
#     ("b", [3, 4, 0]),  # distance = 5
#     ("c", [1, 0, 0]),  # distance = 1
#     ("d", [0, 2, 0]),  # distance = 2
#     ("e", [5, 5, 5]),  # distance ≈ 8.66
# ]

# if __name__ == "__main__":
#     print("Top 3 closest stars:")
#     result = the_kth_closest_stars(stars1, 3)
#     for star_id, dist in result:
#         print(f"  Star {star_id}: distance = {dist:.2f}")

#     print(f"\nAll stars sorted: {the_kth_closest_stars(stars1, 5)}")
#     print(f"Top 1 closest: {the_kth_closest_stars(stars1, 1)}")


# Complexity
# Time: O(n log n) because of the sorting and as it super seeds others
# Space: O(n) because of storing all stars


# Optimized approach
# Using heap
# from my accessment i see that this will be a max heap operation.


import heapq


def the_kth_closest_stars_op(file: list[tuple[str, list[int]]], k: int):

    max_heap = []

    # O (n log k)
    for id, star_cord in file:
        d = distance(star_cord)

        if len(max_heap) < k:
            heapq.heappush(max_heap, (id, -d))
        else:
            current_farthest_id, current_farthest_distance = max_heap[0]

            if -d > current_farthest_distance:
                heapq.heapreplace(max_heap, (id, -d))

    # O(k)
    max_heap = reversed(max_heap)

    # O(k)
    for id, stars in max_heap:
        print(id, -(stars))


# Test example
stars1 = [
    ("a", [10, 0, 0]),  # distance = 10
    ("b", [3, 4, 0]),  # distance = 5
    ("c", [1, 0, 0]),  # distance = 1
    ("d", [0, 2, 0]),  # distance = 2
    ("e", [5, 5, 5]),  # distance ≈ 8.66
]

if __name__ == "__main__":
    print("Top 3 closest stars:")
    the_kth_closest_stars_op(stars1, 3)


# Complexity
# Time : O(n log k)
#        because we visit ever star and use a k sized heap to evaluate
#        staying or discarding

# Space: O(k)
#  because we use a heap sized k at worst case
