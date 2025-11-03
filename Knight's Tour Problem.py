# Knight's Tour Problem using Backtracking

N = 8  # Size of chessboard (8x8)

def print_solution(board):
    for row in board:
        print(' '.join(str(x).rjust(2, '0') for x in row))
    print()

# All 8 possible moves for a knight
move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]

# Check if position is safe
def is_safe(x, y, board):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

# Recursive utility function
def solve_knight_tour(board, curr_x, curr_y, move_count):
    # Base case: If all squares visited
    if move_count == N * N:
        return True

    # Try all next moves
    for i in range(8):
        next_x = curr_x + move_x[i]
        next_y = curr_y + move_y[i]
        if is_safe(next_x, next_y, board):
            board[next_x][next_y] = move_count
            if solve_knight_tour(board, next_x, next_y, move_count + 1):
                return True
            board[next_x][next_y] = -1  # Backtrack
    return False

# Main driver
def knight_tour():
    board = [[-1 for _ in range(N)] for _ in range(N)]

    # Starting position
    board[0][0] = 0

    if solve_knight_tour(board, 0, 0, 1):
        print("✅ Knight's tour solution found:\n")
        print_solution(board)
    else:
        print("❌ No solution exists.")

knight_tour()
