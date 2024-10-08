"""Tkinter -- utility to design the GUI wiz Graphical User Interface. It is indeed one of the fastest and easiest ways to build GUI application. 
Moreover, Tkinter is cross-platform, hence the same code works on macOS, Windows, and Linux."""

# Importing the necessary modules
import re
from tkinter import *
from math import factorial

result =0
operand =" "
expression =" "
equation = " "
def get_number(number): 
    global expression,equation
    expression = expression + str(number)
    equation.set(expression)
    

def get_operator(operator): 
    global expression, equation
    # or'0' part ensures that the expression will be set to "0", which is the appropriate value when the user enters just zeros.
    expression = expression.lstrip('0') or '0' 
    expression = expression + str(operator)
    equation.set(expression)
    

# to evaluate expression
def calculate():
    global expression 
    try:
        # Remove leading zeros from the expression before evaluation
        # This works for numbers but leaves operators intact
        """
        \b0+: This ensures that we're matching leading zeros at the start of numbers.
        For example,In 00056, it matches all three leading 0s.
        (?!\b): This ensures that we don't accidentally remove a 0 that is by itself.
        For example, if the number is just 0, we want to leave it alone, rather than removing it and leaving an empty string.
        """
        cleaned_expression = re.sub(r'\b0+(?!\b)', '', expression)
        
        result = str(eval(cleaned_expression))  # Evaluate the cleaned expression
        
        equation.set(result)
        expression =result
    except Exception as e:
        equation.set("Error")
        expression = " "

def clear_all():
    
    global expression 
    expression =" "
    equation.set("")
    
# draft the window for our calculator which will accommodate the buttons.
gui = Tk() # returns a new top level widget on screen SCREENNAME
# set the background of GUI window
gui.configure(background="light green")

# set the screen size
gui.geometry("290x250")

# set the title of the window
gui.title('Simple Calculator')

 # design the buttons and put them on our application window.
equation = StringVar()
 # Entry() helps in making the text input field.
display = Entry(gui,font=("Arial", 10), insertwidth=20, textvariable=equation, justify="right", width=20)
# grid() - to define the positioning associated with buttons or input field.
display.grid(row=1, columnspan=4, ipadx=70, ipady=10)

# code to add buttons to the calculator
Button(gui,text="1",command=lambda:get_number("1"),height = 2, width = 8).grid(row=2,column=0, sticky=N+E+W+S)
Button(gui,text="2",command=lambda:get_number("2"),height = 2, width = 8).grid(row=2,column=1,sticky=N+E+W+S)
Button(gui,text="3",command=lambda:get_number("3"),height = 2, width = 8).grid(row=2,column=2,sticky=N+E+W+S)

Button(gui,text="4",command=lambda:get_number("4"),height = 2, width = 8).grid(row=3,column=0,sticky=N+E+W+S)
Button(gui,text="5",command=lambda:get_number("5"),height = 2, width = 8).grid(row=3,column=1,sticky=N+E+W+S)
Button(gui,text="6",command=lambda:get_number("6"),height = 2, width = 8).grid(row=3,column=2,sticky=N+E+W+S)

Button(gui,text="7",command=lambda:get_number("7"),height = 2, width = 8).grid(row=4,column=0,sticky=N+E+W+S)
Button(gui,text="8",command=lambda:get_number("8"),height = 2, width = 8).grid(row=4,column=1,sticky=N+E+W+S)
Button(gui,text="9",command=lambda:get_number("9"),height = 2, width = 8).grid(row=4,column=2,sticky=N+E+W+S)

# add other buttons to the calculator
Button(gui,text="AC",command=lambda:clear_all(),height = 2, width = 8).grid(row=5,column=0,sticky=N+E+W+S)
Button(gui,text="0",command=lambda:get_number("0"),height = 2, width = 8).grid(row=5,column=1,sticky=N+E+W+S)
Button(gui,text=".",command=lambda:get_number("."),height = 2, width = 8).grid(row=5,column=2,sticky=N+E+W+S)

Button(gui,text="+",command=lambda:get_operator("+"),height = 2, width = 8).grid(row=2,column=3,sticky=N+E+W+S)
Button(gui,text="-",command=lambda:get_operator("-"),height = 2, width = 8).grid(row=3,column=3,sticky=N+E+W+S)
Button(gui,text="*",command=lambda:get_operator("*"),height = 2, width = 8).grid(row=4,column=3,sticky=N+E+W+S)
Button(gui,text="/",command=lambda:get_operator("/"),height = 2, width = 8).grid(row=5,column=3,sticky=N+E+W+S)

Button(gui,text="=",command= lambda:calculate(),height = 2).grid(row=6,columnspan=4,sticky=N+E+W+S)




gui.mainloop()