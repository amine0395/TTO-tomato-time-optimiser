from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
time = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    start_btn.configure(state=NORMAL)
    window.after_cancel(time)
    canvas.itemconfig(timer, text="00:00")
    title.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    start_btn.configure(state=DISABLED)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 ==0:
        count_down(long_break_sec)
        title.config(text="LONG BREAK",fg=RED)

    elif reps %2 ==0:
        count_down(short_break_sec)
        title.config(text="SHORT BREAK", fg=PINK)

    else :
        count_down(work_sec)
        title.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    min= int(count/60)
    sec= count % 60
    if sec <10 and min<10 and count>0:
        sec=str(sec)
        min=str(min)
        canvas.itemconfig(timer, text="0"+str(min) + ":0" + str(sec))
    elif sec<10 and count>0:
        sec = str(sec)
        min = str(min)
        canvas.itemconfig(timer, text=str(min) + ":0" + str(sec))
    elif sec>10 and min>10 and count>0:
        sec = str(sec)
        min = str(min)
        canvas.itemconfig(timer,text=str(min)+":"+str(sec))
    if count>0:
      global time
      time =window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark=""
        for i in int(reps/2):
            mark+=" ✔"
        check_marks.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.iconbitmap("tomato.ico")
window.title("tomato brain help")
window.config(pady=50,padx=100, bg="#A084DC")


title= Label(text="Timer:", fg=RED,bg="#A084DC",highlightthickness=0)
title.config(font=(FONT_NAME,35,"bold"))
title.grid(column=1,row=0)

canvas = Canvas(width=200,height=224,bg="#A084DC",highlightthickness=0)
photo=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=photo)
timer=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME, 35 ,"bold"))
canvas.grid(column=1,row=1)


start_btn = Button(text="start",highlightthickness=0,command=start_timer)
reset_btn = Button(text="reset",highlightthickness=0,command=reset_timer)
start_btn.grid(column=0,row=2)
reset_btn.grid(column=2,row=2)


check_marks=Label(text="",fg=GREEN,bg="#A084DC")
check_marks.grid(column=1,row=2)
window.mainloop()
