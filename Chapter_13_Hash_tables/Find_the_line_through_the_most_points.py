# Problem 13.3: Let P be a set of n points in the plane. Each point has integer
# coordinates. Design an efficient algorithm for computing a line that contains the
# maximum number of points in P.


# The problem simply askes us to fine the longest line in a plane of cordinates
# i.e cordinates can link up to make the longest line

# we make use of the slope equation to determine if a co ordinate or point falls on a line
# that had already existed


def on_same_line(p1: tuple[int], p2: tuple[int], p3: tuple[int]):
    return (p3[1] - p2[1]) * (p3[0] - p1[0]) == (p3[1] - p1[1]) * (p3[0] - p2[0])


def find_the_line_through_the_most_points(points: list[tuple]):
    if len(points) <= 2:
        return len(points), points

    best = 0
    current_best_cordinate = []

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            count = 2
            coordinates = [points[i], points[j]]

            for k in range(len(points)):
                if k != i and k != j:
                    if on_same_line(points[k], points[j], points[i]):
                        count += 1
                        coordinates.append(points[k])
            if best < count:
                current_best_cordinate = coordinates
                best = count

    return best, current_best_cordinate


# Complexity
# Time: O(n^3) because we go the point's list n^3 times
# Space: O(n) we hold a space that can grow as large as the points list in the wordt case( where all point align)


from collections import defaultdict
from math import gcd


def find_the_line_through_the_most_points_op(points: list[tuple]):
    if points is None:
        return

    if len(points) < 2:
        return IndexError("No enough points")

    best = 0

    for i in range(len(points)):
        slopes = defaultdict(int)
        ## this guy does sumtin very intresting as it allows you to just assign values
        # to even key you have not created, basically under the hood i create key and assigns them
        # to zero for any interation with a key yet to be created
        anchor_x, anchor_y = points[i]

        for j in range(i + 1, len(points)):

            x, y = points[j]

            dx = anchor_x - x
            dy = anchor_y - y

            if dx == 0:
                slope = (
                    0,
                    1,
                )
                # because we just caught on person that aligns on the vertical hemisphere
            elif dy == 0:
                slope = (
                    1,
                    0,
                )
                # because we just caught on person that aligns on the horizontal hemisphere
            else:
                g = gcd(dx, dy)

                dx //= g
                dy //= g

                slope = (dx, dy)

            slopes[slope] += 1  ## this is were that defaultdict(int) comes to live
            # allowing us to declare and immediatly write to a key that was just created by action of writting
            best = max(best, slopes[slope] + 1)
            # cagy one i must say, so lets take it slow
            # Question:
            # why are we checking best here
            # why do we add + 1  to the slope when we compare
            # answers
            # 1) we check best here so we dont do another recursion or iteration find the best
            # 2) we add plus one here because we dont account for the first anchor in our code
            # we just use it as a checker and update +1 t the slope that aligns with it
            # so the + 1 compliments that first anchor and counts it.

    return best


# PS: the lowest common divisor is the source of truth
# it is not about the anchor
# Question: why doent i return to the guys behing me to see how they slope agains me as j why do i only move forward to compare
# Answer: This is because just as said earlier this is not about the anchor, the anchor is just there to record the slope
# so if we from the anchor have recorded the slope forward we no longer need to record it again when we move forward,
# rather we record the slope of the ones in front of in front of us.

## Complexity
# Time: O(n^2)
# Space: O(1)


if __name__ == "__main__":
    points = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2)]
    print(find_the_line_through_the_most_points_op(points))
