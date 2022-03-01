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
