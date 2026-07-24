# 20.2 Implement a Timer class
# Problem 20.2: Develop a Timer class that manages the execution of deferred tasks.
# The Timer constructor takes as its argument an object which includes a Run method
# and a name field, which is a string. Timer must support—(1.) starting a thread,
# identified by name, at a given time in the future; and (2.) canceling a thread, identified
# by name (the cancel request is to be ignored if the thread has already started). pg. 173


# so we want to create a task class that holds a taskes state and a parrelel that might affect it or change its state
# will work only on the pending state

from asyncio import tasks
import threading
from time import sleep
from typing import Literal

Status = Literal["pending", "cancelled", "running"]


class Task:
    def __init__(self, name: str):
        self.name = name
        self.status: Status = "pending"
        self.start_time = int

    def run(self):
        # execute the task
        print("wake up this is an alarm")


import heapq
import itertools
import threading
import time
from dataclasses import dataclass, field
from typing import Callable


@dataclass(order=True)
class ScheduledTask:
    # These first two fields determine heap order.
    run_at: float
    sequence_number: int

    # These fields are not used when comparing heap entries.
    name: str = field(compare=False)
    action: Callable[[], None] = field(compare=False)
    state: str = field(default="PENDING", compare=False)

    def run(self) -> None:
        self.action()


class Timer:
    def __init__(self) -> None:
        # Min-heap ordered by run_at.
        self._heap: list[ScheduledTask] = []

        # Allows cancellation by task name.
        self._tasks_by_name: dict[str, ScheduledTask] = {}

        # Gives tasks with equal times a stable, unique ordering.
        self._sequence = itertools.count()

        # The condition contains the lock protecting both structures.
        self._condition = threading.Condition()

        # Only one thread waits for scheduled tasks.
        self._dispatcher = threading.Thread(
            target=self._dispatch,
            daemon=True,
        )
        self._dispatcher.start()

    def schedule(
        self,
        name: str,
        action: Callable[[], None],
        run_at: float,
    ) -> None:
        """
        run_at is a Unix timestamp.

        Example:
            run_at = time.time() + 5
        """

        with self._condition:
            existing_task = self._tasks_by_name.get(name)

            if existing_task is not None:
                raise ValueError(f"A pending task named {name!r} already exists")

            task = ScheduledTask(
                run_at=run_at,
                sequence_number=next(self._sequence),
                name=name,
                action=action,
            )

            self._tasks_by_name[name] = task
            heapq.heappush(self._heap, task)

            # Wake the dispatcher because this task may be earlier
            # than the task it is currently waiting for.
            self._condition.notify()

    def cancel(self, name: str) -> bool:
        with self._condition:
            task = self._tasks_by_name.get(name)

            if task is None:
                # It does not exist, was cancelled, or already started.
                return False

            if task.state != "PENDING":
                # Cancellation is ignored after execution starts.
                return False

            task.state = "CANCELLED"
            del self._tasks_by_name[name]

            # Wake the dispatcher in case it was waiting for this task.
            self._condition.notify()

            return True

    def _dispatch(self) -> None:
        while True:
            with self._condition:
                while True:
                    # Python's heapq cannot efficiently delete an
                    # arbitrary entry. Remove cancelled entries when
                    # they reach the top.
                    while self._heap and self._heap[0].state != "PENDING":
                        heapq.heappop(self._heap)

                    if not self._heap:
                        # No work exists. Sleep until schedule()
                        # adds a task and calls notify().
                        self._condition.wait()
                        continue

                    next_task = self._heap[0]
                    seconds_remaining = next_task.run_at - time.time()

                    if seconds_remaining > 0:
                        # Sleep until the task is due, unless schedule()
                        # or cancel() wakes us earlier.
                        self._condition.wait(timeout=seconds_remaining)
                        continue

                    # The task is now due.
                    heapq.heappop(self._heap)

                    # Check that this exact task is still active.
                    active_task = self._tasks_by_name.get(next_task.name)

                    if active_task is not next_task or next_task.state != "PENDING":
                        continue

                    # This is the critical state change.
                    # Once RUNNING, cancellation must fail.
                    next_task.state = "RUNNING"
                    del self._tasks_by_name[next_task.name]

                    break

            # Start the worker outside the lock.
            # Otherwise, a long-running task would block schedule()
            # and cancel().
            worker = threading.Thread(
                target=self._run_task,
                args=(next_task,),
                daemon=True,
            )
            worker.start()

    def _run_task(self, task: ScheduledTask) -> None:
        try:
            task.run()
        finally:
            with self._condition:
                task.state = "FINISHED"


# Complexity
# Where n is pending taxes

# Schedule task into heap	O(log n) because heaps rearrange in log n time
# Find task by name	Average O(1) dict find is o(1)
# Cancel task	Average O(1) with lazy deletion remove from dict
# Remove next task	O(log n) from heap
# Stored task records	O(n)
# Waiting dispatcher threads	O(1)


# Priority queue / min-heap
# Hash table lookup
# Producer-consumer scheduling
# Condition-variable synchronization
# Lazy deletion


# In concurrency problems, optimization often comes from separating waiting for work from performing work.
#  One manager can wait efficiently for many tasks; individual worker threads are only needed when real work begins.
