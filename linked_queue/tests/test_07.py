import pytest


def test_linked_queue_exists():
    from linked_queue import LinkedQueue


def test_linked_queue_has_dequeue_method():
    from linked_queue import LinkedQueue
    queue = LinkedQueue()
    assert hasattr(queue, "dequeue")
    assert callable(queue.dequeue)


def test_empty_linked_queue_raises_exception():
    from linked_queue import LinkedQueue
    queue = LinkedQueue()
    with pytest.raises(Exception):
        queue.dequeue()


def test_linked_queue_has_enqueue_method():
    from linked_queue import LinkedQueue
    queue = LinkedQueue()
    assert hasattr(queue, "enqueue")
    assert callable(queue.enqueue)


def test_new_linked_queue_has_head_property_set_to_none():
    from linked_queue import LinkedQueue
    queue = LinkedQueue()
    assert hasattr(queue, "head")
    assert queue.head == None


def test_new_linked_queue_has_tail_property_set_to_none():
    from linked_queue import LinkedQueue
    queue = LinkedQueue()
    assert hasattr(queue, "tail")
    assert queue.tail == None


def test_linked_queue_node_exists():
    from linked_queue import LinkedQueueNode
