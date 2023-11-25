import tkinter as tk
from datetime import datetime, timedelta

class CountdownTimer:
    def __init__(self, root, task_name, task_duration_minutes, start_time_str, alert_time_minutes=None, flash_time=None):
        if start_time_str is None:
            raise ValueError('Start time must be provided.')

        self.root = root
        self.taskName = task_name
        self.task_label = tk.Label(root, text=self.taskName, font=('Helvetica', 16))
        self.task_label.pack(fill=tk.BOTH, expand=True)

        self.alert_time = alert_time_minutes * 60 if alert_time_minutes is not None else None
        self.flash_time = flash_time if flash_time is not None else 5
        self.duration_seconds = task_duration_minutes * 60

        # Check if alert time is provided and less than or equal to duration
        if self.alert_time is not None and self.alert_time > self.duration_seconds:
            raise ValueError('Alert time is greater than duration time')

        # Convert start time string to datetime object
        self.start_time = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S')
        self.end_time = self.start_time + timedelta(seconds=self.duration_seconds)

        self.label = tk.Label(root, font=('Helvetica', 48))
        self.label.pack(fill=tk.BOTH, expand=True)

        self.update_timer()

    def update_timer(self):
        current_time = datetime.now()

        if self.start_time<= current_time < self.end_time:
            remaining_time = self.end_time - current_time

            # Check if alert time is reached and less than duration
            if self.alert_time is not None and (self.alert_time - self.flash_time) < remaining_time.total_seconds() <= self.alert_time:
                self.flash_task_label()
            elif self.task_label.cget('text') == '':
                self.task_label.config(text=self.taskName)

            # Display the remaining time in the timer label
            time_str = str(remaining_time).split('.')[0]
            if remaining_time.total_seconds() >= 3600:
                self.label.config(text=time_str)
            else:
                self.label.config(text=time_str[2:])  # Remove leading zero for less than an hour

            self.root.after(1000, self.update_timer)
        else:
            self.label.pack_forget()
            self.task_label.pack_forget()


    def flash_task_label(self, flashes_remaining=None):
        # Flash the task label on and off for specified seconds or default to 5 seconds
        if flashes_remaining is None:
            flashes_remaining = self.flash_time

        if flashes_remaining > 0:
            if (datetime.now().second % 2 == 0):
                self.task_label.config(text="")
            else:
                self.task_label.config(text=self.taskName)
            self.root.after(1000, lambda: self.flash_task_label(flashes_remaining - 1))

if __name__ == "__main__":
    root = tk.Tk()

    # Task details
    task_name = "Complete Task"
    task_duration_minutes = 1.1  # Example: 15 minutes

    # Specify alert time (e.g., 2 minutes before the end)
    alert_time_minutes = 1

    # Specify flash time (e.g., 3 seconds)
    flash_time_seconds = 5

    # Specify start time as string (e.g., '2023-01-01 12:00:00')
    start_time_str = '2023-01-01 12:00:00'

    timer = CountdownTimer(root, task_name, task_duration_minutes, start_time_str, alert_time_minutes=alert_time_minutes, flash_time=flash_time_seconds)

    root.mainloop()
