"""
I recently interviewed at Palantir and this was one of the questions I came across following the Hackerrank challenge.

Implement a VList class. The behavior of the class is detailed below.

A VList class is an object that contains linked arrays. Each array has a permissible capacity (beginning with 1). When
the number of elements in the array reach the capacity, a new link in the VList is added to the tail with doubled capacity.

[0] <-> [1, 2] <-> [3, 4, _, _] <--- tail

In the example above, when the first link is filled with 1 element, another link in the VList is added with capacity 2. After
the number of elements in this link reach capacity, another link is added with capacity 4.

Implement the add_to_list(element) method that adds element to the tail of the VList
Implement the at_index(index) method that returns the value store in the VList at index
"""

class VListNode():
    def __init__(self, capacity, prev_node, next_node):
        self.arr = []
        self.capacity = capacity
        self.prev = prev_node
        self.next = next_node
