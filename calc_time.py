from tkinter import messagebox

def calc_time(speed_MBps, file_entry, result_label, callback):
    if speed_MBps is None:
        messagebox.showerror("Ошибка", "Сначала введи скорость!")
        return

    try:
        file_size = float(file_entry.get())
        if file_size <= 0:
            raise ValueError

        size_MB = file_size * 1024  # ГБ → МБ
        time_sec = size_MB / speed_MBps

        hours = int(time_sec // 3600)
        minutes = int((time_sec % 3600) // 60)
        seconds = int(time_sec % 60)

        result_label.config(
            text=f"Примерное время: {hours}ч {minutes}м {seconds}с",
            fg="#00FF00"
        )

        callback(time_sec)
    except ValueError:
        messagebox.showerror("Ошибка", "Введи корректное число!")
