from tkinter import *
from tkinter.ttk import *
from time import strftime

clock = Tk()
clock.title("Clock")


def time():
    # Time format in Hour: Minutes : Second & AM/PM
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)
    
    
# Colors are changeable. Tkinter supports "white", "black", "red", "green", "blue", "cyan", "yellow", and "magenta" . For more just Google it.

label = Label(clock, font=("ds-digital", 60),
              background="black", foreground="magenta") 
label.pack(anchor='center')
time()

mainloop()
