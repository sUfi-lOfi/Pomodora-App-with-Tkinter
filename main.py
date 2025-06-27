#!/usr/bun/env python3
from tkinter import *

#---------------------Working Mechanism----------------------#

reps = 0
checkmarks_str = ""
timer = None
work_span : int
total_reps : int
#-------------Start Timer------------#
def start_timer():
    global reps
    global work_span
    global total_reps
    short_break = 5 * 60
    long_break = 20 * 60
    try :
        if reps == 0:
            work_span = int(work_int_entry.get())*60
            total_reps = 2*(int(word_periods_entry.get()))
    except ValueError:
        return None
    if reps >= total_reps:
        return None
    reps += 1
    if reps == total_reps:
        status_label.config(text="Break")
        down_counter(long_break)
    elif reps % 2 == 0:
        status_label.config(text="Break")
        down_counter(short_break)
    else :
        status_label.config(text="Work")
        down_counter(work_span)




#-----------Counter Mechanism--------#
def down_counter(n):
    global reps
    global checkmarks_str
    global timer
    mins = n //60
    secs = n % 60
    if mins < 10 :
        mins = f"0{mins}"
    if secs < 10 :
        secs = f"0{secs}"
    canvas.itemconfig(canvas_text, text=f"{mins}:{secs}")
    if  n > 0:
     timer = window.after(1000,down_counter,n-1)
    else:
        if reps % 2 == 0:
            checkmarks_str += " ✅ "
            checkmarks.config(text=checkmarks_str)
        start_timer()

#--------------------Reset Mechanism---------------#

def reset_func():
    global reps
    global timer
    canvas.itemconfig(canvas_text,text = f"00:00")
    reps = 0
    work_int_entry.delete(0,END)
    word_periods_entry.delete(0,END)
    if timer != None:
        window.after_cancel(timer)
#--------------------------------UI Setup-----------------------------#

#------------Canvas Setup----------#
window = Tk()
window.title = "Pomodoro App"
window.config(bg="#FFFFFF",padx=50,pady=50)
window.minsize(width=850,height=400)

canvas = Canvas(width=200,height=224,bg="#FFFFFF",highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,111,image=tomato_img)
canvas_text = canvas.create_text(100,130,fill="#FFFFFF",text="00:00",font=("FreeMono",32,"bold"))

#---------------Status-----------------#
status_label = Label(text = "Status",font=("FreeMono",40,"bold"))

#------------User Input--------------#
work_int_label = Label(text = "Enter the work interval : ",font=("FreeMono",12))
work_int_entry = Entry(width=10)
work_periods = Label(text = "Enter the work interval : ",font=("FreeMono",12))
word_periods_entry = Entry(width=10)

#---------------Start & Reset Button---------------#

start_button = Button(text = "Start",width=5,command = start_timer)
reset_button =  Button(text = "Reset",width=5,command=reset_func)

#----------------CheckMarks----------------#
emoji = "✅"
checkmarks = Label(text = "")

#------------------Grid Configuration-------------#

status_label.grid(row=1,column=2)
canvas.grid(row=2,column=2)
work_int_label.grid(row=3,column=1,padx = 10,pady = 10)
work_int_entry.grid(row=3,column=2,padx = 10,pady = 10)
work_periods.grid(row=4,column=1,padx = 10,pady = 10)
word_periods_entry.grid(row=4,column=2,padx = 10,pady = 10)
start_button.grid(row=5,column=1,pady=10)
reset_button.grid(row=5,column=3,pady=10,padx=20)
checkmarks.grid(row=6,column=2)























window.mainloop()