

class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage"""

    #------------------------ nested _Node class -------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element','_next'              # streamline memory usage

        def __init__(self, element, next):          # init nodes fields
            self._next = next                       # reference to user's element
            self._element = element

    def __init__(self):
        """ Create an empty stack."""
        self._head = None
        self._size = 0

    def __len__(self):
        """ Return the number of elements in stack."""
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):

        if self.is_empty():
            print('Stack is empty')
        return self._head._element




if __name__ == '__main__':
    ls = LinkedStack()
    print(len(ls))