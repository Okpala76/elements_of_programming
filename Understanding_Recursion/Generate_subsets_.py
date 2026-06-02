# Generate subsets
# we are trying to return the subsets of of a set
# i.e set [1,2]
# output [[],[1],[2],[1,2]]

# this method is called Binary decision tree

def generate_subset(values: list):
    # Final answer storage
    result = []

    def back_tracking(index: int, current_list: list):

        # -------------------------------------------------
        #
        # Watch:
        # - index
        # - current_list
        #
        # This lets you SEE every recursive call created.
        # -------------------------------------------------

        print(f"ENTER -> index={index}, current_list={current_list}")

        # =================================================
        # BASE CASE
        # =================================================
        #
        # If index reaches the length of the array,
        # it means:
        #
        # "We have made a decision for every element."
        #
        # So current_list is now a COMPLETE subset.
        #
        # IMPORTANT:
        # We copy because current_list is mutable.
        #
        if index == len(values):

            # -------------------------------------------------
            # BREAKPOINT 2
            #
            # Stop here to see:
            # - EXACTLY when a subset is completed
            # - what subset gets appended
            # -------------------------------------------------

            print(f"APPEND SUBSET -> {current_list}")

            result.append(current_list.copy())
            return

        # =================================================
        # LEFT BRANCH
        # =================================================
        #
        # Decision:
        # "DO NOT include this value"
        #
        # We simply move to the next index.
        #
        # Example:
        # index = 0
        # value = 1
        #
        # This branch says:
        # "Pretend 1 does not exist."
        #
        print(f"IGNORE -> {values[index]}")

        back_tracking(index + 1, current_list)

        # =================================================
        # RIGHT BRANCH
        # =================================================
        #
        # Decision:
        # "INCLUDE this value"
        #
        print(f"TAKE -> {values[index]}")

        current_list.append(values[index])

        # -------------------------------------------------
        # BREAKPOINT 3
        #
        # Stop here AFTER append.
        #
        # This is one of the MOST IMPORTANT moments.
        #
        # You will see:
        # current_list changing as recursion goes deeper.
        # -------------------------------------------------

        print(f"AFTER APPEND -> {current_list}")

        back_tracking(index + 1, current_list)

        # =================================================
        # BACKTRACK STEP
        # =================================================
        #
        # VERY IMPORTANT.
        #
        # We remove the value we added earlier
        # so that other branches can reuse the list.
        #
        # Without pop():
        # values from previous branches leak into others.
        #
        popped = current_list.pop()

        # -------------------------------------------------
        # BREAKPOINT 4
        #
        # Stop here to understand BACKTRACKING.
        #
        # This is the "undo" step.
        # -------------------------------------------------

        print(f"POP -> removed {popped}, current_list={current_list}")

        print(f"EXIT -> index={index}, current_list={current_list}")

    back_tracking(0, [])

    return result


print(generate_subset([1, 2]))

    #                         []
    #                 /                 \
    #          ignore 1               take 1
    #            []                    [1]
    #         /      \              /       \
    #   ignore2     take2      ignore2      take2
    #     []         [2]         [1]        [1,2]
    #    /  \        /  \        /  \        /   \
    #   ... ...    ... ...    ... ...     ...  ...
