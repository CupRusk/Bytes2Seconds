from tkinter import *

def create_frame_file(parent):
    frame_file = Frame(parent, bg="#23272A", bd=2, relief="ridge")
    frame_file.pack(pady=10, padx=20, fill="x")

    label = Label(
        frame_file,
        text="Размер файла (ГБ):",
        bg="#23272A",
        fg="#FFFFFF",
        font=("Arial", 12)
    )
    label.pack(side=LEFT, padx=10, pady=10)

    return frame_file
