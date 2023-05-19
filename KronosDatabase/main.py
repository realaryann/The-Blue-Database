from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
import sqlite3
count=0

def add_values():
    temp = cur.execute(f"Select * from {tableentry.get()};")
    names = [description[0] for description in temp.description]
    addvalwin= Toplevel()
    addvalwin.configure(bg="lightblue3")
    toplab = Label(addvalwin,text="Add Records to Table",bg="slategrey")
    toplab.configure(font=("modern",40))    
    toplab.pack(padx=50)
    frameval = LabelFrame(addvalwin,padx=50,pady=20,bg="slategrey")
    frameval.pack(padx=50,pady=50)
    columnbox = []
    for j in range(len(names)):
        columnbox.append(Text(frameval,height=1,width=20,wrap=None))
        columnbox[j].insert(INSERT,names[j])
        columnbox[j].grid(row=0,column=j)
        columnbox[j].config(state=DISABLED)
        columnbox[j].configure(font=("Modern",13),bg="slategrey")
    textbox = list()
    for i in range(len(names)):
        textbox.append(Text(frameval, height = 1, width = 20, wrap = None ))
        textbox[i].insert(INSERT,"")
        textbox[i].grid(row=1,column=i)
        textbox[i].configure(font=("Modern",13),bg="slategrey")
    
def view_columns():
    global cur
    global con
    rev = Toplevel()
    rev.configure(bg="lightblue3")
    dem = cur.execute(f"select * from {tableentry.get()};")
    res = dem.fetchall()
    output = Text(rev, height=5, width=30)
    output.configure(font=("modern",15))
    output.pack()
    if (res == []):
        output.insert(END, "No Item in Columns"+'\n')
    else:
        for item in res:
            output.insert(END, str(item)+'\n')
    con.commit()
    
    
def view_table():
    view=Toplevel()
    top = Label(view,text="View/Update Existing Table",bg="slategrey",padx=67)
    top.configure(font=("modern",35))
    top.pack()
    frame=LabelFrame(view,bg="lightblue3",padx=150,pady=150)
    frame.pack()
    print_all_columns=Button(frame,text="Press to view all columns",bg="slategrey",padx=40,pady=30,command=view_columns);
    print_all_columns.grid(row=1,column=0,padx=10,pady=20)
    print_all_columns.configure(font=("modern",15))
    updatebutton = Button(frame, text= "Add Records",padx=86,bg ="slategrey", pady=30,command=add_values)
    updatebutton.grid(row=2,column=0,padx=10,pady=20)
    updatebutton.configure(font=("modern",15))
    view.resizable(False, False)
    
def add_column():
    global tabname
    global count
    count=count+1
    print(count)
    if (count==1):
        query= f"CREATE table {tabname}({cnentry.get()} {result});"
        cur.execute(query)
    else:    
        query1 = f"ALTER table {tabname} add {cnentry.get()} {result};"
        cur.execute(query1)
    con.commit()

    
def new_table_next():
    global result
    global cnentry
    global tabname
    tabname = tablename.get()
    newtableui.destroy()
    nextui = Toplevel()
    nextui.configure(bg="lightblue3")
    nextui.title("Table Initialization")
    nexttop = Label(nextui,text="Table Initialization",bg="slategrey",padx=10,pady=10)
    nexttop.configure(font=("Modern",40))
    nexttop.grid(row=0,column=1,pady=10,padx=40)
    columnname = Label(nextui, text="Enter Column Name",bg="slategrey",padx=10,pady=10)
    columnname.configure(font=("Modern",20))
    columnname.grid(row=1,column=1,pady=20)
    cnentry = Entry(nextui,width=40,borderwidth=5)
    cnentry.grid(row=2,column=1,pady=20)
    result=StringVar()
    result.set("int")
    typeinfo =  Label(nextui, text="Type",bg="slategrey",padx=10,pady=10)
    typeinfo.configure(font=("Modern",15))
    typeinfo.grid(row=3,column=1,pady=10)
    typeentry=OptionMenu(nextui,result,"int","text","real","blob")
    typeentry.grid(row=4,column=1)
    addbut = Button(nextui, text="Add Column",bg="slategrey",padx=10,pady=10,command=add_column)
    addbut.configure(font=("Modern",15))
    addbut.grid(row=5,column=1,pady=20)
    nextui.resizable(False, False)
      
def new_table():
    global newtableui 
    global tabname
    global tablename
    newtableui = Toplevel();
    newtableui.configure(bg="lightblue3")
    newtableui.title("Table Initialization")
    labeltop = Label(newtableui,text="Table Initialization",bg="slategrey",padx=10,pady=10)
    labeltop.grid(row=0,column=1);
    labeltop.configure(font=('Modern',30))
    frametable = LabelFrame(newtableui,bg="slategrey", padx=200,pady=20)
    frametable.grid(row=1,column=1,pady=10)
    tablenamelabel = Label(frametable,text="Enter Table Name",bg ="lightblue3",padx=10,pady=10)
    tablenamelabel.grid(row=0, column=0,pady=10)
    tablenamelabel.configure(font=("Modern",15))
    tablename = Entry(frametable, width=60,borderwidth=5)
    tablename.grid(row=1,column=0)
    nextbutton = Button(frametable,text="Next",bg="lightblue3",padx=10,pady=10,command=new_table_next)
    nextbutton.grid(row=2,column=0,pady=10)
    nextbutton.configure(font=("Modern",16))
    newtableui.resizable(False, False)
    
def pop_up():
    response = messagebox.askyesno("Error Finding Table",f"Did not find table {tableentry.get()} in {data.get()}. Do you want to create a new table?")
    if (response==1):
        sqlitepage.destroy()
        new_table()
        
def check_table():
    global con
    con = sqlite3.connect(data.get())
    global cur
    cur=con.cursor()
    query = f"SELECT tbl_name FROM sqlite_master WHERE type='table' AND tbl_name='{tableentry.get()}';"
    list1=cur.execute(query).fetchall()
    con.commit()
    if list1 == []:
        pop_up()
    else:
        view_table()
    
    
def sqlitepage():
    global sqlitepage
    sqlitepage= Toplevel() 
    sqlitepage.title("Sqlite Initialization")
    sqlitepage.configure(bg="lightblue3")
    label2= Label(sqlitepage,text="Sqlite Initialization",bg="slategrey",padx=10,pady=10)
    label2.config(font=('Modern',30))
    label2.grid(row=0,column=1)
    frame2 = LabelFrame(sqlitepage,bg="slategrey", padx=200,pady=200)
    frame2.grid(row=1,column=1,padx=10,pady=10)
    global data
    data=Entry(frame2,width=60,borderwidth=4);
    data.grid(row =1, column=0)
    datalabel = Label(frame2,text="Enter Database Name",bg="lightblue3",padx=10,pady=10)
    datalabel.grid(row=0,column=0,pady=10)
    tablelabel = Label(frame2,text="Enter Table Name",bg="lightblue3",padx=10,pady=10)
    tablelabel.grid(row=2,column=0,pady=10)
    datalabel.config(font=('Modern',20))
    tablelabel.config(font=('Modern',20))
    global tableentry 
    tableentry= Entry(frame2,width=60,borderwidth=4)
    tableentry.grid(row=3,column=0)
    button1 = Button(frame2,text="Run",padx=10,pady=10,bg = "lightblue3",command = check_table)
    button1.grid(row=4,column=0,pady=10)
    button1.configure(font=('Modern',15))
    sqlitepage.resizable(False, False)

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