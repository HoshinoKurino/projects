import tkinter as tk
from tkinter import *
from tkinter import ttk

window=tk.Tk()
window.title('Kurinos calculator')
window.geometry('570x600')
window.resizable(False,False)
window.config(bg='#1c1d3d')

equation=''

# functions 

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation=''
    label_result.config(text=equation)

def calculator():
    global equation
    result=''
    if equation!='':
        try:
            result=eval(equation)
        except:
            result=='fuck you'
            equation=''
    label_result.config(text=result)

# label

label_result=tk.Label(
    window,
    width=25,
    height=2,
    text='',
    font=('Arial,30')
)

# Functions
## line(C,/,%,*)
clear_button=tk.Button(
    window,
    text='C',
    width=5,
    height=1,
    bd=3,
    bg='#c225a2',
    fg='#fff',
    font=('Arial',30,'bold'),
    command=lambda: clear()
)

divide_button=tk.Button(
    window,
    text='/',
    width=5,
    height=1,
    bd=3,
    bg='#fcfcfc',
    fg='#080808',
    font=('Arial',30,'bold'),
    command=lambda: show('/')
)

divide_button.place(x=150,y=100)

remainder_button=tk.Button(
    window,
    text='%',
    width=5,
    height=1,
    bd=3,
    bg='#fcfcfc',
    fg='#080808',
    font=('Arial',30,'bold'),
    command=lambda: show('%')
)

multiply_button=tk.Button(
    window,
    text='*',
    width=5,
    height=1,
    bd=3,
    bg='#08ffe6',
    fg='#080808',
    font=('Arial',30,'bold'),
    command=lambda: show('*')
)

button7=tk.Button(
    window,
    text='7',
    width=5,
    height=1,
    bd=3,
    bg='#fcfcfc',
    fg='#080808',
    font=('Arial',30,'bold'),
    command=lambda: show('7')
)

button8=tk.Button(
    window,
    text='8',
    width=5,
    height=1,
    bd=3,
    bg='#fcfcfc',
    fg='#080808',
    font=('Arial',30,'bold'),
    command=lambda: show('8')
)

button9=tk.Button(
    window,
    text='9',
    width=5,
    height=1,
    bd=3,
    bg='#fcfcfc',
    fg='#080808',
    font=('Arial',30,'bold'),
    command=lambda: show('9')
)

minus_button=tk.Button(
    window,
    text='-',
    width=5,
    height=1,
    bd=3,
    bg='#08ffe6',
    fg='#080808',
    font=('Arial',30,'bold'),
    command=lambda: show('-')
)

button4=tk.Button(
    window,
    text='4',
    width=5,
    height=1,
    bd=3,
    bg='#fcfcfc',
    fg='#080808',
    font=('Arial',30,'bold'),
    command=lambda: show('4')
)

button5=tk.Button(
    window,
    text='5',
    width=5,
    height=1,
    bd=3,
    bg='#fcfcfc',
    fg='#080808',
    font=('Arial',30,'bold'),
    command=lambda: show('5')
)

button6=tk.Button(
    window,
    text='6',
    width=5,
    height=1,
    bd=3,
    bg='#fcfcfc',
    fg='#080808',
    font=('Arial',30,'bold'),
    command=lambda: show('6')
)

plus_button=tk.Button(
    window,
    text='+',
    width=5,
    height=1,
    bd=3,
    bg='#08ffe6',
    fg='#080808',
    font=('Arial',30,'bold'),
    command=lambda: show('+')
)

button1=tk.Button(
    window,
    text='1',
    width=5,
    height=1,
    bd=3,
    bg='#fcfcfc',
    fg='#080808',
    font=('Arial',30,'bold'),
    command=lambda: show('1')
)

button1.place(x=10,y=400)

button2=tk.Button(
    window,
    text='2',
    width=5,
    height=1,
    bd=3,
    bg='#fcfcfc',
    fg='#080808',
    font=('Arial',30,'bold'),
    command=lambda: show('2')
)

button3=tk.Button(
    window,
    text='3',
    width=5,
    height=1,
    bd=3,
    bg='#fcfcfc',
    fg='#080808',
    font=('Arial',30,'bold'),
    command=lambda: show('3')
)

decimal_button=tk.Button(
    window,
    text='.',
    width=5,
    height=1,
    bd=3,
    bg='#fcfcfc',
    fg='#080808',
    font=('Arial',30,'bold'),
    command=lambda: show('.')
)

button0=tk.Button(
    window,
    text='0',
    width=11,
    height=1,
    bd=3,
    bg='#fcfcfc',
    fg='#080808',
    font=('Arial',30,'bold'),
    command=lambda: show('0')
)

equal_button=tk.Button(
    window,
    text='=',
    width=5,
    height=3,
    bd=3,
    bg='#ff7b08',
    fg='#080808',
    font=('Arial',30,'bold'),
    command=lambda: calculator()
)

equal_button.place(x=430,y=400)

button0.place(x=10,y=500)

decimal_button.place(x=290,y=500)

button3.place(x=290,y=400)

button2.place(x=150,y=400)



plus_button.place(x=430,y=300)

button4.place(x=10,y=300)

button5.place(x=150,y=300)

button6.place(x=290,y=300)

minus_button.place(x=430,y=200)

button9.place(x=290,y=200)

button8.place(x=150,y=200)

button7.place(x=10,y=200)



multiply_button.place(x=430,y=100)

remainder_button.place(x=290,y=100)

clear_button.place(x=10,y=100)

label_result.pack()

window.mainloop()