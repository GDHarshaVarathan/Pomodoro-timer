import tkinter as t
import math
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



# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    label.config(text="TIMER",fg=GREEN)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    short_time_sec=SHORT_BREAK_MIN*60
    long_time_sec=LONG_BREAK_MIN*60
    work_sec=WORK_MIN*60
    if reps%8==0:
        count_down(long_time_sec)
        label.config(text="BREAK",fg=PINK)
    elif reps%2==0:
        count_down(short_time_sec)
        label.config(text="BREAK",fg=PINK)
    else:
        count_down(work_sec)
        label.config(text="WORK",fg=RED)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
        
    if count>=0:
        global timer
        timer=window.after(1000,count_down,count-1)
        canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window=t.Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
label=t.Label(text="TIMER",fg=GREEN,font=(FONT_NAME,30,"bold"),bg=YELLOW)
label.grid(row=0,column=1)


reset_button=t.Button(text="reset",command=reset)
reset_button.grid(row=2,column=2)

canvas=t.Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato=t.PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)
start_button=t.Button(text="start",command=start_timer)
start_button.grid(row=2,column=0)

















window.mainloop()
