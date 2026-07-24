# 20.3_The_readers-writers_problem

# Problem 20.3: Implement a synchronization mechanism for the first readers-writers
# problem.

# This question tries to solve the problem of reading an object where we can have as meant reader but be cant read when we are writting, we cant also write when we are writting or reading


import threading
from typing import List, TypeVar, Callable

T = TypeVar("T")


class Readers_Writers:
    def __init__(self) -> None:
        self.readers: int = 0
        self.writer_active: bool = False
        self.condition = threading.Condition()

    def reader(self, reader_fn: Callable[[], T]) -> T:
        # we lock in the moment
        with self.condition:
            # we check if the writer is writting at this moments
            while self.writer_active:
                self.condition.wait()
            # Now that we are done waiting for rwriters to finish we increase readers count within the lock to stop coming writers from entering again
            self.readers += 1

        # break out of the lock so that other reader can work as well
        try:
            return reader_fn()
        finally:
            # lock the moment again so that we can remove our self from the active readers in case another guy is also thring to do that
            with self.condition:
                self.readers -= 1

                # check if u are the last guy so that u can wake sleeping writers
                if self.readers == 0:
                    self.condition.notify_all()

    def writer(self, writer_fn: Callable[[], T]) -> T:
        # we lock the moments so that no one interfaces with s or any other variable at this moment
        with self.condition:
            # we then check the siyuation for whick we must go to sleep
            while self.writer_active or self.readers > 0:
                self.condition.wait()
            # wehn we wake up we then set our self as active so if someone comes they can know that we are active and if we need to stop them we stop them
            self.writer_active = True

        # we come out of the lock and then we run our fun
        try:
            return writer_fn()
        finally:
            with self.condition:
                self.writer_active = False
                # so that every sleeper can wake, we don do an if because writers are independ and an no simultaneous
                self.condition.notify_all()


# Personal lesson: a lock should protect shared state transitions, not necessarily remain held throughout the entire operation. Releasing the condition lock after registering a reader is what allows multiple readers to run concurrently.

# Monitor / condition-variable synchronization with reader preference.

# Complexity
# Reader entry/exit: O(1)
# Writer entry/exit: O(1)
# Extra space: O(1) — only counters, flags, and the condition variable

# The actual read/write work depends on the supplied function:
# read total  = O(1) + reader_function time
# write total = O(1) + writer_function time
