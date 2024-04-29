import tkinter as tk
from tkinter import messagebox
import activity_generator
import rps_game
import QR_codes


# activity_generator
def show_activity():
    message = activity_generator.activity_generator()
    messagebox.showinfo("Activity", message)


# rock-paper-scissors-game
def play_rps():
    rps_game.start()


def scan_qrcode():
    QR_codes.scan()


rootWindow = tk.Tk()
rootWindow.title("Python Projects")
rootWindow.minsize(400, 200)

activity_generator_button = tk.Button(rootWindow, text="Generate a fun activity", command=show_activity)
activity_generator_button.pack()

rps_button = tk.Button(rootWindow, text='Rock-Paper-Scissors Game', command=play_rps)
rps_button.pack()

scan_qrcode = tk.Button(rootWindow, text='QR code', command=scan_qrcode)
scan_qrcode.pack()

rootWindow.mainloop()
