import random
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class SnakesAndLadders:
    def __init__(self, master):
        self.master = master
        master.title("Snakes & Ladders")

        self.canvas = tk.Canvas(master, width=600, height=600, bg="white")
        self.canvas.grid(row=0, column=0, columnspan=4)

        self.roll_button = tk.Button(master, text="Roll Dice", command=self.play_turn, font=("Arial", 14))
        self.roll_button.grid(row=1, column=0, columnspan=4, pady=10)

        self.turn_label = tk.Label(master, text="Turn: 0", font=("Arial", 12))
        self.turn_label.grid(row=2, column=0, columnspan=4)

        self.reset_game()

    def reset_game(self):
        self.board = [0] * 100
        self.player_position = 0
        self.turns = 0
        self.path = [0]
        self.snake_hits = 0
        self.ladder_hits = 0
        self.generate_snakes_and_ladders()
        self.draw_board()

    def generate_snakes_and_ladders(self):
        self.snakes = random.sample(range(1, 99), 5)
        self.ladders = []
        while len(self.ladders) < 5:
            pos = random.randint(1, 98)
            if pos not in self.snakes and pos not in self.ladders:
                self.ladders.append(pos)

        for i in self.snakes:
            self.board[i] = -random.randint(5, min(i, 94))
        for i in self.ladders:
            self.board[i] = random.randint(5, min(99 - i, 94))

    def draw_board(self):
        self.canvas.delete("all")
        size = 60
        for i in range(100):
            row = i // 10
            col = i % 10 if row % 2 == 0 else 9 - (i % 10)
            x0, y0 = col * size, 540 - row * size
            x1, y1 = x0 + size, y0 + size
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="#f8f8f8", outline="black")
            self.canvas.create_text((x0 + x1)//2, (y0 + y1)//2, text=str(i), font=("Arial", 8))

        for i in self.snakes:
            self.draw_arrow(i, self.board[i], "red")
        for i in self.ladders:
            self.draw_arrow(i, self.board[i], "green")

        self.draw_player()

    def draw_arrow(self, start, offset, color):
        size = 60
        row = start // 10
        col = start % 10 if row % 2 == 0 else 9 - (start % 10)
        x_start = col * size + size // 2
        y_start = 540 - row * size + size // 2

        end = start + offset
        row_end = end // 10
        col_end = end % 10 if row_end % 2 == 0 else 9 - (end % 10)
        x_end = col_end * size + size // 2
        y_end = 540 - row_end * size + size // 2

        self.canvas.create_line(x_start, y_start, x_end, y_end, arrow=tk.LAST, width=2, fill=color)

    def draw_player(self):
        size = 60
        pos = self.player_position
        row = pos // 10
        col = pos % 10 if row % 2 == 0 else 9 - (pos % 10)
        x = col * size + size // 2
        y = 540 - row * size + size // 2
        self.canvas.create_oval(x-10, y-10, x+10, y+10, fill="blue", outline="black")

    def play_turn(self):
        if self.player_position == 99:
            messagebox.showinfo("Game Over", f"You reached the end in {self.turns} turns!")
            return

        dice = random.randint(1, 6)
        self.turns += 1
        self.turn_label.config(text=f"Turn: {self.turns}")

        new_pos = self.player_position + dice
        if new_pos > 99:
            new_pos = self.player_position
        else:
            if self.board[new_pos] > 0:
                self.ladder_hits += 1
            elif self.board[new_pos] < 0:
                self.snake_hits += 1
            new_pos += self.board[new_pos]
        self.player_position = min(new_pos, 99)
        self.path.append(self.player_position)
        self.draw_board()

        if self.player_position == 99:
            msg = (f"🎉 Game Over!\n"
                   f"Total Turns: {self.turns}\n"
                   f"Ladders Climbed: {self.ladder_hits}\n"
                   f"Snakes Bitten: {self.snake_hits}")
            messagebox.showinfo("Summary", msg)

# Start GUI
root = tk.Tk()
game = SnakesAndLadders(root)
root.mainloop()
