from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import string, random

root = Tk()
root.geometry("450x290")
root.title("Password Generator")
root.config(bg="#f0f0f0")
root.resizable(False, False)

def password_generate():
    try:
        length_password = int(solidboss.get())
        include_special = special_var.get()
        small_letters = string.ascii_lowercase
        capital_letters = string.ascii_uppercase
        digits = string.digits
        special_character = string.punctuation if include_special else ''
        
        all_characters = small_letters + capital_letters + digits + special_character
        password_value = ''.join(random.choice(all_characters) for _ in range(length_password))
        
        password.set(password_value)
    except:
        messagebox.askretrycancel("Error !", "Please Try Again.")


Title = Label(root,text="Password Generator",  bg="#f0f0f0", fg="#333333", font=("Arial", 20, "bold"))
Title.pack(anchor="center", pady="10")


special_var = BooleanVar()
special_checkbox = Checkbutton(root, text="Include Special Characters", variable=special_var, bg="#f0f0f0", font=("Arial", 12))
special_checkbox.place(x="50", y="90")

length = Label(root, text="Select the Length of Password  ", fg="#333333", bg="#f0f0f0", font=("Arial", 15))
length.place(x="50", y="50px")

solidboss = IntVar()
Selector = Combobox(root, textvariable=solidboss, state="readonly", width=5)
Selector['values'] = [str(i) for i in range(0, 31)]  
Selector.current(5)  
Selector.place(x="350", y="70")

def on_enter(e):
    generate_btn['bg'] = "grey"
    generate_btn['fg'] = "white"

def on_leave(e):
    generate_btn['bg'] = "white"
    generate_btn['fg'] = "black"   


generate_btn = Button(root, text="Generate Password", fg="black", font=("Arial", 15), cursor="hand2", command=password_generate)
generate_btn.bind("<Enter>", on_enter)
generate_btn.bind("<Leave>", on_leave)
generate_btn.pack(anchor="center", pady="50px")

result_lable = Label(root, text="Password  ", bg="#f0f0f0", font=("Arial", 12))
result_lable.place(x="60", y="160px")

password = StringVar()
password_final = Entry(root, textvariable= password, state="readonly", fg="blue", font=("Arial", 15))
password_final.place(x="150", y="160px")



root.mainloop()