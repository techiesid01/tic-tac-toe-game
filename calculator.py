from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.configure(bg="#03fcb5")

e = Entry(root, width=35, borderwidth=5,bg="#75faff")
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def button_click(number):
    #e.delete(0, END)
    current=e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))
def button_clear():
    e.delete(0, END)

def button_add():
    first_number=e.get()
    global f_num
    global math
    math="addition"
    f_num=int(first_number)
    e.delete(0, END)
    
def button_equal():
    second_number=e.get()
    e.delete(0, END)

    if math=="addition":
        e.insert(0, f_num+int(second_number))
    if math=="subtraction":
        e.insert(0, f_num-int(second_number))
    if math=="multiplication":
        e.insert(0, f_num*int(second_number))
    if math=="division":
        e.insert(0, f_num/float(second_number))
        
    
def button_subtract():
    first_number=e.get()
    global f_num
    global math
    math="subtraction"
    f_num=int(first_number)
    e.delete(0, END)
    
def button_multiply():
    first_number=e.get()
    global f_num
    global math
    math="multiplication"
    f_num=int(first_number)
    e.delete(0, END)
    
def button_divide():
    first_number=e.get()
    global f_num
    global math
    math="division"
    f_num=int(first_number)
    e.delete(0, END)
# define buttons

b1 = Button(root, text="1",padx=40,pady=20, command=lambda: button_click(1),bg="#03fcb5",font=("times",12,'bold'))
b2 = Button(root, text="2",padx=40,pady=20, command=lambda: button_click(2),bg="#03fcb5",font=("times",12,'bold'))
b3 = Button(root, text="3",padx=40,pady=20, command=lambda: button_click(3),bg="#03fcb5",font=("times",12,'bold'))
b4 = Button(root, text="4",padx=40,pady=20, command=lambda: button_click(4),bg="#03fcb5",font=("times",12,'bold'))
b5 = Button(root, text="5",padx=40,pady=20, command=lambda: button_click(5),bg="#03fcb5",font=("times",12,'bold'))
b6 = Button(root, text="6",padx=40,pady=20, command=lambda: button_click(6),bg="#03fcb5",font=("times",12,'bold'))
b7 = Button(root, text="7",padx=40,pady=20, command=lambda: button_click(7),bg="#03fcb5",font=("times",12,'bold'))
b8 = Button(root, text="8",padx=40,pady=20, command=lambda: button_click(8),bg="#03fcb5",font=("times",12,'bold'))
b9 = Button(root, text="9",padx=40,pady=20, command=lambda: button_click(9),bg="#03fcb5",font=("times",12,'bold'))
b0 = Button(root, text="0",padx=40,pady=20, command=lambda: button_click(0),bg="#03fcb5",font=("times",12,'bold'))
bad = Button(root, text="+",padx=40,pady=20, command=button_add,bg="#03fcb5",font=("times",12,'bold'))
beq = Button(root, text="=",padx=91,pady=20, command=button_equal,bg="#03fcb5",font=("times",12,'bold'))
b_clear = Button(root, text="C",padx=91,pady=20, command=button_clear,bg="#03fcb5",font=("times",12,'bold'))

bsub = Button(root, text="-",padx=41,pady=20, command=button_subtract,bg="#03fcb5",font=("times",13,'bold'))
bmul = Button(root, text="x",padx=40,pady=20, command=button_multiply,bg="#03fcb5",font=("times",13,'bold'))
bdiv = Button(root, text="/",padx=41,pady=20, command=button_divide,bg="#03fcb5",font=("times",13,'bold'))

# put them on screen
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)
5
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)

b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)

b0.grid(row=4,column=0)
bad.grid(row=5,column=0)
beq.grid(row=5,column=1,columnspan=2)
b_clear.grid(row=4,column=1,columnspan=2)

bsub.grid(row=6,column=0)
bmul.grid(row=6,column=1)
bdiv.grid(row=6,column=2)

root.mainloop()
