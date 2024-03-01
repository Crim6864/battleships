import random

class BattleshipGame:
    def __init__(self):
        self.board = [['O' for _ in range(10)] for _ in range(10)]
        self.ships = {'Aircraft Carrier': 5, 'Battleship': 4, 'Submarine': 3, 'Destroyer': 3, 'Patrol Boat': 2}
        self.remaining_ships = len(self.ships)
        self.place_ships()
        self.attempts = 0

    def place_ships(self):
        for ship, length in self.ships.items():
            while True:
                direction = random.choice(['horizontal', 'vertical'])
                if direction == 'horizontal':
                    x = random.randint(0, 9)
                    y = random.randint(0, 9 - length)
                    if all(self.board[x][y + i] == 'O' for i in range(length)):
                        for i in range(length):
                            self.board[x][y + i] = ship[0]
                        break
                else:
                    x = random.randint(0, 9 - length)
                    y = random.randint(0, 9)
                    if all(self.board[x + i][y] == 'O' for i in range(length)):
                        for i in range(length):
                            self.board[x + i][y] = ship[0]
                        break

    def print_board(self, show_ships=False):
        print("  0 1 2 3 4 5 6 7 8 9")
        for i, row in enumerate(self.board):
            print(i, end=' ')
            for cell in row:
                if cell != 'X' or show_ships:
                    print(cell, end=' ')
                else:
                    print('O', end=' ')
            print()

    def play(self):
        while self.remaining_ships > 0:
            self.print_board()
            guess = input("Enter your guess (row column): ").split()
            if len(guess) != 2 or not guess[0].isdigit() or not guess[1].isdigit():
                print("Invalid input! Please enter row and column numbers.")
                continue
            x, y = map(int, guess)
            if x < 0 or x > 9 or y < 0 or y > 9:
                print("Invalid input! Row and column numbers must be between 0 and 9.")
                continue
            if self.board[x][y] == 'X':
                print("You already guessed this position.")
                continue
            if self.board[x][y] != 'O':
                print("Hit!")
                self.board[x][y] = 'X'
                self.attempts += 1
                ship_hit = self.board[x][y]
                self.ships[ship_hit] -= 1
                if self.ships[ship_hit] == 0:
                    print(f"You sunk the {ship_hit}!")
                    self.remaining_ships -= 1
                if self.remaining_ships == 0:
                    print("Congratulations! You sunk all the ships!")
                    break
            else:
                print("Miss!")
                self.board[x][y] = 'X'
                self.attempts += 1
        print(f"Total attempts: {self.attempts}")

def update_leaderboard(player, attempts, leaderboard):
    leaderboard.append((player, attempts))
    leaderboard.sort(key=lambda x: x[1])  # Sort by attempts
    if len(leaderboard) > 10:
        leaderboard.pop()

def display_leaderboard(leaderboard):
    print("Leaderboard:")
    for i, (player, attempts) in enumerate(leaderboard):
        print(f"{i+1}. {player}: {attempts} attempts")

def main():
    leaderboard = []
    while True:
        name = input("Enter your name: ")
        game = BattleshipGame()
        game.play()
        update_leaderboard(name, game.attempts, leaderboard)
        display_leaderboard(leaderboard)
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
