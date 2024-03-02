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
                if self.can_place_ship(direction, length):
                    self.place_ship(direction, length, ship)
                    break

    def can_place_ship(self, direction, length):
        if direction == 'horizontal':
            x = random.randint(0, 9)
            y = random.randint(0, 9 - length)
            return all(self.board[x][y + i] == 'O' for i in range(length))
        else:
            x = random.randint(0, 9 - length)
            y = random.randint(0, 9)
            return all(self.board[x + i][y] == 'O' for i in range(length))

    def place_ship(self, direction, length, ship):
        if direction == 'horizontal':
            x = random.randint(0, 9)
            y = random.randint(0, 9 - length)
            for i in range(length):
                self.board[x][y + i] = ship[0]
        else:
            x = random.randint(0, 9 - length)
            y = random.randint(0, 9)
            for i in range(length):
                self.board[x + i][y] = ship[0]

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
            guess = self.get_guess()
            x, y = guess
            if self.valid_guess(x, y):
                self.handle_guess(x, y)
            else:
                print("Invalid guess! Please try again.")

    def get_guess(self):
        guess = input("Enter your guess (row column): ").split()
        if len(guess) != 2 or not guess[0].isdigit() or not guess[1].isdigit():
            return (-1, -1)
        return map(int, guess)

    def valid_guess(self, x, y):
        return 0 <= x <= 9 and 0 <= y <= 9 and self.board[x][y] != 'X'

    def handle_guess(self, x, y):
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
        else:
            print("Miss!")
            self.board[x][y] = 'X'
            self.attempts += 1

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
