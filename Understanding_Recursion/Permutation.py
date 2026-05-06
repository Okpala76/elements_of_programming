## Thinking
## permutation is the sequence multiplication
## 5*4*3*2*1
## That mean every lower integer call the permuattion of the lower number and mutiplies itself by it
## 5 * 4!, 4*3! ...


def permutation(number: int):
    ## base case
    if number == 0:
        return 1

    return number * permutation(number - 1)


print(permutation(7))

print(4 + 5)
