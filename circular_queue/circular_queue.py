# Write your code here to make the tests pass.
#
# Change your working directory to this directory,
# circular_queue.
#
# # Start by running python -m pytest tests/test_01.py and
# making the test pass.
#
# Then, run python -m pytest tests/test_02.py to make the
# next test pass. Keep going to tests/test_XX.py.

class CircularQueue:
    def __init__(self, size):
       self.buffer = [None] * size
       self.size = size
       self.length = 0
       self.head = 0
       self.tail = 0

    def enqueue(self, value):
        if self.length == self.size:
            return None
        offset = self.length
        self.buffer[offset] = value
        self.length += 1
        if self.length == self.size:
            self.tail = 0
        else:
            self.tail = self.length

    def dequeue(self):
        # head of queue is self.length
        value = self.buffer[self.head]
        # get the value there
        self.buffer[self.head] = None
        # remove that entry
        self.length -= 1
        self.head += 1
        if self.head == self.size:
            self.head = 0
        # decrease length
        return value



# queue = CircularQueue(3)
# queue.enqueue(1)
# queue.enqueue(1)
# queue.enqueue(1)
# # queue.enqueue(17)
# # value = queue.dequeue()
# # value = queue.dequeue()
# # print(value)

# print("Head: ", queue.head)
# print("Tail: ", queue.tail)