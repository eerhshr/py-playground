import random
import tkinter as tk
from tkinter import messagebox


def start():
    rps_window = tk.Tk()
    rps_window.title('Rock-Paper-Scissors')
    rps_window.minsize(200, 100)

    rock_button = tk.Button(rps_window, text="Rock", command=lambda: play("Rock"))
    paper_button = tk.Button(rps_window, text="Paper", command=lambda: play("Paper"))
    scissors_button = tk.Button(rps_window, text="Scissors", command=lambda: play("Scissors"))

    rock_button.pack()
    paper_button.pack()
    scissors_button.pack()

    rps_window.mainloop()


def play(user_choice):
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])

    if user_choice == computer_choice:
        return "It's a Tie"
    elif is_win(user_choice, computer_choice):
        result = 'You Win!'
    else:
        result = 'You Lose :('

    message = f"You chose {user_choice}\nComputer chose {computer_choice}\n\n{result}"
    messagebox.showinfo("Result", message)


def is_win(player, computer):
    # rock > scissors; scissors > paper; paper > rock
    if (
            (player == 'Rock' and computer == 'Scissors') or
            (player == 'Scissors' and computer == 'Paper') or
            (player == 'Paper' and computer == 'Rock')
    ):
        return True
