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
