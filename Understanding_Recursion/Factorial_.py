## Thinking
## permutation is the sequence multiplication
## 5*4*3*2*1
## That means every lower integer call the factorial of the lower number and mutiplies itself by it
## 5 * 4! = 4*3! ...


def factorial(number: int):
    ## base case
    if number == 0:
        return 1

    ## Recursive Case
    return number * factorial(number - 1)


print(factorial(5))


# Time complexity O(n) because we go down a linear line
# Space complexity O(n)  because recusion stacks call variable again and again

# factorial(5)
# │
# ├── 5 * factorial(4)
# │
# │   ├── 4 * factorial(3)
# │   │
# │   ├── 3 * factorial(2)
# │   │   │
# │   │   ├── 2 * factorial(1)
# │   │   │   │
# │   │   │   ├── 1 * factorial(0)
# │   │   │   │   │
# │   │   │   │   └── 1
