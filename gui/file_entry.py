from tkinter import *
from tkinter import ttk

def create_fileEntry(parent, frame_file):
    file_entry = ttk.Entry(frame_file, width=15)
    file_entry.pack(side=LEFT, padx=10)
    return file_entry