import pytest

def test_linked_list_exists():
    from linked_list import LinkedList


def test_empty_linked_list_has_head_and_tail_set_to_none():
    from linked_list import LinkedList
    list = LinkedList()
    assert list.head is None
    assert list.tail is None


def test_linked_list_has_insert_method_that_takes_a_value():
    from linked_list import LinkedList
    list = LinkedList()
    assert hasattr(list, "insert")
    assert callable(list.insert)
    list.insert(10)


def test_linked_list_has_insert_method_that_takes_an_optional_position():
    from linked_list import LinkedList
    list = LinkedList()
    list.insert(10, 0)


def test_linked_list_node_exists():
    from linked_list import LinkedListNode


def test_linked_list_node_takes_value_in_constructor_and_sets_value_property():
    from linked_list import LinkedListNode
    node = LinkedListNode(100)
    assert node.value == 100


def test_new_linked_list_node_has_link_property_set_to_none():
    from linked_list import LinkedListNode
    node = LinkedListNode(100)
    assert node.link is None


def test_insert_sets_head_and_tail_to_same_node_with_inserted_value_and_none_link():
    from linked_list import LinkedList
    list = LinkedList()
    list.insert(100)
    assert list.head is not None
    assert list.head == list.tail
    assert list.head.value == 100
    assert list.head.link is None


def test_inserting_nodes_without_index_places_nodes_at_end_of_list():
    from linked_list import LinkedList
    list = LinkedList()
    list.insert(-1)
    for i in range(10):
        list.insert(i)
        assert list.head.value == -1
        assert list.tail.value == i


def test_empty_linked_list_has_length_property_of_zero():
    from linked_list import LinkedList
    list = LinkedList()
    assert hasattr(list, "length")
    assert list.length == 0
    

def test_length_property_increases_with_each_insert():
    from linked_list import LinkedList
    list = LinkedList()
    for i in range(10):
        assert list.length == i
        list.insert(i)
        assert list.length == i + 1


def test_linked_list_has_get_method_to_get_value_at_index():
    from linked_list import LinkedList
    list = LinkedList()
    for i in range(10):
        list.insert(i - 1)
    for i in range(10):
        assert list.get(i) == i - 1


def test_get_method_raises_index_error_for_index_greater_than_or_equal_to_list_length():
    from linked_list import LinkedList
    list = LinkedList()
    for i in range(10):
        with pytest.raises(IndexError):
            list.get(i)
        list.insert(i - 1)


def test_insert_in_non_zero_specified_index_inserts_into_list():
    from linked_list import LinkedList
    list = LinkedList()
    for i in range(11):
        list.insert(i)
    old_head = list.head
    old_tail = list.tail
    list.insert(100, 2)
    assert old_head == list.head
    assert old_tail == list.tail
    for index, value in enumerate([0, 1, 100, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
        print(index, list.length)
        assert list.get(index) == value


def test_linked_list_has_remove_method_that_takes_one_argument():
    from linked_list import LinkedList
    list = LinkedList()
    list.insert(0)
    assert hasattr(list, "remove")
    assert callable(list.remove)
    list.remove(0)


def test_remove_method_for_index_0_removes_value_at_head_reduces_length_returns_value():
    from linked_list import LinkedList
    list = LinkedList()
    list.insert(100)
    assert hasattr(list, "remove")
    assert callable(list.remove)
    value = list.remove(0)
    assert value == 100
    assert list.length == 0
