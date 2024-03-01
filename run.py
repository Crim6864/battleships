# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

# Initialize the board
board_size = 10
board = [['O' for _ in range(board_size)] for _ in range(board_size)]

# Function to print the board
def print_board(board):
    for row in board:
        print(" ".join(row))

# Function to place ships randomly on the board
def place_ships(board, num_ships):
    for _ in range(num_ships):
        while True:
            ship_row = random.randint(0, board_size - 1)
            ship_col = random.randint(0, board_size - 1)
            if board[ship_row][ship_col] != 'S':
                board[ship_row][ship_col] = 'S'
                break

# Function to check if the player's guess is correct
def check_guess(guess_row, guess_col, board):
    if board[guess_row][guess_col] == 'S':
        print("Congratulations! You sunk my battleship!")
        board[guess_row][guess_col] = 'X'
        return True
    else:
        if (guess_row < 0 or guess_row >= board_size) or (guess_col < 0 or guess_col >= board_size):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == 'X':
            print("You've already guessed that one.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = 'X'
        return False

# Main game loop
def battleship_game():
    print("Welcome to Battleship!")
    print_board(board)
    num_ships = 5
    place_ships(board, num_ships)
    turns = 0
    while True:
        print("Turn", turns + 1)
        guess_row = int(input("Guess Row (0-" + str(board_size - 1) + "): "))
        guess_col = int(input("Guess Col (0-" + str(board_size - 1) + "): "))
        if check_guess(guess_row, guess_col, board):
            print_board(board)
            break
        else:
            print_board(board)
            turns += 1
    print("Game Over! You took", turns + 1, "turns.")

# Start the game
battleship_game()