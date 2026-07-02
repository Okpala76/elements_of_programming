# Problem 16.2: Implement a method that takes as input a set S of n distinct elements,
# and prints the power set of S. Print the subsets one per line, with elements separated
# by commas.
# Here we define a power set
# A power set is simply a set that holds all subsets of a set from empty to to the set itself
# Check out image "Power_set"... Just hit ctrl+p then type in "Power_set.png"
#
# So yes that is the task as well to get all subsets found in the power set of a set and print it out line by line


def power_set(the_set: list):

    def power_setter(start: int, current: list):
        # every current is a subset
        print(current)

        for i in range(start, len(the_set)):
            # update the curent list
            current.append(the_set[i])

            # move to the next index after i
            power_setter(i + 1, current)

            ## Backtrack and append value
            current.pop()

    power_setter(0, [])


if __name__ == "__main__":
    power_set(["A", "B", "C"])

# complexity
# Time : O(2^n) because we visit every node in the binary tree illustartion atleast once,
# where n is the number of values in the set
# Space: O(2^n) 
