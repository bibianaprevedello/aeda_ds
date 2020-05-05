from nodes import SingleListNode
from list import List
from exceptions import *
from sl_iterator import Iterator

class SinglyLinkedList(List):
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    # Returns true iff the list contains no elements.
    def is_empty(self):
        return self.head == None

    # Returns the number of elements in the list.
    def size(self):
        return self.num_elements

    # Returns the first element of the list.
    # Throws EmptyListException.
    def get_first(self):
        if self.head != None:
            return self.head
        else:
            raise EmptyListException("List is empty.")

    # Returns the last element of the list.
    # Throws EmptyListException.
    def get_last(self):
        if self.tail != None:
            return self.tail
        else:
            raise EmptyListException("List is empty.")
            
    # Returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    def get(self, position):
        if (position >=0 and position < self.num_elements):
            current_node = self.head

            for i in range(position):
                if position == i:
                    return current_node.get_element()
                current_node = current_node.get_next()
        else:
            raise InvalidPositionException

    # Returns the position in the list of the
    # first occurrence of the specified element,
    # or -1 if the specified element does not
    # occur in the list.
    def find(self, element):
        current_node = self.head

        for i in range(self.num_elements):
            if element == current_node.get_element():
                return i
            current_node = current_node.get_next()
        return -1

    # Inserts the specified element at the first position in the list.
    def insert_first(self, element):
        new = SingleListNode(element, self.head)
        self.head = new

        if self.num_elements == 0:
            self.tail = new
        
        self.num_elements += 1

    # Inserts the specified element at the last position in the list.
    def insert_last(self, element):
        new =  SingleListNode(element, None)

        if self.num_elements == 0:
            self.head = new
            self.tail = new
        else:
            self.tail.set_next(new)
            self.tail = new

        self.num_elements += 1

    # Inserts the specified element at the specified position in the list.
    # Range of valid positions: 0, ..., size().
    # If the specified position is 0, insert corresponds to insertFirst.
    # If the specified position is size(), insert corresponds to insertLast.
    # Throws InvalidPositionException.
    def insert(self, element, position):
        if position > self.num_elements or position < 0:
            raise InvalidPositionException
        elif position == 0:
            self.insert_first(element)
        elif position == self.num_elements:
            self.insert_last(element)
        else:
            current = self.head

            for i in range(position):
                if i == position-1:
                    new = SingleListNode(element, current.get_next())
                    current.set_next(new)
                current = current.get_next()

            self.num_elements += 1

    # Removes and returns the element at the first position in the list.
    # Throws EmptyListException.
    def remove_first(self):
        if self.num_elements > 1:
            self.head = self.head.get_next()
            self.num_elements -= 1
        elif self.num_elements == 1:
            self.head = None
            self.tail = None
            self.num_elements -= 1
        else:
            raise EmptyListException

        return self.head

    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.
    def remove_last(self):
        if self.head == None:
            raise EmptyListException
        else:
            current_node = self.head
            for _ in range(self.num_elements-2):
                current_node = current_node.get_next()

            current_node.set_next(None)
            self.tail = current_node

        self.num_elements -= 1

        return self.tail
    
    # Removes and returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    # Throws InvalidPositionException.
    def remove(self, position):
        if position > self.num_elements or position < 0:
            raise InvalidPositionException
        elif position == 0:
            self.remove_first()
        elif position == self.num_elements:
            self.remove_last()
        else:
            current = self.head

            for i in range(position):
                if i == position-1:
                    current.set_next(current.get_next().get_next())
                current = current.get_next()

            self.num_elements -= 1

    # Removes all elements from the list.
    def make_empty(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    # Returns an iterator of the elements in the list (in proper sequence).
    def iterator(self):
        return Iterator(self.head)

    # Print the list
    def print_all(self):
        it = self.iterator()
        while True:
            try:
                print(it.next())
            except NoSuchElementException:
                break