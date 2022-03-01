import pytest

def test_circular_queue_class_exists():
    from circular_queue import CircularQueue


def test_circular_queue_constructor_has_required_size_argument_and_sets_property():
    from circular_queue import CircularQueue
    with pytest.raises(TypeError):
        CircularQueue()
    queue = CircularQueue(10)
    assert queue.size == 10


def test_new_queue_has_head_and_tail_set_to_zero():
    from circular_queue import CircularQueue
    queue = CircularQueue(10)
    assert queue.head == 0
    assert queue.tail == 0


def test_new_queue_has_buffer_property_with_a_list_of_length_size():
    from circular_queue import CircularQueue
    queue = CircularQueue(10)
    assert queue.buffer is not None
    assert len(queue.buffer) == 10


def test_new_queue_has_zero_length():
    from circular_queue import CircularQueue
    queue = CircularQueue(10)
    assert queue.length == 0


def test_enqueue_increases_length_and_tail_by_one_and_stores_value_in_buffer():
    from circular_queue import CircularQueue
    queue = CircularQueue(10)
    queue.enqueue(8)
    assert queue.length == 1
    assert queue.tail == 1
    assert queue.buffer[0] == 8

    queue.enqueue(-3)
    assert queue.length == 2
    assert queue.tail == 2
    assert queue.buffer[0] == 8
    assert queue.buffer[1] == -3


def test_dequeue_reduces_length_by_one_increase_head_by_one_and_returns_value():
    from circular_queue import CircularQueue
    queue = CircularQueue(10)
    queue.enqueue(8)
    queue.enqueue(-3)
    queue.enqueue(3)
    queue.enqueue(17)

    value = queue.dequeue()
    assert value == 8
    assert queue.head == 1
    assert queue.length == 3

    value = queue.dequeue()
    assert value == -3
    assert queue.head == 2
    assert queue.length == 2

    value = queue.dequeue()
    assert value == 3
    assert queue.head == 3
    assert queue.length == 1

    value = queue.dequeue()
    assert value == 17
    assert queue.head == 4
    assert queue.length == 0


def test_enqueue_to_full_size_sets_tail_to_zero():
    from circular_queue import CircularQueue
    queue = CircularQueue(3)
    queue.enqueue(1)
    queue.enqueue(1)
    queue.enqueue(1)
    assert queue.head == 0
    assert queue.tail == 0


def test_dequeue_to_end_sets_head_to_zero():
    from circular_queue import CircularQueue
    queue = CircularQueue(3)
    queue.enqueue(1)
    queue.enqueue(1)
    queue.enqueue(1)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    assert queue.head == 0
    assert queue.tail == 0
