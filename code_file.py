#Tic-Tac-Toe game

#creating board
board = []

for i in range(3):
    row = ["-","-","-"]
    board.append(row)

def print_board(board):
    for row in board:
        print(" | ".join(row))
    print()

#checking does our board full
def is_full(board):
    for row in board:
        if "-" in row:
            return False
    return True

#checking winner
def check_winner(board, player):

    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def play_game():
    #Taking input and updating the board
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s Turn")

        while True:
            try:
                row = int(input("Enter row (1,2 or 3 ): ")) -1
                col = int(input("Enter col (1,2 or 3 ): ")) -1

                if row not in range(3) or col not in range(3):
                    print("Invalid input. please enter 1,2 or 3.")
                    continue

                if board[row][col] != "-":
                    print("Cell already Taken. choose another ")
                    continue

                board[row][col] = current_player
                break

            except ValueError:
                print("Please enter valid numbers. ")
        if check_winner(board, current_player):
            print_board(board)
            print(f" player {current_player} wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw! ")
            break
    
        current_player = "O" if current_player == "X" else "X"

play_game()
