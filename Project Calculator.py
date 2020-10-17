# importing tkinter 
from tkinter import*
root = Tk() 
root.title("Calculator")

# gave background color black
root.configure(bg='#222')

# made the gui window resizeable
root.resizable(False,False)

# defined a global variable 'operator'
operator = ""

# function for displaying number when button is clicked
def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    equation.set(operator)

# function for clearing the display screen
def btnclear():
    global operator
    operator = " "
    equation.set(operator)

# function to use equal to button and give result for the calculation done
def equalpress():
    # using try and except for handling errors like zero division
    try:
        global operator
        total = float(eval(operator))
        equation.set(total)
        operator = ""
    
    except:
        equation.set("error")
        operator = ""

# specific function for percent sign since eval does not calculate percentage.
def percentcalc(sign):
    global operator
    # using try and except to handle errors
    try:
        percent1 = float(operator)/100
        equation.set(percent1)
        operator=""
    except:
        equation.set("error")
        operator=""
    
# using string variable for input 
equation = StringVar()
# making the input field
input_field = Entry(root, textvariable=equation, width=20, font=("Arial", 20, "bold"), bd=5, justify="right",
                        state="disabled", disabledforeground="black")

# giving no. of columns to be fitted inside this
input_field.grid(columnspan=4)


allclear = Button(root, padx=24, text="A", font=("Helvetica", 15), bg="black", fg="white", relief="raised",command=lambda:btnclear())
allclear.grid(column=0, row=3)
percent = Button(root, padx=23, text="%", font=("Helvetica", 15), bg="black", fg="white", relief="raised", command=lambda:percentcalc("%"))
percent.grid(column=1, row=3)
clear = Button(root, padx=24, text="C", font=("Helvetica", 15), bg="black", fg="white", relief="raised", command=lambda:btnclear())
clear.grid(column=2, row=3)
divide = Button(root, padx=27, text="/", font=("Helvetica", 15), relief="raised", bg="black", fg="white", command=lambda:btnclick("/"))
divide.grid(column=3, row=3)


_7 = Button(root, padx=25, text="7", font=("Helvetica", 15), relief="raised", command=lambda:btnclick("7"))
_7.grid(column=0, row=4)
_8 = Button(root, padx=26, text="8", font=("Helvetica", 15), relief="raised", command=lambda:btnclick("8"))
_8.grid(column=1, row=4)
_9 = Button(root, padx=26, text="9", font=("Helvetica", 15), relief="raised", command=lambda:btnclick("9"))
_9.grid(column=2, row=4)
multiply = Button(root, padx=26, text="x", font=("Helvetica", 15), relief="raised", bg="black", fg="white", command=lambda:btnclick("*"))
multiply.grid(column=3, row=4)

_4 = Button(root, padx=25, text="4", font=("Helvetica", 15), relief="raised", command=lambda:btnclick("4"))
_4.grid(column=0, row=5)
_5 = Button(root, padx=26, text="5", font=("Helvetica", 15), relief="raised", command=lambda:btnclick("5"))
_5.grid(column=1, row=5)
_6 = Button(root, padx=26, text="6", font=("Helvetica", 15), relief="raised", command=lambda:btnclick("6"))
_6.grid(column=2, row=5)
minus = Button(root, padx=27, text="-", font=("Helvetica", 15), relief="raised", bg="black", fg="white", command=lambda:btnclick("-"))
minus.grid(column=3, row=5)


_1 = Button(root, padx=25, text="1", font=("Helvetica", 15), relief="raised", command=lambda:btnclick("1"))
_1.grid(column=0, row=6)
_2= Button(root, padx=26, text="2", font=("Helvetica", 15), relief="raised", command=lambda:btnclick("2"))
_2.grid(column=1, row=6)
_3 = Button(root, padx=26, text="3", font=("Helvetica", 15), relief="raised", command=lambda:btnclick("3"))
_3.grid(column=2, row=6)
plus = Button(root, padx=25, text="+", font=("Helvetica", 15), relief="raised", bg="black", fg="white", command=lambda:btnclick("+"))
plus.grid(column=3, row=6)

_00 = Button(root, padx=19, text="00", font=("Helvetica", 15), relief="raised", command=lambda:btnclick("00"))
_00.grid(column=0, row=7)
_0 = Button(root, padx=26, text="0", font=("Helvetica", 15), relief="raised", command=lambda:btnclick("0"))
_0.grid(column=1, row=7)
_dot= Button(root, padx=28, text=".", font=("Helvetica", 15), relief="raised", command=lambda:btnclick("."))
_dot.grid(column=2, row=7)
_equals = Button(root, padx=25, text="=", font=("Helvetica", 15), relief="raised", bg="red", fg="white", command=equalpress)
_equals.grid(column=3, row=7)


root.mainloop()