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
