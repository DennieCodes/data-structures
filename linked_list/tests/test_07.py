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
