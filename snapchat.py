def is_bst(node, max_val, min_val):
    if node == None:
        return True
    if node.left.val > max_val:
        return False
    if node.right.val < min_val:
        return False
    return is_bst(node.left, node.val, min_val) and is_bst(node.right, max_val, node.val)