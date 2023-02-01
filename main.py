# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
import string



def spin_values():

    if pass_vars.get() == 1:
        LETTERS = int(letters_spin.get())
        NUMBERS = int(numbers_spin.get())
        SYMBOLS = int(symbols_spin.get())
    else:
        LETTERS = 6
        NUMBERS = 2
        SYMBOLS = 0
    generator(LETTERS, NUMBERS, SYMBOLS)

def generator(let,numbers,sym):

    alpha = list(string.ascii_letters)
    nums = list(string.digits)
    syms = list(string.punctuation)
    main_list = []
    for num in range(let):
        alpha_list = random.choice(alpha)
        main_list.append(alpha_list)
    for num in range(numbers):
        num_list = random.choice(nums)
        main_list.append(num_list)
    for num in range(sym):
        sym_list = random.choice(syms)
        main_list.append(sym_list)
    random.shuffle(main_list)
    new_pass = ''.join(map(str, main_list))
    pass_entry.delete(0,"end")
    pass_entry.insert(0,new_pass)
# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

BLACK = "#2C3333"
DARK_BLUE = "#395B64"
LIGHT_BLUE = "#A5C9CA"
WHITE = "#E7F6F2"
FONT_NAME = "Courier"

def checkbox_clicked():
    if pass_vars.get() == 1:
        letters_label.grid(column=0,row=5,sticky="e")
        letters_spin.grid(column=1, row=5,sticky="w")
        numbers_label.grid(column=1, row=5)
        numbers_spin.grid(column=1, row=5,sticky="e")
        symbols_label.grid(column=2, row=5)
        symbols_spin.grid(column=3, row=5,sticky="e")
        let_var = IntVar(window)
        num_var = IntVar(window)
        let_var.set(6)
        num_var.set(2)
        letters_spin.config(textvariable=let_var)
        numbers_spin.config(textvariable=num_var)
    else:
        letters_label.grid_forget()
        letters_spin.grid_forget()
        numbers_label.grid_forget()
        numbers_spin.grid_forget()
        symbols_label.grid_forget()
        symbols_spin.grid_forget()


window = Tk()
window.title("Password Manager")
window.minsize(width=600,height=400)
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

pass_button = Button(text="Generate Password",bg=WHITE,fg=BLACK,command=spin_values)
pass_button.grid(column=2,row=3,sticky="NW")

save_button = Button(text="Save",bg=WHITE,fg=BLACK,width=50)
save_button.grid(column=1 ,row=8,columnspan=2)

#CHECK DOX DROPDOWN
letters_label = Label(text="Letters",font=(FONT_NAME,12,"bold"),pady=10,fg=LIGHT_BLUE,bg=BLACK)
letters_spin = Spinbox(from_=0,to=20,width=5)

numbers_label = Label(text="  Numbers",font=(FONT_NAME,12,"bold"),pady=10,fg=LIGHT_BLUE,bg=BLACK,padx=10)
numbers_spin = Spinbox(from_=0,to=20,width=5)

symbols_label = Label(text="Symbols",font=(FONT_NAME,12,"bold"),pady=10,fg=LIGHT_BLUE,bg=BLACK)
symbols_spin = Spinbox(from_=0,to=20,width=5)

pass_vars = IntVar()
pass_checkbox = Checkbutton(text="Password Parameters",command=checkbox_clicked,variable=pass_vars,bg=BLACK,fg=WHITE)
pass_checkbox.grid(column=0,row=4)


window.mainloop()