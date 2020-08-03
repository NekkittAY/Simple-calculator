# Made by NekkittAY and Habr website
from tkinter import *
from math import *

class Calc(Frame):
    def __init__(self, root):
        super(Calc, self).__init__(root)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"), bg="#000", foreground="#FFF")
        self.lbl.place(x=11, y=50)
        self.lbl1 = Label(text="Made by NekkittAY and Habr website", font=("Times New Roman", 21, "bold"), bg="#000", foreground="#FFF")
        self.lbl1.place(x=10, y=785)
        
        buttons = [
            "C", "DEL", "*", "=",
            "1", "2", "3", "/",
            "4", "5", "6", "+",
            "7", "8", "9", "-",
            "(", "0", ")", "x^2",
            "√", "π", "e", "x!",
            "|x|", "sin", "cos",
            "tg", "ln", "lg", "Loss_func",
            "1-Loss_func"
        ]

        x = 10
        y = 140
        for button in buttons:
            command = lambda x=button: self.logicalc(x)
            Button(text=button, bg="#FFF",
                   font=("Times New Roman", 15),
                   command=command).place(x=x, y=y,
                                      width=115,
                                      height=79)
            x += 117
            if x > 400:
                x = 10
                y += 81

    def logicalc(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation == "x^2":
            self.formula = str((eval(self.formula))**2)
        elif operation == "=":
            self.formula = str(eval(self.formula))
        elif operation == "√":
            self.formula = str(sqrt(eval(self.formula)))
        elif operation == "x!":
            self.formula = str(factorial(eval(self.formula)))
        elif operation == "|x|":
            self.formula = str(fabs(eval(self.formula)))
        elif operation == "sin":
            self.formula = str(sin(eval(self.formula)))
        elif operation == "cos":
            self.formula = str(cos(eval(self.formula)))
        elif operation == "tg":
            self.formula = str(tan(eval(self.formula)))
        elif operation == "ln":
            self.formula = str(log1p(eval(self.formula)))
        elif operation == "lg":
            self.formula = str(log10(eval(self.formula)))
        elif operation == "Loss_func":
            self.formula = str(erf(eval(self.formula)))
        elif operation == "1-Loss_func":
            self.formula = str(erfc(eval(self.formula)))
        else:
            if self.formula == "0":
                self.formula = ""
            elif self.formula == "π":
                self.formula = str(pi)
            elif self.formula == "e":
                self.formula = str(e)
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        elif self.formula == "π":
            self.formula = str(pi)
        elif self.formula == "e":
            self.formula = str(e)
        self.lbl.configure(text=self.formula)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#000"
    root.geometry("485x820")
    root.title("Калькулятор_Крота")
    root.resizable(False, False)
    app = Calc(root)
    app.pack()
    root.mainloop()

