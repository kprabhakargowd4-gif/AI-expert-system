N = 8  # Size of the chessboard (8x8)

def print_solution(board):
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))
    print("\n")

def is_safe(board, row, col):
    # Check this row on the left
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, col):
    # Base case: All queens placed
    if col >= N:
        print_solution(board)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens(board, col + 1) or res
            board[i][col] = 0  # Backtrack
    return res

def solve():
    board = [[0] * N for _ in range(N)]
    if not solve_nqueens(board, 0):
        print("No solution exists")

# Run the program
solve()
