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
        self.prev_node = prev_node
        self.next_node = next_node

    def add(self, element):
        self.arr.append(element)

class VList():
    def __init__(self):
        self.tail = VListNode(capacity=1, prev_node=None, next_node=None)
        self.cur = -1

    def add_to_list(self, element):
        if len(self.tail.arr) < self.tail.capacity:
            self.tail.add(element)
        else:
            new_tail = VListNode(capacity=self.tail.capacity * 2, prev_node=self.tail, next_node=None)
            new_tail.add(element)
            self.tail.next_node = new_tail
            self.tail = new_tail
        self.cur += 1

    def at_index(self, index):
        current_node = self.tail
        current_node_len = len(current_node.arr) - 1
        tmp_cur = self.cur
        while tmp_cur != index:
            tmp_cur -= 1
            if current_node_len == 0:
                current_node = current_node.prev_node
                current_node_len = len(current_node.arr) - 1
            else:
                current_node_len -= 1
        return current_node.arr[current_node_len]

my_list = VList()
my_list.add_to_list(0)
print("added 0", my_list.tail.arr)
my_list.add_to_list(1)
print("added 1", my_list.tail.arr)
my_list.add_to_list(2)
print("added 2", my_list.tail.arr)
print("previous node", my_list.tail.prev_node.arr)
print(my_list.at_index(0))
print(my_list.at_index(1))
