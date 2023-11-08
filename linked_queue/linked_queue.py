# Write your code here to make the tests pass.
#
# Change your working directory to this directory,
# linked_queue.
#
# # Start by running python -m pytest tests/test_01.py and
# making the test pass.
#
# Then, run python -m pytest tests/test_02.py to make the
# next test pass. Keep going to tests/test_15.py.

class LinkedQueueNode:
    def __init__(self, value):
        self.value = value
        self.link = None

class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # removes value at beginning of the queue
    def dequeue(self):
        if self.length == 0:
            raise Exception

        value = self.head.value

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            next = self.head.link
            self.head = next

        self.length -= 1
        return value
        # record the head.link (next Node)
        # set head to next Node

    # adds a value to the end of the queue
    def enqueue(self, value):
        newNode = LinkedQueueNode(value)

        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.link = newNode
            self.tail = newNode

        self.length += 1


# queue = LinkedQueue()
# queue.enqueue(50)
# value = queue.dequeue()
# print(value)