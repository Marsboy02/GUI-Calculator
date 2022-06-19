from stackcalc import *
import tkinter as tkt

root = tkt.Tk()
root.title("계산기")
root.resizable(0, 0)  # 윈도우 크기 고정
root.wm_attributes("-topmost", 1)

equa = ""
equation = tkt.StringVar()

calculation = tkt.Label(root, textvariable=equation)
equation.set("계산식을 입력하세요 : ")
calculation.grid(row=2, columnspan=8)


def btnPress(num):
    global equa
    equa = equa + str(num)
    equation.set(equa)
    print()


def EqualPress():
    global equa
    print(equa)
    total = evalPostfix(Infix2Postfix(MakeNewList(list(equa))))
    print(total)
    equation.set(total)
    equa = ""


def ClearPress():
    global equa
    equa = ""
    equation.set("")


button_table = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    ['1', '2', '3', '(', ')'],
    ['4', '5', '6', '-', '+'],
    ['7', '8', '9', '*', '/'],
    ['C', '0', '=', 'sin', '']
]


Button0 = tkt.Button(root, text="0", bg='white', command=lambda: btnPress(0), height=1, width=7, borderwidth=1,
                     relief=tkt.SOLID)
Button0.grid(row=6, column=2, padx=10, pady=10)
Button1 = tkt.Button(root, text="1", bg='white', command=lambda: btnPress(1), height=1, width=7, borderwidth=1,
                     relief=tkt.SOLID)
Button1.grid(row=3, column=1, padx=10, pady=10)
Button2 = tkt.Button(root, text="2", bg='white', command=lambda: btnPress(2), height=1, width=7, borderwidth=1,
                     relief=tkt.SOLID)
Button2.grid(row=3, column=2, padx=10, pady=10)
Button3 = tkt.Button(root, text="3", bg='white', command=lambda: btnPress(3), height=1, width=7, borderwidth=1,
                     relief=tkt.SOLID)
Button3.grid(row=3, column=3, padx=10, pady=10)
Button4 = tkt.Button(root, text="4", bg='white', command=lambda: btnPress(4), height=1, width=7, borderwidth=1,
                     relief=tkt.SOLID)
Button4.grid(row=4, column=1, padx=10, pady=10)
Button5 = tkt.Button(root, text="5", bg='white', command=lambda: btnPress(5), height=1, width=7, borderwidth=1,
                     relief=tkt.SOLID)
Button5.grid(row=4, column=2, padx=10, pady=10)
Button6 = tkt.Button(root, text="6", bg='white', command=lambda: btnPress(6), height=1, width=7, borderwidth=1,
                     relief=tkt.SOLID)
Button6.grid(row=4, column=3, padx=10, pady=10)
Button7 = tkt.Button(root, text="7", bg='white', command=lambda: btnPress(7), height=1, width=7, borderwidth=1,
                     relief=tkt.SOLID)
Button7.grid(row=5, column=1, padx=10, pady=10)
Button8 = tkt.Button(root, text="8", bg='white', command=lambda: btnPress(8), height=1, width=7, borderwidth=1,
                     relief=tkt.SOLID)
Button8.grid(row=5, column=2, padx=10, pady=10)
Button9 = tkt.Button(root, text="9", bg='white', command=lambda: btnPress(9), height=1, width=7, borderwidth=1,
                     relief=tkt.SOLID)
Button9.grid(row=5, column=3, padx=10, pady=10)
Plus = tkt.Button(root, text="+", bg='white', command=lambda: btnPress("+"), height=1, width=7, borderwidth=1,
                  relief=tkt.SOLID)
Plus.grid(row=3, column=4, padx=10, pady=10)
Minus = tkt.Button(root, text="-", bg='white', command=lambda: btnPress("-"), height=1, width=7, borderwidth=1,
                   relief=tkt.SOLID)
Minus.grid(row=4, column=4, padx=10, pady=10)
Multiply = tkt.Button(root, text="*", bg='white', command=lambda: btnPress("*"), height=1, width=7, borderwidth=1,
                      relief=tkt.SOLID)
Multiply.grid(row=5, column=4, padx=10, pady=10)
Divide = tkt.Button(root, text="/", bg='white', command=lambda: btnPress("/"), height=1, width=7, borderwidth=1,
                    relief=tkt.SOLID)
Divide.grid(row=6, column=4, padx=10, pady=10)
sin = tkt.Button(root, text="sin", bg='white', command=lambda: btnPress("sin"), height=1, width=7, borderwidth=1,
                 relief=tkt.SOLID)
sin.grid(row=3, column=5, padx=10, pady=10)
leftBracket = tkt.Button(root, text="(", bg='white', command=lambda: btnPress("("), height=1, width=7, borderwidth=1,
                         relief=tkt.SOLID)
leftBracket.grid(row=4, column=5, padx=10, pady=10)
rightBracket = tkt.Button(root, text=")", bg='white', command=lambda: btnPress(")"), height=1, width=7, borderwidth=1,
                          relief=tkt.SOLID)
rightBracket.grid(row=5, column=5, padx=10, pady=10)

Equal = tkt.Button(root, text="=", bg='white', command=EqualPress, height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Equal.grid(row=6, column=3, padx=10, pady=10)
Clear = tkt.Button(root, text="C", bg='white', command=ClearPress, height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Clear.grid(row=6, column=1, padx=10, pady=10)

root.mainloop()
