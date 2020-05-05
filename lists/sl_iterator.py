from exceptions import *

class Iterator():
    def __init__(self, head):
        self.head = head
        self.current = self.head

    # Returns true iff the iteration has more elements.
    # In other words, returns true next would return an element rather than throwing an exception.
    def has_next(self):
        if self.current == None:
            return False
        else:
            return True

    # Returns the next element in the iteration.
    # Throws NoSuchElementException
    def next(self):
        if self.has_next():
            elem = self.current.get_element()
            self.current = self.current.get_next()
            return elem
        else:
            raise NoSuchElementException

    # Restarts the iteration. After rewind, if the iteration is not empty, next will return the first element in the iteration.
    def rewind(self):
        self.current = self.head