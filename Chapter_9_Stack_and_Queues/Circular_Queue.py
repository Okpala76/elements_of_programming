# Problem 9.3: Implement a queue API using an array for storing elements. Your API
# should include a constructor function, which takes as argument the capacity of the
# queue, enqueue and dequeue functions, a size function, which returns the number
# of elements stored, and implement dynamic resizing.

## This problem looks to cook a sweet and intesting story
# which is a queue that is circular
# one might ask what does that mean and even look like?
# it means that the queue will have a specific size and the queue will not need adjustments when variables are move on
# in the brute force we will see where linear is used and where the waste occurs
# then what does it look like?
# it looks like a simple array treated as a cyclic one by using pointer and a very intutive opiawuni


## Brute force


class Linear_Queue:
    def __init__(self):
        self.arr = []

    def enqueue(self, data):
        return self.arr.append(data)

    def dequeue(self):
        if not self.arr:
            raise IndexError("Broo there is nothing in this list sir")
        ## This will do a shift of all other elements to the left after a pop
        # say [A,B,C,D]
        # deque(), pop(0)
        # A is out
        # now BCD needs to be pushed left one place so B 1--> 0 , C 2 ---> 1, D 3 ---> 1
        # hence O(n)
        return self.arr.pop(0)

    def resize(self):
        print("This is O(1) because we just append to the end the incoming")

    def size(self):
        return len(self.arr)

        ## This is O(1)
        # Python stores the length internally.
        # does not count elements one-by-one.
        # It instantly returns the stored size.


l_que = Linear_Queue()

l_que.enqueue(4)
l_que.enqueue(5)
l_que.enqueue(1)
l_que.dequeue()

# print(l_que.size())

# This  has complexity
# enqueue = O(1)
# dequeue = O(n)


class Circular_Queue:
    def __init__(self, capacity: int):
        self.count = 0
        self.arr = [0] * capacity
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        if self.count == len(self.arr):
            self.resize()

        if self.count == 0:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % len(self.arr)

        self.arr[self.rear] = data
        self.count += 1

        return self.arr[self.rear]

    def dequeue(self):
        if self.count == 0:
            raise IndexError("There's is no value here sir")

        temp = self.arr[self.front]
        # Last element being removed
        if self.count == 1:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % len(self.arr)

        self.count -= 1
        return temp

    def resize(self):

        old_capacity = len(self.arr)
        new_capacity = old_capacity * 2

        temp = [None] * new_capacity

        # Copy elements in queue order
        for i in range(self.count):
            temp[i] = self.arr[(self.front + i) % old_capacity]

        self.arr = temp
        self.front = 0
        self.rear = self.count - 1

    def size(self):
        return self.count

    def __repr__(self):

        if self.count == 0:
            return "[]"

        result = []

        for i in range(self.count):
            result.append(self.arr[(self.front + i) % len(self.arr)])

        return str(result)


cq_que = Circular_Queue(6)

cq_que.enqueue(4)
cq_que.enqueue(5)
cq_que.enqueue(1)
cq_que.dequeue()

print(cq_que.size())

# This  has complexity
# enqueue = O(1)
# dequeue = O(1)
