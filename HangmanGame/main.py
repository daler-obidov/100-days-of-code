import tkinter as tk
from tkinter import messagebox
import random

def load_words(filename="/home/daler/code/HangmanGame/data.txt"):
    try:
        with open(filename, "r") as file:
            words = file.read().splitlines()
            return words
    except FileNotFoundError:
        messagebox.showerror("Error", f"File '{filename}' not found.")
        return []

word_list = load_words()

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("400x650")
        self.word = random.choice(word_list).lower() if word_list else "example"
        self.word_display = ["_" for _ in self.word]
        self.attempts_left = 6
        self.guessed_letters = []
        self.setup_gui()

    def setup_gui(self):
        title_label = tk.Label(self.root, text="Hangman Game", font=("Helvetica", 24, "bold"), bg="Red", fg="Black")
        title_label.pack(pady=10)

        self.word_label = tk.Label(self.root, text=" ".join(self.word_display), font=("Helvetica", 20), bg="Red", fg="#000000")
        self.word_label.pack(pady=20)

        self.canvas = tk.Canvas(self.root, width=200, height=200, bg="Red", highlightthickness=0)
        self.canvas.pack(pady=20)
        self.draw_hangman()

        self.letter_entry = tk.Entry(self.root, font=("Helvetica", 18), width=5, bg="Red", fg="#333333", highlightthickness=0, borderwidth=2, relief="solid")
        self.letter_entry.pack(pady=10)

        self.guess_button = tk.Button(self.root, text="Guess", font=("Courier", 20), bg="Green", fg="#013220", command=self.guess_letter)
        self.guess_button.pack(pady=10)

        self.attempts_label = tk.Label(self.root, text=f"Attempts Left: {self.attempts_left}", font=("Helvetica", 16), bg="", fg="yellow")
        self.attempts_label.pack(pady=10)

        self.guessed_label = tk.Label(self.root, text="Guessed Letters: " + ", ".join(self.guessed_letters), font=("Helvetica", 16), bg="Red", fg="Blue")
        self.guessed_label.pack(pady=10)

    def draw_hangman(self):
        self.canvas.delete("all")
        self.canvas.create_line(50, 180, 150, 180, width=3)
        self.canvas.create_line(100, 180, 100, 20, width=3)
        self.canvas.create_line(100, 20, 150, 20, width=3)
        self.canvas.create_line(150, 20, 150, 40, width=3)

        if self.attempts_left <= 5:
            self.canvas.create_oval(130, 40, 170, 80, width=3, fill="#ffcccb")
            self.root.configure(bg="#FFA07A")
        if self.attempts_left <= 4:
            self.canvas.create_line(150, 80, 150, 130, width=3, fill="#000000")
            self.root.configure(bg="#FF7F50")
        if self.attempts_left <= 3:
            self.canvas.create_line(150, 90, 130, 110, width=3, fill="#000000")
            self.root.configure(bg="#FF6347")
        if self.attempts_left <= 2:
            self.canvas.create_line(150, 90, 170, 110, width=3, fill="#000000")
            self.root.configure(bg="#FF0000")
        if self.attempts_left <= 1:
            self.canvas.create_line(150, 130, 130, 160, width=3, fill="#000000")
            self.root.configure(bg="#8B0000")
        if self.attempts_left == 0:
            self.canvas.create_line(150, 130, 170, 160, width=3, fill="#000000")
            self.root.configure(bg="Black")

    def guess_letter(self):
        guessed_letter = self.letter_entry.get().lower()
        self.letter_entry.delete(0, tk.END)

        if len(guessed_letter) != 1 or not guessed_letter.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
            return

        if guessed_letter in self.guessed_letters:
            messagebox.showinfo("Hangman", f"You already guessed the letter '{guessed_letter}'!")
            return

        self.guessed_letters.append(guessed_letter)
        self.guessed_label.config(text="Guessed Letters: " + ", ".join(self.guessed_letters))

        if guessed_letter in self.word:
            for i, letter in enumerate(self.word):
                if letter == guessed_letter:
                    self.word_display[i] = guessed_letter
            self.word_label.config(text=" ".join(self.word_display))

            if "_" not in self.word_display:
                messagebox.showinfo("Hangman", f"Congratulations! You guessed the word '{self.word}'!")
                self.reset_game()
        else:
            self.attempts_left -= 1
            self.attempts_label.config(text=f"Attempts Left: {self.attempts_left}")
            self.draw_hangman()

            if self.attempts_left == 0:
                messagebox.showinfo("Hangman", f"You've run out of attempts! The word was '{self.word}'.")
                self.reset_game()

    def reset_game(self):
        self.word = random.choice(word_list).lower() if word_list else "example"
        self.word_display = ["_" for _ in self.word]
        self.attempts_left = 6
        self.guessed_letters = []

        self.word_label.config(text=" ".join(self.word_display))
        self.attempts_label.config(text=f"Attempts Left: {self.attempts_left}")
        self.guessed_label.config(text="Guessed Letters: ")
        self.draw_hangman()

root = tk.Tk()
game = HangmanGame(root)
root.mainloop()
