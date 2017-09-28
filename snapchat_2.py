def max_trees(k):
    if k == 0:
        return 1
    left_count = 0
    right_count = 0
    total = 0
    for nodes in range(1, k):
        left_count += max_trees(nodes - 1)
        right_count += max_trees(n - nodes)
        total += left_count + right_count
        left_count, right_count = 0, 0
    return total