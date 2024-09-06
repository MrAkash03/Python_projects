import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("_" * 9)

def check_winner(board, player):
    
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    
    for row in board:
        if all(box == player for box in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True


    return False

def is_board_full(board):
    return all(box != " " for row in board for box in row)

def computer_move(board):
    while True:
        col = random.randint(0, 2)
        row = random.randint(0, 2)
        if board[row][col] == " ":
            return row, col

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    human = "X"
    computer= "O"
    current_player = human
    
    while True:
        print_board(board)
        
        if current_player == human:
            col = int(input(f"Player {current_player}, enter the column (0, 1, 2): "))
            row = int(input(f"Player {current_player}, enter the row (0, 1, 2): "))
        else:
            print(f"Computer {current_player} is making a move.")
            row, col = computer_move(board)
        
        if 0 <= col < 3 and 0 <= row < 3 and board[row][col] == " ":
            board[row][col] = current_player
            
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins this match!!!")
                break
            
            if is_board_full(board):
                print_board(board)
                print("The match ends in a draw!!!")
                break
            
            current_player = human if current_player == computer else computer
        else:
            print("It's a Invalid move!!. Please, Try again!!!")

if __name__ == "__main__":
    main()