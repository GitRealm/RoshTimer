from tkinter import *
import time 


root = Tk()
root.geometry("300x250")
root.title("Time Counter")
frame = Frame(root)


paused = 0
separator = "\n----------------"

aegisTime = 300
aegisLabel = Label(frame, text="\nAegis"+separator)
aegisTimer = Label(frame, text="")

roshMinTime = 480
roshMinLabel = Label(frame, text="\nRosh Min Spawn"+separator)
roshMinTimer = Label(frame, text="")

roshMaxTime = 660
roshMaxLabel = Label(frame, text="\nRosh Max Spawn"+separator)
roshMaxTimer = Label(frame, text="")

resetButton = Button(frame, text = "Reset")

frame.pack()

aegisLabel.pack()
aegisTimer.pack()

roshMinLabel.pack()
roshMinTimer.pack()

roshMaxLabel.pack()
roshMaxTimer.pack()

resetButton.pack()

def countdown(aegisText, minText, maxText):
    
    global aegisTime
    global roshMinTime
    global roshMaxTime

    while not paused:
        
        if aegisTime > -1:
            aegisText.configure(text = formatTime(aegisTime))
            aegisTime -= 1

        if roshMinTime > -1:
            minText.configure(text = formatTime(roshMinTime))
            roshMinTime -= 1
                   
        if roshMaxTime > -1:
            maxText.configure(text = formatTime(roshMaxTime))
            roshMaxTime -= 1

        time.sleep(1)
        root.update()
        
def reset():

    aegisTime = 300
    roshMinTime = 480
    roshMaxTime = 660

    countdown(aegisTimer, roshMinTimer, roshMaxTimer)


def formatTime(seconds):
    mins, secs = divmod(seconds, 60)
    return '{:02d}:{:02d}'.format(mins, secs)

resetButton.configure(command = reset())
countdown(aegisTimer, roshMinTimer, roshMaxTimer)
root.mainloop()
