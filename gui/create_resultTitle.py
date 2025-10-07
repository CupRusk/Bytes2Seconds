from tkinter import *

def create_resultTitle(parent):
    result_label = Label(
        parent,
        text="",
        font=("Arial", 14, "bold"),
        bg="#2C2F33",
        fg="#00FF00"
    )
    result_label.pack(pady=20)
    
    return result_label