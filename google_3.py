class Node():
    def __init__(self, lower, upper, parent):
        self.lower = lower
        self.upper = upper
        self.parent = parent
        self.left_child = None
        self.right_child = None
        self.left_child_count = 0
        self.right_child_count = 0

    def split(self, i, node):
        if self.lower >= i <= self.upper:
            if self.lower == i:
                self.lower += 1
                return (self, [self.upper - self.lower + 1])
            elif self.upper == i:
                self.upper -= i
                return (self, [self.upper - self.lower + 1])
            else:
                left_empty = (self.lower, i - 1)
                right_empty = (i + 1, self.upper)
                if self.left_child_count > self.right_child_count:
                    self.lower, self.upper = left_empty
                    right_child = Node(right_empty[0], right_empty[1], self)
                    if self.right_child:
                        self.right_child.add_node(right_child)
                else:
                    self.lower, self.upper = right_empty
                    left_child = Node(left_empty[0], left_empty[1], self)
                    if self.left_child:
                        self.left_child.add_node(left_child)
        else:
            left_top = self.split(i, node.left_child)
            right_top = self.split(i, node.right_child)

    def add_node(self, new_node):




# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(P, K):
    if K is len(P):
        return 0
    top = Node(0, len(P) - 1, None)
    for i in P:
        top, k_groups = top.split(i, top)
        if K in k_groups:
            return i
    return None