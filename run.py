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
            self.place_ship(ship, length)

    def place_ship(self, ship, length):
        while True:
            direction = random.choice(['horizontal', 'vertical'])
            if self.can_place_ship(direction, length):
                self.place_ship_on_board(direction, length, ship)
                break

    def can_place_ship(self, direction, length):
        try:
            if direction == 'horizontal':
                x = random.randint(0, 9)
                y = random.randint(0, 9 - length)
                return all(self.board[x][y + i] == 'O' for i in range(length))
            else:
                x = random.randint(0, 9 - length)
                y = random.randint(0, 9)
                return all(self.board[x + i][y] == 'O' for i in range(length))
        except IndexError:
            return False

    def place_ship_on_board(self, direction, length, ship):
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
            for j, cell in enumerate(row):
                if cell == 'X':
                    print(cell, end=' ')
                elif cell == 'O':
                    print('O', end=' ')
                elif not show_ships and cell != 'O':
                    print('O', end=' ')
                else:
                    print(cell, end=' ')
            print()

    def handle_guess(self, x, y):
        try:
            if not (0 <= x < 10 and 0 <= y < 10):
                raise ValueError("Invalid input! Row and column numbers must be between 0 and 9.")
            
            if self.board[x][y] != 'O':
                self.handle_hit(x, y)
            else:
                self.handle_miss(x, y)
        except ValueError as e:
            print(e)

    def handle_hit(self, x, y):
        print("Hit!")
        self.board[x][y] = 'X'
        self.attempts += 1
        ship_hit = self.board[x][y]
        if ship_hit in self.ships:
            self.ships[ship_hit] -= 1
            if self.ships[ship_hit] == 0:
                print(f"You sunk the {ship_hit}!")
                self.remaining_ships -= 1
                del self.ships[ship_hit]
                if self.remaining_ships == 0:
                    print("Congratulations! You sunk all the ships!")

    def handle_miss(self, x, y):
        print("Miss!")
        self.board[x][y] = 'X'
        self.attempts += 1

    def valid_guess(self, x, y):
        if not (0 <= x < 10 and 0 <= y < 10):
            print("Invalid input! Row and column numbers must be between 0 and 9 and contain a space between them.")
            return False
        if self.board[x][y] == 'X':
            print("You already guessed this position.")
            return False
        return True

    def play(self):
        while self.remaining_ships > 0:
            self.print_board()
            try:
                guess = self.get_guess()
                x, y = guess
                if not self.valid_guess(x, y):
                    continue
                self.handle_guess(x, y)
            except ValueError:
                print("Invalid input! Please enter row and column numbers.")
        print(f"Total attempts: {self.attempts}")

    def get_guess(self):
        guess = input("Enter your guess (row column): ").split()
        if len(guess) != 2:
            raise ValueError("Invalid input! Please enter two space-separated integers.")
        x, y = map(int, guess)
        return x, y

def update_leaderboard(player, attempts, leaderboard):
    leaderboard.append((player, attempts))
    leaderboard.sort(key=lambda x: x[1])  
    if len(leaderboard) > 10:
        leaderboard.pop()

def display_leaderboard(leaderboard):
    print("Leaderboard:")
    for i, (player, attempts) in enumerate(leaderboard[:10]):  # Display only top 10 players
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
        while play_again.lower() not in ['yes', 'no']:  # Validate user input
            print("Invalid input! Please enter 'yes' or 'no'.")
            play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
