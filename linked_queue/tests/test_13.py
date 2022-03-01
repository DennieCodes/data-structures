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


def test_linked_queue_node_has_value_parameter_in_constructor():
    from linked_queue import LinkedQueueNode
    LinkedQueueNode(5)


def test_new_linked_queue_node_has_value_property():
    from linked_queue import LinkedQueueNode
    node = LinkedQueueNode(5)
    assert node.value == 5


def test_new_linked_queue_node_has_link_property_set_to_none():
    from linked_queue import LinkedQueueNode
    node = LinkedQueueNode(5)
    assert node.link == None


def test_first_enqueue_sets_head_and_tail_to_node_with_value():
    from linked_queue import LinkedQueue
    queue = LinkedQueue()
    queue.enqueue(5)
    assert queue.head == queue.tail
    assert queue.head.value == 5


def test_second_enqueue_maintains_head_tail_is_new_node():
    from linked_queue import LinkedQueue
    queue = LinkedQueue()
    queue.enqueue(5)
    queue.enqueue(10)
    assert queue.head != queue.tail
    assert queue.head.value == 5
    assert queue.tail.value == 10


def test_dequeue_of_single_item_list_returns_value_sets_head_tail_to_none():
    from linked_queue import LinkedQueue
    queue = LinkedQueue()
    queue.enqueue(50)
    value = queue.dequeue()
    assert value == 50
    assert queue.head is None
    assert queue.tail is None
