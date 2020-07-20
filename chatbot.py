from tkinter import *
root = Tk()
def send():
    send = "You =>"+e.get()
    txt.insert(END, "\n"+send)
    if e.get()=="hello":
        txt.insert(END, "\n"+"Bot => Hi there !")
    elif e.get()=="hi":
        txt.insert(END, "\n"+"Bot => Hi there !")
    elif e.get()=="Hello":
        txt.insert(END, "\n"+"Bot => Hi there !")
    elif e.get()=="HELLO":
        txt.insert(END, "\n"+"Bot => Hi there !")
    elif e.get()=="How are you?":
        txt.insert(END, "\n"+"Bot => I am Fine !")
    elif e.get()=="What is your Job?":
        txt.insert(END, "\n"+"Bot => I am here to help you !")
    else :
        txt.insert(END, "\n"+"Bot => Sorry ! I can't Understand.Can i help you in some other way?")
    e.delete(0,END)
txt = Text(root)
txt.grid(row = 0, column = 0, columnspan = 2)
e = Entry(root, width=100)
send = Button(root,text="Send", command = send, bg="red").grid(row = 1, column = 1)
e.grid(row = 1, column = 0)
root.title("CHATBOT")
root.mainloop()
