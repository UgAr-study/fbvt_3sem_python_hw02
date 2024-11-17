import pytest
from typing import Any
from dll import DoublyLinkedList


@pytest.fixture
def empty_dll() -> DoublyLinkedList:
    return DoublyLinkedList()


@pytest.fixture
def common_dll() -> DoublyLinkedList:
    dll = DoublyLinkedList()
    dll.push(1)
    dll.push(2)
    dll.push(3)
    return dll


@pytest.fixture
def other_dll() -> DoublyLinkedList:
    dll = DoublyLinkedList()
    dll.push(4)
    dll.push(5)
    return dll

def test_len(empty_dll: DoublyLinkedList, common_dll: DoublyLinkedList, other_dll: DoublyLinkedList) -> None:
    assert len(empty_dll) == 0
    assert len(common_dll) == 3
    common_dll.pop()
    assert len(common_dll) == 2
    common_dll.insert(other_dll)
    assert len(common_dll) == 4

def test_push(empty_dll: DoublyLinkedList) -> None:
    empty_dll.push(10)
    assert empty_dll._head.data == 10
    assert empty_dll._tail.data == 10

    empty_dll.push(20)
    assert empty_dll._tail.data == 20
    assert empty_dll._head.next.data == 20
    assert empty_dll._tail.prev.data == 10


def test_pop(common_dll: DoublyLinkedList) -> None:
    assert common_dll.pop() == 1
    assert common_dll._head.data == 2
    assert common_dll._head.prev is None

    assert common_dll.pop() == 2
    assert common_dll._head.data == 3

    assert common_dll.pop() == 3
    assert common_dll._head is None
    assert common_dll._tail is None

    with pytest.raises(ValueError, match="List is empty"):
        common_dll.pop()


def test_at(common_dll: DoublyLinkedList) -> None:
    assert common_dll.at(0) == 1
    assert common_dll.at(1) == 2
    assert common_dll.at(2) == 3

    with pytest.raises(IndexError, match="Index must be non-negative"):
        common_dll.at(-1)

    with pytest.raises(IndexError, match="Index out of bounds"):
        common_dll.at(10)


def test_insertat_index(common_dll: DoublyLinkedList, other_dll: DoublyLinkedList) -> None:
    common_dll.insert(other_dll, 1)
    current = common_dll._head
    data_sequence = [1, 4, 5, 2, 3]
    for data in data_sequence:
        assert current.data == data
        current = current.next

    assert current is None

    # Insert at the head
    another_list = DoublyLinkedList()
    another_list.push(6)
    another_list.push(7)
    common_dll.insert(another_list, 0)
    current = common_dll._head
    data_sequence = [6, 7, 1, 4, 5, 2, 3]
    for data in data_sequence:
        assert current.data == data
        current = current.next

    # Insert at the tail
    final_list = DoublyLinkedList()
    final_list.push(8)
    common_dll.insert(final_list)
    assert common_dll._tail.data == 8
