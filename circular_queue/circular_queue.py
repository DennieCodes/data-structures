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
        self.size = size
        self.head = 0
        self.tail = 0
        self.buffer = [None] * size
        self.length = 0

    def enqueue(self, value):
        self.length += 1
        self.buffer[self.tail] = value
        self.tail += 1
        if self.tail >= self.size:
            self.tail = 0

    def dequeue(self):
        self.length -= 1;
        value = self.buffer[self.head]
        self.head += 1
        if self.head >= self.size:
            self.head = 0
        return value
