# Write a function to swap a number in place
```python
def swap_1(a, b):
    return a, b = b, a

def swap_2(a, b):
    n = b - a
    a = n + a
    b = b - n
    return a, b
```

# Design an algorithm to figure out if someone has won a game of tic tac toe
```python
def has_winner(board):
    return right_diag(board, 1, 1) or left_diag(board, 1, len(board) - 2) or columns(board, 0, 0) or horizontal(board, 0, 0)

def right_diag(board, row, col):
    if row == len(board) - 1 or col == len(board) - 1:
        return True
    if board[row - 1][col - 1] != board[row][col]:
        return False
    return right_diag(board, row + 1, col + 1)

def left_diag(board, row, col):
    if row == len(board) - 1 or col == 0:
        return True
    if board[row - 1][col + 1] != board[row][col]:
        return False
    return right_diag(board, row + 1, col - 1)
```
