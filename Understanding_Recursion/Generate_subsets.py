## The thinking behind this is very interesting
## Why?
## it uses a binary approach to recursively add and evade adding values in the loop tree
#  becoz when you think of recursion you think of a tree
#  so with every recursion you create a branch
#  even if that branch is linear to the formal node still treat it as a branch that is the visualization we need to see problems get solved


# Now this solution looks at iteratively calling the function and carrying all the index value we want to go to next... along
# this helps us immediately use the value at that index in the recursion depth we find ourselves


def generate_subset(value: list):
    result = []

    def back_tracking(index: int, current_list: list):
        ## Base case 
        # length of the value is equal to the value of the index  
        if len(value) == index:
            result.append(current_list.copy())
            return

        ## left side that ignores the current index value
        back_tracking(index + 1, current_list)

        ## right side that adds the value at the index
        current_list.append(value[index])
        back_tracking(index + 1, current_list)

        current_list.pop()

    back_tracking(0, [])

    return result


print(generate_subset([1, 2, 3]))
