from tkinter import *
import back

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    entry1.delete(0,END)
    entry1.insert(END,selected_tuple[1])
    entry2.delete(0,END)
    entry2.insert(END,selected_tuple[2])
    entry3.delete(0,END)
    entry3.insert(END,selected_tuple[3])
    entry4.delete(0,END)
    entry4.insert(END,selected_tuple[4])
    entry5.delete(0,END)
    entry5.insert(END,selected_tuple[5])
    entry6.delete(0,END)
    entry6.insert(END,selected_tuple[6])

def view_command():
    list1.delete(0,END)
    for row in back.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in back.search(name_text.get(),address_text.get(),phone_number_text.get(),roomtype_text.get(),noof_text.get(),amount_text.get()):
        list1.insert(END,row)

def add_command():
    back.insert(name_text.get(),address_text.get(),phone_number_text.get(),noof_text.get(),roomtype_text.get(),amount_text.get())
    list1.delete(0,END)
    list1.insert(END,(name_text.get(),address_text.get(),phone_number_text.get(),noof_text.get(),roomtype_text.get(),amount_text.get()))

def delete_command():
    back.delete(selected_tuple[0])

def update_command():
    back.update(selected_tuple[0],name_text.get(),address_text.get(),phone_number_text.get(),roomtype_text.get(),noof_text.get(),amount_text.get())



window=Tk()
window.title("Hotel Management System")
label1=Label(window,text="Hotel ROYALE")
label1.grid(row=0,column=2)

label2=Label(window,text="Name")
label2.grid(row=1,column=0)

label3=Label(window,text="Address")
label3.grid(row=2,column=0)

label4=Label(window,text="Phone number")
label4.grid(row=3,column=0)

label5=Label(window,text="Number of days you want to stay in:")
label5.grid(row=4,column=0)

label6=Label(window,text="Room type(Normal , king or delux) :")
label6.grid(row=5,column=0)

label7=Label(window,text="Total amount")
label7.grid(row=6,column=0)

name_text=StringVar()
entry1=Entry(window,textvariable=name_text)
entry1.grid(row=1,column=1)

address_text=StringVar()
entry2=Entry(window,textvariable=address_text)
entry2.grid(row=2,column=1)

phone_number_text=StringVar()
entry3=Entry(window,textvariable=phone_number_text)
entry3.grid(row=3,column=1)

noof_text=StringVar()
entry4=Entry(window,textvariable=noof_text)
entry4.grid(row=4,column=1)

roomtype_text=StringVar()
entry5=Entry(window,textvariable=roomtype_text)
entry5.grid(row=5,column=1)

amount_text=StringVar()
entry6=Entry(window,textvariable=amount_text)
entry6.grid(row=6,column=1)

list1=Listbox(window,height=20,width=59)
list1.grid(row=1,column=3, rowspan=6, columnspan=2)

scrl=Scrollbar(window)
scrl.grid(row=1,column=2, sticky='ns',rowspan=6)

list1.configure(yscrollcommand=scrl.set)
scrl.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View all",width=12, command=view_command, bg="red")
b1.grid(row=7, column=0)

b2=Button(window,text="Add entry",width=12,command=add_command, bg="red")
b2.grid(row=8, column=0)

b3=Button(window,text="Delete entry",width=12,command=delete_command, bg="red")
b3.grid(row=10, column=0)

b4=Button(window,text="Search",width=12,command=search_command, bg="red")
b4.grid(row=7, column=1)

b5=Button(window,text="Update",width=12,command=update_command, bg="red")
b5.grid(row=8, column=1)





window.mainloop()
