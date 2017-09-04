# Remove duplicates from a linked list
```python
def del_dups(linked_list):
    vals = set()
    node = linked_list.head
    while node.next != None and node != None:
        if node.next.val in vals:
            node.next = node.next.next
        vals.add(node.val)
        node = node.next
```

# Find the kth to last element in a singularly linked linked list
```python
def find_kth(node, k):
    if node.next == None:
        return 1
    else:
        val = 1 + find_kth(node.next, k)
        if val == k:
            print(node.data)
        return val
```

# Given a reference to a middle node in a singly linked list, remove the node
```python
def delete_mid(node):
    while node.next != None and node != None:
        node.data = node.next.data
        node = node.next
    node = None
```

# Partition a linked list around a value x such that all values less than x come before all values greater than or equal to x
```python
def partition(linked_list, x):
    current = linked_list.head
    while current.next != None:
        while current.next.val < x:
            tmp = current.next
            current.next = current.next.next
            tmp.next = linked_list.head
            linked_list.head = tmp
        current = current.next
```

# Given a linked list that stores digits of numbers in reverse order, write a function that adds the two numbers and returns the sum as a linked list
