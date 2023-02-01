# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

BLACK = "#2C3333"
DARK_BLUE = "#395B64"
LIGHT_BLUE = "#A5C9CA"
WHITE = "#E7F6F2"
FONT_NAME = "Courier"

window = Tk()
window.title("Password Manager")
window.minsize(width=200,height=200)
window.config(padx=20,pady=20,bg=BLACK)

image = PhotoImage(file="logo.png")
canvas = Canvas(width=200,height=200,bg=BLACK,highlightthickness=0)
canvas.create_image(100,100,image=image)
canvas.grid(column=1,row=0)

web_label = Label(text="Website:",fg=LIGHT_BLUE,bg=BLACK,font=(FONT_NAME,12,"bold"),)
web_label.grid(column=0,row=1,sticky="e",)
web_entry = Entry(width=50,bg=WHITE,fg=BLACK,)
web_entry.grid(column=1,row=1,columnspan=2,sticky="NW")

user_label = Label(text="Email/Username:",fg=LIGHT_BLUE,bg=BLACK,font=(FONT_NAME,12,"bold"))
user_label.grid(column=0,row=2,sticky="e")
user_entry = Entry(width=50,bg=WHITE,fg=BLACK)
user_entry.grid(column=1,row=2,columnspan=2,sticky="NW")

pass_label = Label(text="Password:",fg=LIGHT_BLUE,bg=BLACK,font=(FONT_NAME,12,"bold"))
pass_label.grid(column=0,row=3,sticky="e")
pass_entry = Entry(width=31,bg=WHITE,fg=BLACK)
pass_entry.grid(column=1,row=3,sticky="NW")

pass_button = Button(text="Generate Password",bg=WHITE,fg=BLACK)
pass_button.grid(column=2,row=3,sticky="NW")

def checkbox_clicked():
    if pass_vars.get() == 1:
        print("Checkbox selected")
    else:
        print("Checkbox deselected")

pass_vars = IntVar()
pass_checkbox = Checkbutton(text="Password Parameters",command=checkbox_clicked(),variable=pass_vars,bg=BLACK,fg=WHITE)
pass_checkbox.grid(column=0,row=4)

window.mainloop()