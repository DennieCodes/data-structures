class LinkedQueueNode:
    def __init__(self, value):
        self.value = value
        self.link = None


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def dequeue(self):
        value = self.head.value
        self.head = self.head.link
        if self.head is None:
            self.tail = None
        return value

    def enqueue(self, value):
        node = LinkedQueueNode(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.link = node
            self.tail = node
