# Linked Queue

A _queue_ is a data structure that provides two methods:

* `enqueue` adds a value to the end of the queue
* `dequeue` removes the value at the beginning of the queue
  and returns the value

A `LinkedQueue` is a data structure that uses
`LinkedQueueNode` instances to maintain the structure of the
data inside the queue.

You should write your code in _linked\_queue.py_.

You have two options about how to approach this problem.

## Test-driven development

To do the test-driven development method, change the working
directory to this directory, _./linked\_queue_. Then,
step-by-step, start with running this command.

```sh
python -m pytest tests/test_01.py
```

Once you make that test pass, run the next test file,
_tests/test\_02.py_. Make the new test pass. Then continue
on with the next test until you get to the last one, test
file number 15.

## All-at-once development

If you feel like just jumping right in, you can run this
command.

```sh
python -m pytest tests/test_15.py
```

That will run all of the tests for the linked queue. Just
make them all pass.
