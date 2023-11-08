# Write your code here to make the tests pass.
#
# Change your working directory to this directory,
# linked_list.
#
# Start by running python -m pytest tests/test_01.py and
# making the test pass.
#
# Then, run python -m pytest tests/test_02.py to make the
# next test pass. Keep going to tests/test_19.py.

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.link = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert(self, value, index=None):
        if index != None:
            if index > self.length-1 and index > 0:
                raise IndexError

        newNode = LinkedListNode(value)

        if not self.head:
            self.head = newNode
            self.tail = newNode
        elif index == 0:
            newNode.link = self.head
            self.head = newNode
        elif index == None:
            self.tail.link = newNode
            self.tail = newNode
        else:
            pointer = self.traverseToIndex(index-1)
            newNode.link = pointer.link
            pointer.link = newNode
        self.length += 1
        return value

    def get(self, index):
        # Check if index is within scope of DLL
        if index > self.length-1:
            raise IndexError

        if index < 0:
            # Traverse from end of list according to index
            pointer = self.traverseToIndex(self.length - abs(index))
            return pointer.value

        pointer = self.traverseToIndex(index)
        return pointer.value

    def remove(self, index):
        # if removing head node
        if index == 0:
            value = self.head.value
            self.head = self.head.link
            self.length -= 1
            return value

        previous = self.traverseToIndex(index -1)
        target = previous.link
        after = target.link

        value = target.value
        previous.link = after

        if after is None:
            self.tail = previous

        self.length -= 1
        return value

    def traverseToIndex(self, index):
        counter = 0
        pointer = self.head

        while(pointer.link != None):
            if counter == index:
                return pointer
            pointer = pointer.link

            if pointer.link == None:
                return pointer
            counter += 1

# dll = LinkedList()
# dll.insert(100)
# dll.insert(99)
# dll.insert(98)
# dll.insert(97)
# dll.insert(96)

# print(dll.get(-2))