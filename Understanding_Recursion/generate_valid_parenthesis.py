def generate_valid_parenthesis(n: int):
    result = []

    def back_tracking(open_count: int, close_count: int, current_strings: list):

        ## base case
        if len(current_strings) == n * 2:
            result.append("".join(current_strings))
            return

        ## recursive_case one
        if open_count < n:
            current_strings.append("(")

            back_tracking(open_count + 1, close_count, current_strings)

            current_strings.pop()

        ## recursive case two
        if close_count < open_count:
            current_strings.append(")")

            back_tracking(open_count, close_count + 1, current_strings)

            current_strings.pop()

    back_tracking(0, 0, [])

    return result


print(generate_valid_parenthesis(2))
