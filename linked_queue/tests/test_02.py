def test_linked_queue_exists():
    from linked_queue import LinkedQueue


def test_linked_queue_has_dequeue_method():
    from linked_queue import LinkedQueue
    queue = LinkedQueue()
    assert hasattr(queue, "dequeue")
    assert callable(queue.dequeue)
