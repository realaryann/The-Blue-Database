from tkinter import *
import tkinter.font as tkFont

def sqlitepage():
    sqlitepage = Toplevel()
    sqlitepage.title("Sqlite Initialization")
    label2= Label(sqlitepage,text="Sqlite Initialization",bg="slategrey",padx=10,pady=10)
    label2.config(font=('Modern',30))
    label2.grid(row=0,column=1)
    frame2 = LabelFrame(sqlitepage, padx=200,pady=200)
    frame2.grid(row=1,column=1,padx=10,pady=10)
    

def excelpage():
    pass

root = Tk()
root.title("Kronos Database")
root.configure(bg="lightblue3")
label1 = Label(root,text="Kronos Database",bg="slategrey",padx=10,pady=10)
label1.config(font=('Modern',40))
label1.grid(row=0, column=1)
frame1 = LabelFrame(root,padx=200,pady=200,bg="slategrey")
frame1.grid(row=1,column=1,padx=10,pady=10)
button_sqlite = Button(frame1, text="Start Sqlite Database",bg="lightblue3",padx=88,pady=40, command=sqlitepage)
button_sqlite.pack(pady=20)
button_excel = Button(frame1, text="Start Excel Entry",bg="lightblue3",padx=105,pady=40, command = excelpage)
button_excel.pack(pady=20)

button_sqlite.config(font=('Modern',15))
button_excel.config(font=('Modern',15))
root.resizable(False,False)
root.mainloop()