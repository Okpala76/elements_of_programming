## the Brute force is not even possible becase we cant tell from inception how deep the the lists will be or where they will appear as the ar the direct factors to determine the recursive call

##  Now the recursive call takes the approach of seprating the list varables and the single variables
## an then calling recursion on the list  valraibles with the pareant list


def recursive_sumation_nested_list(l: list):
    total = 0

    for value in l:
        if isinstance(value, list):
            total += recursive_sumation_nested_list(value)
        else:
            total += value
    return total


print(recursive_sumation_nested_list([1, [2, 3], [4, [5]]]))


##Why would loops become difficult for nested lists?
# because it is irregular and random , to it can not perform a straigt forward operation that runs iterativey
##What is the recursive case here?
#the recursive case is the case where there is a lit with the array or list 
##What is the base case?
#The base case is the for loop that has a definete end WRONG!!!!!
# The base case is simply put the point where we dnt need recursion anymore, a point where recursion is no longer need 
# hence that will be defined as the the else block where there is no recursion
