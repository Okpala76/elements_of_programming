# Problem 19.4: Given an instance of the task scheduling problem, compute the least
# amount of time in which all the tasks can be performed, assuming an unlimited
# number of servers. Explicitly check that the system is feasible.

# This problem looks to
# 1) get a task that has type <time:int, prerequistes:[classType]>
# 2) in a list
# 3) and return the time taken for all tasks to be completed
# 4) and check if it has a bottle neck anywhere
# Bottleneck?: when the prerequiste is cyclic and hence jams the whole system
# A -> B
# B -> C
# C -> A

# a task with this prequisted will never run because all tasks are wait for each other

# Unlimited resources means that the servers are aboundant and any task can start as and when due


from __future__ import annotations


class Task:
    def __init__(self, duration: int, prereq: list[Task] | None = None):
        self.duration = duration
        self.remaining_time = duration
        self.prereq = prereq or []
        self.started = False
        self.completed = False

    def is_prereq_completed(self) -> bool:
        return all(task.completed for task in self.prereq)


def delay_schedule_brute_force(tasks: list[Task]) -> int:
    time = 0
    completed_tasks = 0
    task_number = len(tasks)

    while completed_tasks < task_number:

        # Start every task whose prerequisites are complete.
        for task in tasks:
            if not task.started and task.is_prereq_completed():
                task.started = True

        running_something = False

        # Run all started tasks for one unit of time.
        for task in tasks:
            if task.started and not task.completed:
                running_something = True
                task.remaining_time -= 1

                if task.remaining_time == 0:
                    task.completed = True
                    completed_tasks += 1

        # Tasks remain, but nothing can run: dependency cycle.
        if not running_something and completed_tasks < task_number:
            return -1

        time += 1

    return time


# Complexity
# where t = time of count, p = prerequisite number of task we need to iter over to check completion, n = number of tasks
# Time  O(t* (2n*e))
# === ((t*(n*e))) removed the constant
# === (t*(n^2)) if e == n worst

# Space = the tasks held in ram memory for execution
# O(n)


## OPTI


class Task_Opti:
    def __init__(self, duration: int, prereq: list[Task_Opti] | None = None):
        self.duration = duration
        self.prereq = prereq or []


def delay_schedule(tasks: list[Task_Opti]) -> int:
    state: dict[Task_Opti, int] = {}
    memo: dict[Task_Opti, int] = {}

    def completion_time(task: Task_Opti) -> int:
        task_state = state.get(task, 0)

        # We returned to a task still in the current DFS path.
        if task_state == 1:
            raise ValueError("Cyclic dependency detected")

        # Already completely calculated.
        if task_state == 2:
            return memo[task]

        state[task] = 1

        longest_prerequisite_time = 0

        for prerequisite in task.prereq:
            longest_prerequisite_time = max(
                longest_prerequisite_time,
                completion_time(prerequisite),
            )

        result = longest_prerequisite_time + task.duration

        memo[task] = result
        state[task] = 2

        return result

    minimum_total_time = 0

    try:
        for task in tasks:
            minimum_total_time = max(
                minimum_total_time,
                completion_time(task),
            )
    except ValueError:
        return -1

    return minimum_total_time


## Complexity
# Time if n = number of task and e = number of preqs
# Time O(n * e) memo streamlines it but this is O(n)
# Space O(3n) === the state dict == O(n) , memo dict O(n) , dfs stack = O(n)  === complexity rule = O(n)

# Pattern: longest path in a weighted directed acyclic graph, using DFS, memoization, and cycle detection.


# A = 3
# B = 2

# C = 4 + A
#   = 4 + 3
#   = 7

# D = 1 + max(A, B)
#   = 1 + max(3, 2)
#   = 4

# E = 2 + max(C, D)
#   = 2 + max(7, 4)
#   = 9

if __name__ == "__main__":
    A = Task_Opti(3)
    B = Task_Opti(2)
    C = Task_Opti(4, [A])
    D = Task_Opti(1, [A, B])
    E = Task_Opti(2, [C, D])

    print(delay_schedule([A, B, C, D, E]))
