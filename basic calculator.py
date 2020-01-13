from tkinter import *


class calculator:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("312x324")
        self.window.resizable(0, 0)
        self.window.title("Calcualtor")
        self.expression = ""
        self.input_text = StringVar()
        self.input_frame = Frame(self.window, width=312, height=50, bd=0,
                                 highlightbackground="yellow", highlightcolor="black",
                                 highlightthickness=1)
        self.input_frame.pack(side=TOP)
        self.input_field = Entry(self.input_frame, font=('arial', 16, 'bold'),
                                 textvariable=self.input_text, width=50, bg="black", fg='white', bd=0, justify=RIGHT)
        self.input_field.grid(row=0, column=0)
        self.input_field.pack(ipady=10)
        self.btns_frame = Frame(self.window, width=400, height=280, bg="pink")
        self.btns_frame.pack()
        # first row
        self.clear = Button(self.btns_frame, text="AC", fg="black", width=32,
                            height=3, bd=0, bg="light grey", cursor="hand2", command=lambda:
            self.btn_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady
        =1)
        self.divide = Button(self.btns_frame, text="/", fg="white", width=10,
                             height=3, bd=0, bg="orange", cursor="hand2", command=lambda:
            self.btn_click("/")).grid(row=0, column=3, padx=1, pady=1)
        # second row
        self.seven = Button(self.btns_frame, text="7", fg="white", width=10,
                            height=3, bd=0, bg="black", cursor="hand2", command=lambda:
            self.btn_click(7)).grid(row=1, column=0, padx=1, pady=1)
        self.eight = Button(self.btns_frame, text="8", fg="white", width=10,
                            height=3, bd=0, bg="black", cursor="hand2", command=lambda:
            self.btn_click(8)).grid(row=1, column=1, padx=1, pady=1)
        self.nine = Button(self.btns_frame, text="9", fg="white", width=10, height
        =3, bd=0, bg="black", cursor="hand2", command=lambda:
        self.btn_click(9)).grid(row=1, column=2, padx=1, pady=1)
        self.multiply = Button(self.btns_frame, text="*", fg="white", width=10,
                               height=3, bd=0, bg="orange", cursor="hand2", command=lambda:
            self.btn_click("*")).grid(row=1, column=3, padx=1, pady=1)
        # third row
        self.four = Button(self.btns_frame, text="4", fg="white", width=10, height
        =3, bd=0, bg="black", cursor="hand2", command=lambda:
        self.btn_click(4)).grid(row=2, column=0, padx=1, pady=1)
        self.five = Button(self.btns_frame, text="5", fg="white", width=10, height
        =3, bd=0, bg="black", cursor="hand2", command=lambda:
        self.btn_click(5)).grid(row=2, column=1, padx=1, pady=1)
        self.six = Button(self.btns_frame, text="6", fg="white", width=10, height
        =3, bd=0, bg="black", cursor="hand2", command=lambda:
        self.btn_click(6)).grid(row=2, column=2, padx=1, pady=1)
        self.minus = Button(self.btns_frame, text="-", fg="white", width=10,
                            height=3, bd=0, bg="orange", cursor="hand2", command=lambda:
            self.btn_click("-")).grid(row=2, column=3, padx=1, pady=1)
        # fourth row
        self.one = Button(self.btns_frame, text="1", fg="white", width=10, height
        =3, bd=0, bg="black", cursor="hand2", command=lambda:
        self.btn_click(1)).grid(row=3, column=0, padx=1, pady=1)
        self.two = Button(self.btns_frame, text="2", fg="white", width=10, height
        =3, bd=0, bg="black", cursor="hand2", command=lambda:
        self.btn_click(2)).grid(row=3, column=1, padx=1, pady=1)
        self.three = Button(self.btns_frame, text="3", fg="white", width=10,
                            height=3, bd=0, bg="black", cursor="hand2", command=lambda:
            self.btn_click(3)).grid(row=3, column=2, padx=1, pady=1)
        self.plus = Button(self.btns_frame, text="+", fg="white", width=10, height
        =3, bd=0, bg="orange", cursor="hand2", command=lambda:
        self.btn_click("+")).grid(row=3, column=3, padx=1, pady=1)
        self.zero = Button(self.btns_frame, text="0", fg="white", width=21, height
        =3, bd=0, bg="black", cursor="hand2", command=lambda:
        self.btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady
        =1)
        self.point = Button(self.btns_frame, text=".", fg="white", width=10,
                            height=3, bd=0, bg="black", cursor="hand2", command=lambda:
            self.btn_click(".")).grid(row=4, column=2, padx=1, pady=1)
        self.equals = Button(self.btns_frame, text="=", fg="white", width=10,
                             height=3, bd=0, bg="orange", cursor="hand2", command=lambda:
            self.btn_equal()).grid(row=4, column=3, padx=1, pady=1)
        self.window.mainloop()

    def btn_click(self, item):
        global expression
        self.expression = self.expression + str(item)
        self.input_text.set(self.expression)

    # 'btn_clear' function clears the input field
    def btn_clear(self):
        global expression
        self.expression = ""
        self.input_text.set("")

    def btn_equal(self):
        global expression
        result = str(eval(self.expression))
        self.input_text.set(result)
        self.expression = ""


c1 = calculator()