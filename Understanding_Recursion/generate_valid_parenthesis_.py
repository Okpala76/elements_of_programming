# This problem seeks to return only vaild closed parenthesis for a given number input
# Hence it is looking to take n integer input and return n differnt amount of closed parenthesis
# so 2 will have 
# ()(), (())


def generate_valid_parenthesis(n: int):
    result = []

    def back_tracking(open_count: int, close_count: int, current_strings: list):

        ## base case
        # Obviously this will be our base case because when we have  
        # 2 times the input(n) in valid parentesis{i.e (()) or ()() for 2 as input } then we are to stop
        # and append to the holder variable (result)
        if len(current_strings) == n * 2:
            result.append("".join(current_strings))
            return

        ## recursive_case one
        if open_count < n:
            # this will be holding the open parenthesis 
            current_strings.append("(")

            back_tracking(open_count + 1, close_count, current_strings)

            current_strings.pop()

        ## [()()]

        ## recursive case two
        if close_count < open_count:
            current_strings.append(")")

            back_tracking(open_count, close_count + 1, current_strings)

            current_strings.pop()

    back_tracking(0, 0, [])

    return result


print(generate_valid_parenthesis(3))
