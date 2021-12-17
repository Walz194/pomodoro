import tkinter
import math
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text,text='00:00')
    timer_label.config(text='Timer',fg=GREEN)
    check_mark.config(text='')
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # work_sec = 15
    # short_break_sec = 5
    # long_break_sec = 10

    if (reps%2) != 0:
        print('Working')
        timer_label.config(text='Work')
        count_down(work_sec)
    elif reps == 8:
        print('Long Break')
        timer_label.config(text='Break',fg=RED)
        count_down(long_break_sec)

    else:
        print('Short Break')
        timer_label.config(text='Break',fg=PINK)
        count_down(short_break_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count%60

    if ~count < 0:
        global timer
        timer = window.after(1000,count_down,count-1)
        canvas.itemconfig(timer_text,text=f'{count_min}:{str(count_sec).zfill(2)}')
    elif (count < 0) and (reps < 8):
        start_timer()
        checks = '✔'
        check_mark.config(text=checks*(reps//2))

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Pomodoro')
window.resizable(width=False,height=False)
window.config(bg=YELLOW,padx=100,pady=50)

timer_label = tkinter.Label(text='Timer')
timer_label.config(fg=GREEN,font=(FONT_NAME,35,'bold'),bg=YELLOW)
timer_label.grid(row=0,column=1)

# Check on the canvas widget
canvas = tkinter.Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
# We can't pass in a direct image location. We in fact need a an object called "PhotoImage"
tomato_img = tkinter.PhotoImage(file="tomato.png")
# When we create an image, we need to specify the x,y position of the image. I want it in the center, so i am taking half of the width and height
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text='00:00',fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(row=1,column=1)


start_btn = tkinter.Button(text='Start')
start_btn.config(command=start_timer)
start_btn.grid(row=2,column=0)

reset_btn = tkinter.Button(text='Reset')
reset_btn['command'] = reset_timer
reset_btn.grid(row=2,column=2)

check_mark = tkinter.Label()
check_mark.config(fg=GREEN,bg=YELLOW,)
check_mark.grid(row=3,column=1)



window.mainloop()