import tkinter as tk
from tkinter import messagebox
import activity_generator
import rps_game


# activity_generator
def show_activity():
    message = activity_generator.activity_generator()
    messagebox.showinfo("Activity", message)


# rock-paper-scissors-game
def play_rps():
    rps_game.start()


rootWindow = tk.Tk()
rootWindow.title("Python Projects")
rootWindow.minsize(400, 200)

activity_generator_button = tk.Button(rootWindow, text="Generate a fun activity", command=show_activity)
activity_generator_button.pack()

rps_button = tk.Button(rootWindow, text='Rock-Paper-Scissors Game', command=play_rps)
rps_button.pack()

rootWindow.mainloop()
