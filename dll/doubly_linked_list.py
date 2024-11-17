from typing import  Iterable, TypeVar, Generic, Optional, overload

"""
Uglovskii Artem: Variant 2, implementing a doubly linked list with queue's interface (insert at the end, pop from the front).
"""

T = TypeVar('T')

class Node(Generic[T]):
    """
    Class for storing data in the linked list.
    """
    def __init__(self, data: T):
        self.data = data
        self.prev: Optional[Node[T]] = None
        self.next: Optional[Node[T]] = None

    def __eq__(self, other: 'Node[T]') -> bool:
        return self.data == other.data

    def __ne__(self, other: 'Node[T]') -> bool:
        return self.data != other.data

    def link_prev(self, other: Optional['Node[T]']):
        """Add prev neighbour"""
        self.prev = other
        if other is not None:
            other.next = self
        return

    def link_next(self, other: Optional['Node[T]']):
        """Add next neighbour"""
        self.next = other
        if other is not None:
            other.prev = self
        return


class DoublyLinkedList(Generic[T]):
    def __init__(self, elems: Optional[Iterable[T]] = None):
        self._size = 0
        self._head: Optional[Node[T]] = None
        self._tail: Optional[Node[T]] = None

        if elems:
            for elem in elems:
                self.push(elem)

    def __len__(self) -> int:
        return self._size

    def push(self, data: T) -> None:
        """Store new data at the end of the list"""
        new_node = Node[T](data)
        self._size += 1
        if not self._head: # we have an empty list, so just store the node
            self._head = new_node
            self._tail = new_node
        else: # insert at tail and update tail
            self._tail.next = new_node
            new_node.prev = self._tail
            self._tail = new_node

    def pop(self) -> T:
        """Remove the node from the beginning of the list and return its data"""
        if not self._head:
            raise ValueError("List is empty")
        removed_data = self._head.data
        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next
            self._head.prev = None
        self._size -= 1
        return removed_data

    def _at(self, index: int) -> Optional[Node[T]]:
        """Return node at the given index"""
        if index < 0:
            raise IndexError("Index must be non-negative")
        current = self._head
        count = 0
        while current and count < index:
            current = current.next
            count += 1

        if count != index:
            raise IndexError("Index out of bounds")
        return current

    def at(self, index: int) -> Optional[T]:
        """Return data at the given index"""
        node = self._at(index)
        if node is None:
            return None
        return node.data

    def insert(self, other: 'DoublyLinkedList[T]', index: Optional[int] = None) -> None:
        """Insert another doubly linked list before the node at the given index."""
        if not isinstance(other, DoublyLinkedList): # we should check it to be able to make insertion in O(index)
            raise TypeError("Expected a DoublyLinkedList")

        if index is None: # insert at the end
            return self._insert_between(self._tail, None, other)

        right = self._at(index)
        left = self._at(index - 1) if index > 0 else None
        return self._insert_between(left, right, other)

    def _insert_between(self, left: Optional[Node[T]], right: Optional[Node[T]], other: 'DoublyLinkedList[T]') -> None:
        """Insert another doubly linked list between given nodes"""
        if left is None:
            self._head = other._head
        else:
            left.link_next(other._head)
        if right is None:
            self._tail = other._tail
        else:
            right.link_prev(other._tail)
        self._size += len(other)
        return
