# Thinking bit

# The Fibonacci sequence starts with 0 and 1.
# From there, every next number is created by adding the previous two numbers together.

# So, except for 0 and 1:

# fib(n) = fib(n - 1) + fib(n - 2)

# Example sequence:

# 0, 1, 1, 2, 3, 5, 8, 13, ...

# Because:

# 1 = 1 + 0
# 2 = 1 + 1
# 3 = 2 + 1
# 5 = 3 + 2


# brute force
def fibonacci(number: int):
    ## base case
    if number == 1:
        return 1
    if number == 0:
        return 0

    ## recursive case
    return fibonacci(number - 1) + fibonacci(number - 2)


print("Brute force return of Fib", fibonacci(10))
# fibonacci(100) ---- this never stopped running

### There is a repeation here every time that someone calls fibonacci -1 and -2 it must likely have been called before
## lets take 7 for instants
## fib (6)+ fib(5)
## fib(5)+ fib(4)  +  fib(4) + fib(3)
## so we see that we call fib(5) twice on the first level and second level and also fib(4 as well)


def optimized_fibonacci(num: int, memo={}):

    if num in memo:
        return memo[num]
        # base case
    if num == 0:
        return 0
    if num == 1:
        return 1

    ## recursive case
    result = optimized_fibonacci(num - 1) + optimized_fibonacci(num - 2)
    memo[num] = result
    return result


print("this is the optimized fib ", optimized_fibonacci(100))
# time was 0.089


## Understanding brute force call of Big(O) = O(2^n)

## The Big(O) of the none Optimized
## This will be 2^n as we have two from each function call
## and this will create 2^n amount of call nodes if u check it out
## instance
## 3 input
## left call will be 2,1,0,0,0
## right call will be 1,0,0
## that is eight function calls hence 2^3 = 8
## we see the justification for that big(O)


## For Optimized
## because we have to  only the left side of all nodes and store it value for all the right nodes to rely on
## then we have linearized this process and hence we are golden
## Big(O) = O(n)
