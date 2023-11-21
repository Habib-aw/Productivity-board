from tkinter import Tk,Label,Frame
from datetime import datetime

root= Tk()
today = datetime.today()

bgColour = 'black'
fgColour = 'white'

clockFontSize = 150
clock = Label(root,text=today.strftime('%I:%M:%S %p'),font=("Arial",clockFontSize),background=bgColour,foreground=fgColour)
clock.pack(expand=1,fill='both')
def repeater():
    time = datetime.now().strftime('%I:%M:%S %p')
    clock.config(text=time)
    clock.after(200,repeater)
repeater()
root.attributes('-fullscreen',True)
root.mainloop() 
