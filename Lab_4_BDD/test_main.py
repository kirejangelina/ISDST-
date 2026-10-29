import pytest
from main import push, pop, peek, is_empty


def test_is_empty():
    queue = []
    assert is_empty(queue) is True
    push(queue, "hello")
    assert is_empty(queue) is False


def test_push():
    queue = []
    push(queue, "msg1")
    push(queue, "msg2")
    assert queue == ["msg1", "msg2"]


def test_pop_fifo_order():
    queue = ["first", "second", "third"]
    assert pop(queue) == "first"
    assert pop(queue) == "second"
    assert pop(queue) == "third"
    assert is_empty(queue) is True


def test_pop_empty():
    queue = []
    with pytest.raises(IndexError):
        pop(queue)


def test_peek():
    queue = ["msg1", "msg2"]
    assert peek(queue) == "msg1"
    # Проверяем, что peek не удаляет элемент
    assert queue == ["msg1", "msg2"]


def test_peek_empty():
    queue = []
    with pytest.raises(IndexError):
        peek(queue)
