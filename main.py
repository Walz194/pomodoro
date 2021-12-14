import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Pomodoro')
window.resizable(width=False,height=False)
window.config(bg=YELLOW,padx=100,pady=50)

# Check on the canvas widget
canvas = tkinter.Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
# We can't pass in a direct image location. We in fact need a an object called "PhotoImage"
tomato_img = tkinter.PhotoImage(file="tomato.png")
# When we create an image, we need to specify the x,y position of the image. I want it in the center, so i am taking half of the width and height
canvas.create_image(100,112,image=tomato_img)
canvas.create_text(100,130,text='00:00',fill='white',font=(FONT_NAME,35,'bold'))
canvas.pack()



window.mainloop()