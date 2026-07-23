# Problem 20.1: Write Java code in which the two threads, running concurrently, print
# the numbers from 1 to 100 in order.


# This marks the start of a concept I call muti threading that speaks of the concept of having mutiple works execute a task
# it doablity and if it is effecient if choosen


# This example here we solve an interleaving where we build a system that print out odd and even numbers nusing two workers


from importlib.machinery import OPTIMIZED_BYTECODE_SUFFIXES
import threading
import time


def two_interleaves_brute_force(n: int) -> None:
    turn = "odd"

    def print_odd() -> None:
        nonlocal turn

        for number in range(1, n + 1, 2):
            while turn != "odd":
                # Keep checking until it becomes this thread's turn.
                time.sleep(0)

            print(number)
            turn = "even"

    def print_even() -> None:
        nonlocal turn

        for number in range(2, n + 1, 2):
            while turn != "even":
                # Keep checking until it becomes this thread's turn.
                time.sleep(0)

            print(number)
            turn = "odd"

    odd_thread = threading.Thread(target=print_odd)
    even_thread = threading.Thread(target=print_even)

    odd_thread.start()
    even_thread.start()

    odd_thread.join()
    even_thread.join()


two_interleaves_brute_force(10)


# Complexity
# Time O(n)  entire en visit
# Space O(1) we hold nothing in ram memory, except constant variable names


# OPTIMIZED

import threading


def two_interleaves(n: int) -> None:
    if n < 1:
        return

    condition = threading.Condition()
    turn = "odd"

    def print_odd() -> None:
        nonlocal turn

        for number in range(1, n + 1, 2):
            with condition:
                while turn != "odd":
                    condition.wait()

                print(number)

                turn = "even"
                condition.notify()

    def print_even() -> None:
        nonlocal turn

        for number in range(2, n + 1, 2):
            with condition:
                while turn != "even":
                    condition.wait()

                print(number)

                turn = "odd"
                condition.notify()

    odd_thread = threading.Thread(target=print_odd)
    even_thread = threading.Thread(target=print_even)

    odd_thread.start()
    even_thread.start()

    odd_thread.join()
    even_thread.join()


# Complexity
# Time O(n) same space but we see the optimization in the repeated while loop that happens while we wait stop basically
#  Unlike busy waiting, sleeping threads do not continuously consume CPU while waiting.
# Space O(1)
