# Tic Tac Toe Game
import random

rows = 3
cols = 3
board = [[" " for _ in range(cols)] for _ in range(rows)]

def initialize_board():
    for i in range(3):
        for j in range (3):
            board[i][j] = " "

def displayboard():
    print("  0 1 2")
    for i in range(3):
        print(i, end=" ")
        for j in range(3):
            print(board[i][j], end=" ")
        print()

def computer_move():
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                return 

def user_move():
    while True:
        try:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Cell already occupied! Try again.")
        except (ValueError, IndexError):
            print("Invalid input! Please enter numbers between 0 and 2.")       

def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

def main():
    initialize_board()
while True:
    displayboard()
    user_move()
    if check_winner():
        displayboard()
        print("Congratulations! You win!")
        break
    computer_move()
    if check_winner():
        displayboard()
        print("Computer wins!")
        break
    if all(board[i][j] != " " for i in range(3) for j in range(3)):
        displayboard()
        print("It's a draw!")
        break
    if all(board[i][j] != " " for i in range(3) for j in range(3)):
        displayboard()
        print("It's a draw!")
        break
main()