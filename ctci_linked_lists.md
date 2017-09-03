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
