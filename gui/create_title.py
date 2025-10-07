from tkinter import *

def create_title(parent):
    title_label = Label(
        parent,
        text="Калькулятор времени загрузки",
        font=("Arial", 18, "bold"),
        bg="#2C2F33",
        fg="#FFFFFF"
    )
    title_label.pack(pady=10)
    return title_label

