import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x300")
        self.root.config(bg="#87CEEB")

        # Game variables
        self.secret_number = random.randint(1, 50)
        self.guesses_left = 5
        self.game_over = False

        # Title
        title = tk.Label(self.root, text="Guess the Number (1-50)",
                        font=("Arial", 18, "bold"), bg="#87CEEB")
        title.pack(pady=20)

        # Guesses remaining
        self.guesses_label = tk.Label(self.root, text=f"Guesses remaining: {self.guesses_left}",
                                      font=("Arial", 12), bg="#87CEEB")
        self.guesses_label.pack(pady=10)

        # Feedback label
        self.feedback_label = tk.Label(self.root, text="",
                                       font=("Arial", 11), bg="#87CEEB", fg="#333333")
        self.feedback_label.pack(pady=10)

        # Entry frame
        entry_frame = tk.Frame(self.root, bg="#87CEEB")
        entry_frame.pack(pady=10)

        tk.Label(entry_frame, text="Your guess:", font=("Arial", 10), bg="#87CEEB").pack(side=tk.LEFT, padx=5)

        self.entry = tk.Entry(entry_frame, font=("Arial", 10), width=10)
        self.entry.pack(side=tk.LEFT, padx=5)
        self.entry.bind('<Return>', lambda e: self.make_guess())

        # Guess button
        guess_btn = tk.Button(self.root, text="Guess", command=self.make_guess,
                             font=("Arial", 10), bg="#4CAF50", fg="white", padx=20, pady=5)
        guess_btn.pack(pady=10)

        # Reset button (hidden initially)
        self.reset_btn = tk.Button(self.root, text="Play Again", command=self.reset_game,
                                   font=("Arial", 10), bg="#2196F3", fg="white", padx=20, pady=5)

        self.entry.focus()

    def make_guess(self):
        if self.game_over:
            return

        try:
            guess = int(self.entry.get())
            if guess < 1 or guess > 50:
                self.feedback_label.config(text="Please enter a number between 1 and 50!", fg="red")
                return

            self.guesses_left -= 1

            if guess == self.secret_number:
                self.win_game()
            elif guess < self.secret_number:
                self.feedback_label.config(text="Too low! Try again.", fg="orange")
            else:
                self.feedback_label.config(text="Too high! Try again.", fg="orange")

            self.guesses_label.config(text=f"Guesses remaining: {self.guesses_left}")

            if self.guesses_left == 0 and guess != self.secret_number:
                self.lose_game()

            self.entry.delete(0, tk.END)
            self.entry.focus()

        except ValueError:
            self.feedback_label.config(text="Please enter a valid number!", fg="red")

    def win_game(self):
        self.game_over = True
        self.root.config(bg="#2d5016")  # Minecraft grass

        # Update all text colors for Minecraft theme
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(bg="#2d5016", fg="#FFFF00")  # Yellow text on green
            elif isinstance(widget, tk.Frame):
                widget.config(bg="#2d5016")

        self.feedback_label.config(text="🎮 YOU WIN! Minecraft mode activated! 🎮",
                                  font=("Arial", 14, "bold"), fg="#FFFF00")
        self.entry.config(state="disabled")
        self.reset_btn.pack(pady=10)

    def lose_game(self):
        self.game_over = True
        self.root.config(bg="#8B0000")  # Dark red

        # Update all text colors for sad theme
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(bg="#8B0000", fg="#FFFFFF")
            elif isinstance(widget, tk.Frame):
                widget.config(bg="#8B0000")

        self.feedback_label.config(text=f"😭 GAME OVER! 😭\nThe number was {self.secret_number}",
                                  font=("Arial", 12, "bold"), fg="#FFFFFF")
        self.entry.config(state="disabled")
        self.reset_btn.pack(pady=10)

    def reset_game(self):
        self.secret_number = random.randint(1, 50)
        self.guesses_left = 5
        self.game_over = False

        self.root.config(bg="#87CEEB")
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(bg="#87CEEB", fg="#333333")
            elif isinstance(widget, tk.Frame):
                widget.config(bg="#87CEEB")

        self.guesses_label.config(text=f"Guesses remaining: {self.guesses_left}")
        self.feedback_label.config(text="")
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)
        self.entry.focus()
        self.reset_btn.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
