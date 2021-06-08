from tkinter import *
from tkinter import ttk
import time 
from global_hotkeys import *


root = Tk()
root.geometry("250x265")
root.title("Rosh Timer")
root.configure(bg="#23272A")

frame = Frame(root)
frame.configure(bg="#23272A")

aegisTime = 300
roshMinTime = 480
roshMaxTime = 660

aegisLabel = Label(frame, text="\nAegis:\n", bg="#23272A", fg="#FFFFFF")
roshMinLabel = Label(frame, text="\nRosh Min Spawn:\n", bg="#23272A", fg="#FFFFFF")
roshMaxLabel = Label(frame, text="\nRosh Max Spawn:\n", bg="#23272A", fg="#FFFFFF")

aegisTimer = Label(frame, text="", bg="#23272A", fg="#FFFFFF")
roshMinTimer = Label(frame, text="", bg="#23272A", fg="#FFFFFF")
roshMaxTimer = Label(frame, text="", bg="#23272A", fg="#FFFFFF")

sep = ttk.Separator(frame, orient='horizontal')
sep1 = ttk.Separator(frame, orient='horizontal')
sep2 = ttk.Separator(frame, orient='horizontal')

frame.pack()

aegisLabel.pack()
sep.place(relwidth=50, y=33)
aegisTimer.pack()

roshMinLabel.pack()
sep1.place(relwidth=50, y=105)
roshMinTimer.pack()

roshMaxLabel.pack()
sep2.place(relwidth=50, y=177)
roshMaxTimer.pack()


def countdown():
    
    global aegisTime
    global roshMinTime
    global roshMaxTime
    global paused

    if not paused:
        
        if aegisTime > -1:
            aegisTimer.configure(text = formatTime(aegisTime))
            aegisTime -= 1

        if roshMinTime > -1:
            roshMinTimer.configure(text = formatTime(roshMinTime))
            roshMinTime -= 1
                   
        if roshMaxTime > -1:
            roshMaxTimer.configure(text = formatTime(roshMaxTime)+'\n')
            roshMaxTime -= 1

    root.after(1000,countdown)

     
def reset():
    global aegisTime
    global roshMinTime
    global roshMaxTime

    aegisTime = 300
    roshMinTime = 480
    roshMaxTime = 660

def formatTime(seconds):
    mins, secs = divmod(seconds, 60)
    return '{:02d}:{:02d}'.format(mins, secs)

def pauseTimer():
    global paused
    global aegisTime
    global roshMinTime
    global roshMaxTime

    if paused == 1:
        paused -= 1
        pauseLabel = "Pause"
    else:
        paused += 1
        pauseLabel = "Resume"

    pauseButton.configure(text = pauseLabel)


paused = 0
pauseLabel = "Pause"
pauseButton = Button(frame, text = pauseLabel, command = pauseTimer, bg="#23272A", fg="#FFFFFF")
pauseButton.pack(side = LEFT )

resetButton = Button(frame, text = "Reset", command = reset, bg="#23272A", fg="#FFFFFF")
resetButton.pack(side = RIGHT)
countdown()

bindings = [
   [["control", "d"], None, reset],
   [["control", "g"], None, pauseTimer],
   ]

register_hotkeys(bindings)
start_checking_hotkeys()

root.mainloop()

