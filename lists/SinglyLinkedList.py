from list import List

import sys
sys.path.append("../")
from exceptions import *
# from . import exceptions

# class EmptyListException(Exception):
#     pass

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
            raise EmptyListException("List cannot be empty.")


    # Returns the last element of the list.
    # Throws EmptyListException.
    def get_last(self):
        if self.tail != None:
            return self.tail
        else:
            raise EmptyListException("List cannot be empty.")
            

    # Returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    def get(self, position): pass

    # Returns the position in the list of the
    # first occurrence of the specified element,
    # or -1 if the specified element does not
    # occur in the list.
    def find(self, element): pass

    # Inserts the specified element at the first position in the list.
    def insert_first(self, element):

        self.num_elements += 1

    # Inserts the specified element at the last position in the list.
    def insert_last(self, element):

        self.num_elements += 1

    # Inserts the specified element at the specified position in the list.
    # Range of valid positions: 0, ..., size().
    # If the specified position is 0, insert corresponds to insertFirst.
    # If the specified position is size(), insert corresponds to insertLast.
    # Throws InvalidPositionException.
    def insert(self, element, position):

        self.num_elements += 1

    # Removes and returns the element at the first position in the list.
    # Throws EmptyListException.
   
    def remove_first(self):

        self.num_elements -= 1

    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.
   
    def remove_last(self):

        self.num_elements -= 1
    
    # Removes and returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    # Throws InvalidPositionException.
   
    def remove(self, position):
    
        self.num_elements -= 1

    # Removes all elements from the list.
   
    def make_empty(self):

        self.num_elements -= 1

    # Returns an iterator of the elements in the list (in proper sequence).
   
    def iterator(self): pass

a = SinglyLinkedList()
# print(a.is_empty())
b = a.get_first()