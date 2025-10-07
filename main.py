from tkinter import *
from tkinter import ttk, messagebox

# -- Функций
from set_speed import set_speed
from calc_time import calc_time

# -- Рендер с других файлова для читаемости
from gui.create_speed_frame import create_speed_frame
from gui.create_title import create_title
from gui.frame_file import create_frame_file
from gui.file_entry import create_fileEntry
from gui.create_resultTitle import create_resultTitle

speed_MBps = None
time = None

# --- функции для кнопок ---
def on_set_speed():
    set_speed(mbbit_entry, result_label, set_speed_value)

def on_calc_time():
    calc_time(speed_MBps, file_entry, result_label, calc_time_value)


# --- колбэки для приёма значений ---
def set_speed_value(value):
    global speed_MBps
    speed_MBps = value

def calc_time_value(value):
    global time
    time = value


# --- окно ---
win = Tk()
win.title("Калькулятор времени загрузки")
win.geometry("500x350")
win.configure(bg="#2C2F33")

# --- Блок подключения к GUI ---
title_label = create_title(win)
frame_speed, mbbit_entry = create_speed_frame(win)
frame_file = create_frame_file(win)
file_entry = create_fileEntry(win, frame_file)
result_label = create_resultTitle(win)

# -- Кнопачки
btn_speed = ttk.Button(frame_speed, text="Сохранить скорость", command=on_set_speed)
btn_speed.pack(side=LEFT, padx=10)
# --
btn_time = ttk.Button(frame_file, text="Рассчитать время", command=on_calc_time)
btn_time.pack(side=LEFT, padx=10)
# --


win.mainloop()
