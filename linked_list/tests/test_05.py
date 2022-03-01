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
