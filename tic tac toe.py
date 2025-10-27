def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board, player):
    # Check rows, columns and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Row
            return True
        if all([board[j][i] == player for j in range(3)]):  # Column
            return True

    # Diagonals
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def is_full(board):
    return all([cell != " " for row in board for cell in row])

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        print(f"Player {current_player}'s turn.")
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
        except ValueError:
            print("❌ Invalid input! Please enter numbers only.")
            continue

        if row not in range(3) or col not in range(3):
            print("❌ Invalid position! Choose between 1 and 3.")
            continue

        if board[row][col] != " ":
            print("⚠️ That cell is already occupied. Try again.")
            continue

        # Make the move
        board[row][col] = current_player
        print_board(board)

        # Check for a winner
        if check_winner(board, current_player):
            print(f"🏆 Player {current_player} wins!")
            break

        # Check for draw
        if is_full(board):
            print("🤝 It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Run the game
tic_tac_toe()
