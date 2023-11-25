# from tkinter import Tk, Label
# from datetime import datetime, timedelta
# import json
# from timer_module import CountdownTimer

# root = Tk()
# today = datetime.today()

# bgColour = 'black'
# fgColour = 'white'

# clockFontSize = 150
# dateFontSize = 90
# clock = Label(root, text=today.strftime('%I:%M:%S %p'), font=("Arial", clockFontSize), background=bgColour,
#               foreground=fgColour)
# date_label = Label(root, text=today.strftime('%A, %d %B %Y'), font=("Arial", dateFontSize), background=bgColour,
#                    foreground=fgColour)
# date_label.pack(side="bottom", fill='x')
# clock.pack(expand=1, fill='both')

# # Load tasks from JSON file
# tasks = json.load(open('tasks.json', 'r'))

# # Initialize timerStarted as False
# timerStarted = False

# def start_timers_for_due_tasks():
#     global timerStarted
#     current_time = datetime.now()
#     for task_params in tasks:
#         start_time = datetime.strptime(task_params['start_time'], '%Y-%m-%d %H:%M:%S')
#         end_time = start_time + timedelta(minutes=task_params['task_duration_minutes'])
        
#         # Check if the timer has not been started and the condition is met
#         if not timerStarted and start_time <= current_time <= end_time:
#             CountdownTimer(
#                 root,
#                 task_name=task_params['task_name'],
#                 task_duration_minutes=task_params['task_duration_minutes'],
#                 start_time_str=task_params['start_time'],
#                 alert_time_minutes=task_params['alert_time_minutes'],
#                 flash_time=task_params['flash_time_seconds'],
#                 timer_started_variable=timerStarted  # Pass the timerStarted variable
#             )
#             timerStarted = True  # Update timerStarted to True

#         # If the timer has been started and the condition is not met, set timerStarted to False
#         elif timerStarted and not (start_time <= current_time <= end_time):
#             timerStarted = False

# # Initial date
# current_date = today.date()

# def update_date():
#     global current_date
#     if current_date != datetime.today().date():
#         current_date = datetime.today().date()
#         date_label.config(text=current_date.strftime('%A, %d %B %Y'))
#     root.after(60000, update_date)  # Check every minute

# # Function to repeat every 200 milliseconds
# def repeater():
#     global timerStarted
#     time = datetime.now().strftime('%I:%M:%S %p')
#     start_timers_for_due_tasks()
#     if json.load(open('changes.json', 'r'))['changesMade']:
#         print('found change')
#         json.dump({"changesMade": False}, open('changes.json', 'w'))
#     clock.config(text=time)
#     clock.after(400, repeater)

# # Start the repeater function
# repeater()

# # Start the date update function
# update_date()

# # Set window attributes
# root.attributes('-fullscreen', True)
# root.mainloop()



# import tkinter as tk
# from datetime import datetime, timedelta

# class QuarterHourTimer:
#     def __init__(self, root):
#         self.root = root
#         self.label = tk.Label(root, font=('Helvetica', 48))
#         self.label.pack(fill=tk.BOTH, expand=True)
#         self.update_timer()

#     def find_next_quarter_hour(self):
#         current_time = datetime.now()
#         quarters = [15,30,45,60]
#         for quarter in quarters:
#             if current_time.minute <quarter:
#                 return current_time + timedelta(quarter - current_time.minute)

#     def update_timer(self):
#         current_time = datetime.now()
#         next_quarter_hour = self.find_next_quarter_hour()
#         remaining_time = max(next_quarter_hour - current_time, timedelta())

#         # Display the remaining time in the timer label
#         time_str = str(remaining_time).split('.')[0]
#         self.label.config(text=time_str)

#         if remaining_time.total_seconds() == 0:
#             self.root.after(1000, self.find_next_quarter_hour)
#         else:
#             self.root.after(1000, self.update_timer)

# if __name__ == "__main__":
#     root = tk.Tk()
#     timer = QuarterHourTimer(root)
#     root.mainloop()


from tkinter import Tk,Label,Frame
from datetime import datetime,timedelta
def quarterHour(current_time):
        quarters = [15,30,45,60]
        for quarter in quarters:
            if current_time.minute <quarter:
                endTime  = current_time +timedelta(minutes=quarter)-timedelta(minutes=current_time.minute,seconds=current_time.second)
                return str(endTime-current_time).split('.')[0][2:]
root= Tk()
today = datetime.today()

bgColour = 'black'
fgColour = 'white'
dateFontSize = 65

date_label = Label(root, text=today.strftime('%A, %d %B %Y'), font=("Arial", dateFontSize), background=bgColour,
                   foreground=fgColour)
date_label.pack(side="bottom", fill='x')
clockFontSize = 150
clock = Label(root,text=today.strftime('%I:%M:%S %p'),font=("Arial",clockFontSize),background=bgColour,foreground=fgColour)
clock.pack(side='bottom',fill='x')


timer = Label(root,text= quarterHour(datetime.now()),font=("Arial",clockFontSize+20),background=bgColour,foreground=fgColour)
timer.pack(side='top',expand=1,fill='both')
def repeater():
    timeObject = datetime.now()
    time = timeObject.strftime('%I:%M:%S %p')
    clock.config(text=time)
    timer.config(text=quarterHour(timeObject))
    root.after(200,repeater)
repeater()
root.attributes('-fullscreen',True)
root.mainloop() 