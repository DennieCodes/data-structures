def test_linked_list_exists():
    from linked_list import LinkedList


def test_empty_linked_list_has_head_and_tail_set_to_none():
    from linked_list import LinkedList
    list = LinkedList()
    assert list.head is None
    assert list.tail is None
