class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.link = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    @property
    def length(self):
        return self._length

    def get(self, index):
        if index < 0:
            index = self._length + index
        node = self.traverse(index)
        return node.value

    def insert(self, value, index=None):
        node = LinkedListNode(value)

        if self.head is None:
            self.head = node
            self.tail = node
        elif index is not None and index < self._length:
            if index == 0:
                node.link = self.head
                self.head = node
            else:
                old_node = self.traverse(index - 1)
                node.link = old_node.link
                old_node.link = node
        else:
            self.tail.link = node
            self.tail = node

        self._length += 1

    def remove(self, index):
        self._length -= 1

        if index == 0:
            value = self.head.value
            self.head = self.head.link
            return value
        
        before_node = self.traverse(index - 1)
        node_to_remove = before_node.link
        next_node = node_to_remove.link

        value = node_to_remove.value
        before_node.link = next_node

        if next_node is None:
            self.tail = before_node

        return value


    def traverse(self, index):
        if index >= self._length:
            raise IndexError("index out of range")
        node = self.head
        i = 0
        while i < index:
            node = node.link
            i += 1
        return node
