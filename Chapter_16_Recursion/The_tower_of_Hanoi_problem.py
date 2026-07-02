## The Tower of Hanoi problem is one that is very mazzy, omo i can tell you for a fact that after this this one still need revisting
# i will like to solve mutiple problem on this to get better


# Now let us go ahead ahead

# Here we are tasked to take a group of rings ordered by diatmeter size and move the rings around
# Our constriant is that we can't move the ring of a greater diameter on to one of a lesser diameter
# and we have an extra tower to move the ring into temporarly

# so we impore the Tower of Hanoi method


# Brute Force is a continous movement on the rings after testing legality of the move(if it is within the constraint)
# That will take forever
#
#   def brute_force(pegs, target_state):
# if pegs == target_state:
#     return True

# for each possible move:
#     if move is legal:
#         make move
#         brute_force(...)
#         undo move

# but the hanoi method has a formula that works using three spaces
# and that is
#
# We move then n-1 rings away from the top my moving them inter changeably to the other two guys
# Where we start is dependent on the height of the source tower
# n = 3 == t
# n = 4 == h and continues interchangeably like that
#
# Then we move the biggest ring to the target
#
# Then we move the remain ring back unto opt the target ring
#
# This is the whole concept
#


def tower_of_hanoi(n: int):
    move = []

    def transfer(n: int, source: str, target: str, helper: str):
        # base case
        if n == 0:
            return

        # take away the top n-1 rings from the source and target
        transfer(
            n - 1, source, helper, target
        )  # saying move n-1 about of rings from source to the helper

        # Move the last ring to it target
        move.append(
            (source, target)
        )  # now that source remains with only the largest , move that to the target which is also empty

        # Take the remain pile and put over target
        transfer(
            n - 1, helper, target, source
        )  # Now move all that pile in helper on to target

    transfer(n, "P1", "P2", "P3")

    return move


print(tower_of_hanoi(4))

# Complexity
# Time: O(n) * O(n) because of the first transfer and the second transfer and these are like bt trees
# Time = O(2^n)
# Space = O(n) the recursion and it variable stack level creations
