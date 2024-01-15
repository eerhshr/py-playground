import tkinter as tk
from tkinter import messagebox
import activity_generator


def show_activity():
    message = activity_generator.activity_generator()
    messagebox.showinfo("Activity", message)


rootWindow = tk.Tk()
rootWindow.title("Activity Generator")
rootWindow.minsize(400, 200)


button = tk.Button(text="Generate a fun activity", command=show_activity)
button.pack()

message_label = tk.Label(rootWindow, text="")
message_label.pack()

rootWindow.mainloop()
