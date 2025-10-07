from tkinter import messagebox

def set_speed(mbbit_entry, result_label, callback):
    try:
        num = float(mbbit_entry.get())
        speed_MBps = num / 8.3886
        result_label.config(text=f"Скорость ≈ {speed_MBps:.2f} MB/s", fg="#00FF00")
        callback(speed_MBps)  # передаём значение обратно в main.py
    except ValueError:
        messagebox.showerror("Ошибка", "Введи число!")
