import random
import numpy as np
import os

class Game2048:
    def __init__(self, size=4):
        self.size = size
        self.grid = np.zeros((self.size, self.size), dtype=int)
        self.score = 0
        self.high_score = self.load_high_score()
        self.won = False  # Pour vérifier si le joueur a déjà atteint 2048
        self.add_new_tile()
        self.add_new_tile()

    def load_high_score(self):
        if os.path.exists("high_score.txt"):
            with open("high_score.txt", "r") as file:
                return int(file.read())
        return 0

    def save_high_score(self):
        if self.score > self.high_score:
            with open("high_score.txt", "w") as file:
                file.write(str(self.score))

    def add_new_tile(self):
        empty_cells = list(zip(*np.where(self.grid == 0)))
        if empty_cells:
            x, y = random.choice(empty_cells)
            self.grid[x][y] = 4 if random.random() > 0.9 else 2

    def slide_row_left(self, row):
        new_row = [i for i in row if i != 0]
        for i in range(len(new_row) - 1):
            if new_row[i] == new_row[i + 1]:
                new_row[i] *= 2
                self.score += new_row[i]  # Increment score when tiles merge
                new_row[i + 1] = 0
        new_row = [i for i in new_row if i != 0]
        return new_row + [0] * (len(row) - len(new_row))

    def move_left(self):
        old_grid = self.grid.copy()
        self.grid = np.array([self.slide_row_left(row) for row in self.grid])
        if not np.array_equal(old_grid, self.grid):
            self.add_new_tile()
            self.check_win_condition()

    def move_right(self):
        old_grid = self.grid.copy()
        self.grid = np.array([self.slide_row_left(row[::-1])[::-1] for row in self.grid])
        if not np.array_equal(old_grid, self.grid):
            self.add_new_tile()
            self.check_win_condition()

    def move_up(self):
        old_grid = self.grid.copy()
        self.grid = np.transpose(self.grid)
        self.move_left()
        self.grid = np.transpose(self.grid)
        if not np.array_equal(old_grid, self.grid):
            self.add_new_tile()
            self.check_win_condition()

    def move_down(self):
        old_grid = self.grid.copy()
        self.grid = np.transpose(self.grid)
        self.move_right()
        self.grid = np.transpose(self.grid)
        if not np.array_equal(old_grid, self.grid):
            self.add_new_tile()
            self.check_win_condition()

    def check_win_condition(self):
        if not self.won and np.any(self.grid == 2048):
            self.won = True
            self.display()
            continue_game = input("Congratulations, you've reached 2048! Do you want to continue playing? (yes/no): ").lower()
            if continue_game != 'yes':
                self.save_high_score()
                print(f"Your score: {self.score} has been saved.")
                self.stop_game()
                exit()

    def can_move(self):
        if np.any(self.grid == 0):
            return True
        for i in range(self.size):
            for j in range(self.size - 1):
                if self.grid[i, j] == self.grid[i, j + 1] or self.grid[j, i] == self.grid[j + 1, i]:
                    return True
        return False

    def is_game_over(self):
        return not self.can_move()

    def display(self):
        print(f"Score: {self.score}  High Score: {self.high_score}")
        print(self.grid)

    def stop_game(self):
        print("Game stopped.")
        self.save_high_score()
        print(f"Your score: {self.score} has been saved.")

def main():
    size = int(input("Enter the size of the grid (e.g., 4 for 4x4): "))
    game = Game2048(size)
    while True:
        game.display()
        move = input("Enter move (z/q/s/d) or 'stop' to quit: ").lower()
        if move == 'z':
            game.move_up()
        elif move == 's':
            game.move_down()
        elif move == 'q':
            game.move_left()
        elif move == 'd':
            game.move_right()
        elif move == 'stop':
            game.stop_game()
            break
        else:
            print("Invalid move. Use 'z', 'q', 's', 'd', or 'stop'.")

        if game.is_game_over():
            print("Game Over!")
            game.save_high_score()
            game.display()
            break

main()
