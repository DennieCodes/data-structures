# Linked List

A _list_ is a data structure that provides three methods:

* `insert` inserts a value into a list at a specified index,
  or appends it to the end of the list if no index is
  specified
* `get` returns the value in the list at the specified
  index, or raises an `IndexError` if the index is outside
  the bounds of the list
* `remove` removes a value at a specified index, then
  returns that value

A `LinkedList` is a data structure that uses
`LinkedListNode` instances to maintain the structure of the
data inside the list.

You should write your code in _linked\_list.py_.

You have two options about how to approach this problem.

## Test-driven development

To do the test-driven development method, change the working
directory to this directory, _./linked\_list_. Then,
step-by-step, start with running this command.

```sh
python -m pytest tests/test_01.py
```

Once you make that test pass, run the next test file,
_tests/test\_02.py_. Make the new test pass. Then continue
on with the next test until you get to the last one, test
file number 19.

## All-at-once development

If you feel like just jumping right in, you can run this
command.

```sh
python -m pytest tests/test_19.py
```

That will run all of the tests for the linked list. Just
make them all pass.
