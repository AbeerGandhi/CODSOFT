import tkinter as tk
calculation = ""


def add(symbol):
    global calculation
    calculation +=str(symbol)
    text_res.delete(1.0, "end")
    text_res.insert(1.0, calculation)

def evaluate():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_res.delete(1.0, "end")
        text_res.insert(1.0, calculation)
    except:
        clear()
        text_res.insert(1.0, "Error")

def clear():
    global calculation
    calculation = ""
    text_res.delete(1.0, "end")


root = tk.Tk()
root.title("Calculator")
root.geometry("289x275")

text_res = tk.Text(root, height=2, width=16, font=("Arial",25))
text_res.grid(columnspan=5)

b1 = tk.Button(root, text="1", command=lambda: add(1), width=5, font=("Arial",15))
b1.grid(row=2, column=1)
b2 = tk.Button(root, text="2", command=lambda: add(2), width=5, font=("Arial",15))
b2.grid(row=2, column=2)
b3 = tk.Button(root, text="3", command=lambda: add(3), width=5, font=("Arial",15))
b3.grid(row=2, column=3)
b4 = tk.Button(root, text="4", command=lambda: add(4), width=5, font=("Arial",15))
b4.grid(row=3, column=1)
b5 = tk.Button(root, text="5", command=lambda: add(5), width=5, font=("Arial",15))
b5.grid(row=3, column=2)
b6 = tk.Button(root, text="6", command=lambda: add(6), width=5, font=("Arial",15))
b6.grid(row=3, column=3)
b7 = tk.Button(root, text="7", command=lambda: add(7), width=5, font=("Arial",15))
b7.grid(row=4, column=1)
b8 = tk.Button(root, text="8", command=lambda: add(8), width=5, font=("Arial",15))
b8.grid(row=4, column=2)
b9 = tk.Button(root, text="9", command=lambda: add(9), width=5, font=("Arial",15))
b9.grid(row=4, column=3)
b0 = tk.Button(root, text="0", command=lambda: add(0), width=5, font=("Arial",15))
b0.grid(row=5, column=2)
bplus = tk.Button(root, text="+", command=lambda: add("+"), width=5, font=("Arial",15))
bplus.grid(row=2, column=4)
bminus = tk.Button(root, text="-", command=lambda: add("-"), width=5, font=("Arial",15))
bminus.grid(row=3, column=4)
bmul = tk.Button(root, text="*", command=lambda: add("*"), width=5, font=("Arial",15))
bmul.grid(row=4, column=4)
bdiv = tk.Button(root, text="/", command=lambda: add("/"), width=5, font=("Arial",15))
bdiv.grid(row=5, column=4)
bbra1 = tk.Button(root, text="(", command=lambda: add("("), width=5, font=("Arial",15))
bbra1.grid(row=5, column=1)
bbra2 = tk.Button(root, text=")", command=lambda: add(")"), width=5, font=("Arial",15))
bbra2.grid(row=5, column=3)
bclear = tk.Button(root, text="C", command=clear, width=11, font=("Arial",15))
bclear.grid(row=6, column=1, columnspan=2)
bequal = tk.Button(root, text="=", command=evaluate, width=11, font=("Arial",15))
bequal.grid(row=6, column=3, columnspan=2)
root.mainloop()