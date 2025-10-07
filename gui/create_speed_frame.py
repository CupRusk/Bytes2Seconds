from tkinter import *
from tkinter import ttk

def create_speed_frame(parent):
    frame = Frame(parent, bg="#23272A", bd=2, relief="ridge")
    frame.pack(pady=10, padx=20, fill="x")
    Label(frame, text="Скорость (Мбит/с):", bg="#23272A", fg="#FFFFFF").pack(side=LEFT, padx=10)
    entry = ttk.Entry(frame, width=15)
    entry.pack(side=LEFT, padx=10)
    return frame, entry
