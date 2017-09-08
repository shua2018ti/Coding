# Use a single array to implement three stacks
```python
class TripleStax(object):
    """docstring for TripleStax."""
    def __init__(self, size):
        super(TripleStax, self).__init__()
        self.array = [0] * size
        self.p1_top = 0
        self.p2_top = len(self.array) // 3
        self.p3_top = 2 * p2_top

    def push(self, stack, element):
        if stack == 1:
            if self.p1_top < len(self.array) // 3:
                self.array[self.p1_top] = element
                self.p1_top += 1
                return True
            else:
                print("Stack 1 is full.")
                return False
        elif stack == 2:
            if self.p2_top < 2 * (len(self.array) // 3):
                self.array[self.p2_top] = element
                self.p2_top += 1
                return True
            else:
                print("Stack 2 is full.")
                return False
        else:
            if self.p3_top < len(self.array) - 1:
                self.array[self.p3_top] = element
                self.p3_top += 1
                return True
            else:
                print("Stack 3 is full.")
                return False

    def pop(self, stack):
        if stack == 1:
            if self.p1_top >= 0:
                self.p1_top -= 1
                return self.array[self.p1_top + 1]
            else:
                print("Stack 1 is empty.")
                return False
        elif stack == 2:
            if self.p2_top >= len(self.array) // 3:
                self.p2_top -= 1
                return self.array[self.p2_top + 1]
            else:
                print("Stack 2 is empty.")
                return False
        else:
            if self.p3_top >= 2 * (len(self.array) // 3):
                self.p3_top -= 1
                return self.array[self.p3_top + 1]
            else:
                print("Stack 3 is empty.")
                return False
```

# Design a stack that that has push, pop, and min (returns the minimum element in the stack) operations that run in O(1) time
```python
class StackNode(object):
    """docstring for StackNode."""
    def __init__(self, val):
        super(StackNode, self).__init__()
        self.val = val
        self.previous = None
        self.previous_min = 0

class Stack(object):
    """docstring for Stack."""
    def __init__(self, top):
        super(Stack, self).__init__()
        self.top = top

    def push(self, node):
        if self.top == None:
            self.top = node
            node.previous_min = node.val
        else:
            node.previous = self.top
            node.previous_min = min(self.top.previous_min, node.val)
            self.top = node

    def pop(self):
        if self.top == None:
            return None
        top = self.top
        self.top = self.top.previous
        return top

    def min(self):
        if self.top == None:
            return None
        return self.top.previous_min
```

# Implement a `SetOfStacks` class that creates a new stack when the current stack grows too large
```python
class Node(object):
    """docstring for Node."""
    def __init__(self, val):
        super(Node, self).__init__()
        self.val = val


class SetOfStacks(object):
    """docstring for SetOfStacks."""
    def __init__(self):
        super(SetOfStacks, self).__init__()
        self.stacks = []

```
