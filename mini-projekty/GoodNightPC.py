import os
import time
import threading
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from datetime import datetime, timedelta


class ShutdownApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer systemowy")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        self.timer_thread = None
        self.stop_flag = False

        # Wybór akcji
        self.action_var = tk.StringVar(value="shutdown")
        ttk.Label(root, text="Akcja do wykonania:", font=("Arial", 12)).pack(pady=5)
        ttk.Radiobutton(root, text="Wyłącz", variable=self.action_var, value="shutdown").pack()
        ttk.Radiobutton(root, text="Uruchom ponownie", variable=self.action_var, value="restart").pack()
        ttk.Radiobutton(root, text="Uśpij", variable=self.action_var, value="sleep").pack()

        # Minutnik
        ttk.Label(root, text="Odliczanie (minuty):", font=("Arial", 12)).pack(pady=5)
        self.minutes_entry = ttk.Entry(root)
        self.minutes_entry.pack()

        # Godzina
        ttk.Label(root, text="Lub wyłącz o godzinie (HH:MM):", font=("Arial", 12)).pack(pady=5)
        self.time_entry = ttk.Entry(root)
        self.time_entry.pack()

        # Przycisk start
        self.start_btn = ttk.Button(root, text="Start", command=self.start_timer, bootstyle="success")
        self.start_btn.pack(pady=10)

        # Przycisk anuluj
        self.cancel_btn = ttk.Button(root, text="Anuluj", command=self.cancel_timer, bootstyle="danger")
        self.cancel_btn.pack()

        # Status
        self.status_label = ttk.Label(root, text="Brak aktywnego timera.", font=("Arial", 11))
        self.status_label.pack(pady=10)

    def start_timer(self):
        if self.timer_thread and self.timer_thread.is_alive():
            messagebox.showwarning("Uwaga", "Timer już działa!")
            return

        minutes = self.minutes_entry.get().strip()
        time_str = self.time_entry.get().strip()

        delay = None
        if minutes:
            try:
                delay = int(minutes) * 60
            except ValueError:
                messagebox.showerror("Błąd", "Podaj poprawną liczbę minut.")
                return
        elif time_str:
            try:
                target_time = datetime.strptime(time_str, "%H:%M").time()
                now = datetime.now()
                target_dt = datetime.combine(now.date(), target_time)
                if target_dt < now:
                    target_dt += timedelta(days=1)  # jeśli godzina już minęła → jutro
                delay = (target_dt - now).seconds
            except ValueError:
                messagebox.showerror("Błąd", "Podaj godzinę w formacie HH:MM.")
                return
        else:
            messagebox.showwarning("Uwaga", "Podaj czas w minutach lub godzinę.")
            return

        action = self.action_var.get()
        self.stop_flag = False
        self.timer_thread = threading.Thread(target=self.run_timer, args=(delay, action))
        self.timer_thread.start()
        self.status_label.config(text=f"Timer ustawiony. Akcja za {delay // 60} minut.")

    def run_timer(self, delay, action):
        for _ in range(delay):
            if self.stop_flag:
                return
            time.sleep(1)

        if not self.stop_flag:
            self.execute_action(action)

    def cancel_timer(self):
        if self.timer_thread and self.timer_thread.is_alive():
            self.stop_flag = True
            self.status_label.config(text="Timer anulowany.")
            messagebox.showinfo("Info", "Timer został anulowany.")
        else:
            messagebox.showinfo("Info", "Brak aktywnego timera.")

    def execute_action(self, action):
        if action == "shutdown":
            cmd = "shutdown /s /t 1" if os.name == "nt" else "shutdown -h now"
        elif action == "restart":
            cmd = "shutdown /r /t 1" if os.name == "nt" else "reboot"
        elif action == "sleep":
            cmd = "rundll32.exe powrprof.dll,SetSuspendState 0,1,0" if os.name == "nt" else "systemctl suspend"
        else:
            return

        os.system(cmd)


if __name__ == "__main__":
    app = ttk.Window(themename="flatly")
    ShutdownApp(app)
    app.mainloop()
