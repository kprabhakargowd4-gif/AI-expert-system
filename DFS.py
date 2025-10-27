N = 8  # 8x8 chessboard

def print_board(board):
    for row in board:
        print(" ".join("Q" if i == 1 else "." for i in row))
    print("\n")

def is_safe(board, row, col):
    # Check left side of row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower-left diagonal
    for i, j in zip(range(row + 1, N), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def dfs(board, col):
    # Base case: all queens placed
    if col == N:
        print_board(board)
        return True

    for row in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place queen
            if dfs(board, col + 1):  # Recurse to next column
                return True
            board[row][col] = 0  # Backtrack

    return False

def solve_8_queens_dfs():
    board = [[0] * N for _ in range(N)]
    if not dfs(board, 0):
        print("No solution exists")

# Run the program
solve_8_queens_dfs()
