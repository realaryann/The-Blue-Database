from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
import sqlite3
import csv
count=0
primcheck=0

def validation(text):
    test = text.get()
    if len(test) == 0:
        msg = "You have entered Empty Text!"
        messagebox.showinfo('Error', msg)
        return 1
    else:
        return 0

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
    
def insert_call():
    lister=[]
    for j in range(len(names)):
        if (textbox[j].get(1.0, "end-1c")).isnumeric():
            lister.append(int(textbox[j].get(1.0, "end-1c")))
        elif isfloat(textbox[j].get(1.0, "end-1c")):
            lister.append(float(textbox[j].get(1.0, "end-1c")))
        else:
            lister.append(textbox[j].get(1.0, "end-1c"))
    i=len(names)
    demo = "?,"
    demo=demo*i
    query = f"Insert into {tableentry.get()} values({demo[0:-1]});"
    messagebox.showinfo('Success!',"The Entry has been added!")
    cur.execute(query,lister)
    con.commit()
    
def add_values():
    global names
    temp = cur.execute(f"Select * from {tableentry.get()};")
    names = [description[0] for description in temp.description]
    addvalwin= Toplevel()
    addvalwin.iconbitmap("favicon.ico")
    addvalwin.configure(bg="lightblue3")
    toplab = Label(addvalwin,text="Add Records to Table",bg="slategrey")
    toplab.configure(font=("modern",40))    
    toplab.pack()
    frameval = LabelFrame(addvalwin,padx=50,pady=20,bg="slategrey")
    frameval.pack(padx=50,pady=50)
    columnbox = []
    for j in range(len(names)):
        columnbox.append(Text(frameval,height=1,width=20,wrap=None))
        columnbox[j].insert(INSERT,names[j])
        columnbox[j].grid(row=0,column=j)
        columnbox[j].config(state=DISABLED)
        columnbox[j].configure(font=("Modern",13),bg="lightblue3")
    global textbox
    textbox = list()
    for i in range(len(names)):
        textbox.append(Text(frameval, height = 1, width = 20, wrap = None ))
        textbox[i].insert(INSERT,"")
        textbox[i].grid(row=1,column=i)
        textbox[i].configure(font=("Modern",13),bg="lightblue3")
    submit = Button(addvalwin,text="Insert In Table",bg="slategrey",command=insert_call)
    submit.configure(font=("Modern",15))
    submit.pack()
    addvalwin.resizable(False, False)
    
def view_columns():
    global cur
    global con
    temper = cur.execute(f"Select * from {tableentry.get()};")
    name = [description[0] for description in temper.description]
    rev = Toplevel()
    rev.iconbitmap("favicon.ico")
    rev.title("View Table")
    rev.configure(bg="lightblue3")
    topster = Label(rev,text="      ",bg="slategrey")
    topster.configure(font=("Modern",20))
    topster.grid(row=0,column=1)
    dem = cur.execute(f"select * from {tableentry.get()};")
    res = dem.fetchall()
    output = Text(rev, height=10, width=30,padx=100,pady=100,bg="lightblue3")
    output.configure(font=("modern",25))
    output.tag_configure('center',justify='center')
    output.grid(row=1,column=1)
    columnbox = []
    for j in range(len(name)):
        columnbox.append(Text(topster,height=1,width=20,wrap=None))
        columnbox[j].insert(INSERT,name[j])
        columnbox[j].grid(row=0,column=j)
        columnbox[j].config(state=DISABLED)
        columnbox[j].configure(font=("Modern",13),bg="lightblue3")
    if (res == []):
        output.insert(END, "No Item in Columns"+'\n')
    else:
        for item in res:
            output.insert(END, str(item)+'\n')
    output.config(state=DISABLED)
    con.commit()
    rev.resizable(FALSE,FALSE)

def real_name_changer(newname,name):
    global cur
    tcquery=f"ALTER table {tableentry.get()} RENAME to {newname}"
    cur.execute(tcquery)
    con.commit()
    messagebox.showinfo('Success!',f"The Table has been renamed to {newname}")
    name.destroy()
    
def change_name():
    changetypewin = Toplevel()
    changetypewin.iconbitmap("favicon.ico")
    changetypewin.title("Update Table Name")
    changetypewin.configure(bg="lightblue3")
    cttop = Label(changetypewin,text="Change Table Name",bg="slategrey",padx=70,pady=30)
    cttop.configure(font=("modern",30))
    cttop.pack()
    ctframe = LabelFrame(changetypewin,bg="lightblue3",padx=200,pady=50)
    ctframe.pack()
    cname = Label(ctframe,text="Enter New Table Name",padx=50,bg="slategrey",pady=20)
    cname.configure(font=("Modern",15))
    cname.grid(row = 0,column=1,pady=10)
    ctentry=Entry(ctframe,width=50,borderwidth=4)
    ctentry.grid(row = 1, column=1,pady=10)
    ctBut = Button(ctframe, text="Submit",padx=30,pady=20,bg="slategrey",command=lambda: real_name_changer(ctentry.get(),changetypewin))
    ctBut.configure(font=("Modern",10))
    ctBut.grid(row = 2, column = 1, pady=10)

def del_it(name_of_col, delete_this):
    global cur
    global con
    dq= f"DELETE from {tableentry.get()} where {name_of_col} = {delete_this};"
    rek = messagebox.showinfo("Delete Row", "Row has been deleted")
    cur.execute(dq)
    con.commit()

def delete_rec():
    delrec = Toplevel()
    delrec.configure(bg="lightblue3")
    delrec.iconbitmap("favicon.ico")
    delrec.title("Delete Record")
    deltop = Label(delrec,text="Delete Record",bg="slategrey",padx=67)
    deltop.configure(font=("Modern",35))
    deltop.pack()
    delframe = LabelFrame(delrec,bg="lightblue3",padx=150,pady=30)
    delframe.pack()
    l2=[]
    q=f"SELECT l.name FROM pragma_table_info('{tableentry.get()}') as l WHERE l.pk = 1;"
    l2=cur.execute(q).fetchall()
    textr = f"Enter {l2[0][0]} To Delete"
    lab = Label(delframe,text =textr, bg="slategrey",padx= 50)
    lab.configure(font=("Modern",15))
    lab.grid(row=0, column=1,pady=10)
    laben = Entry(delframe,width=50,borderwidth=5)
    laben.grid(row=1, column=1,pady=10)
    delsub= Button(delframe,text="Submit",bg="slategrey",padx=20,command=lambda:del_it(l2[0][0], laben.get()))
    delsub.configure(font=("modern",15))
    delsub.grid(row=2,column=1,pady=10)

def real_get_record(primary_column,col,frame):
    list1=[]
    q=f"SELECT * from {tableentry.get()} where {primary_column}={col};"
    list1=cur.execute(q).fetchall()
    textrt = f"{list1[0]}"
    result=Label(frame,text=textrt,padx=100,pady=20,bg="slategrey")
    result.configure(font=("Modern",15))
    result.grid(row=3,column=0,pady=20)

def get_records(primary_column):
    grec = Toplevel()
    grec.configure(bg="lightblue3")
    grec.iconbitmap("favicon.ico")
    grec.title("Get Record")
    grtop = Label(grec,text="Get Individual Record",bg="slategrey",padx=67)
    grtop.configure(font=("Modern",35))
    grtop.pack()
    grframe = LabelFrame(grec, bg="lightblue3",padx=150,pady=30)
    grframe.pack()
    grtext = f"Enter The {primary_column} To Obtain Full Record"
    grframelab = Label(grframe, text=grtext,bg="slategrey",padx=50,pady=10)
    grframelab.grid(row = 0, column = 0, pady=20)
    grframelab.configure(font=("Modern",17))
    grframeent = Entry(grframe,border=50,borderwidth=5)
    grframeent.grid(row=1, column=0,pady=20)
    grsub = Button(grframe, text="Submit", padx=35,pady=10,bg="slategrey",command = lambda:real_get_record(primary_column, grframeent.get(),grframe))
    grsub.configure(font=("Modern",15))
    grsub.grid(row=2, column = 0,pady=20)
    
def view_table():
    global cur
    view=Toplevel()
    view.iconbitmap("favicon.ico")
    view.title("View/Update Table")
    top = Label(view,text="View/Update Existing Table",bg="slategrey",padx=67)
    top.configure(font=("modern",35))
    view.configure(bg="lightblue3")
    top.pack()
    frame=LabelFrame(view,bg="lightblue3",padx=150,pady=30)
    frame.pack()
    print_all_columns=Button(frame,text="View All Columns",bg="slategrey",padx=63,pady=30,command=view_columns);
    print_all_columns.grid(row=1,column=0,padx=10,pady=20)
    print_all_columns.configure(font=("modern",15))
    updatebutton = Button(frame, text= "Add Records",padx=79,bg ="slategrey", pady=30,command=add_values)
    updatebutton.grid(row=2,column=0,padx=10,pady=20)
    updatebutton.configure(font=("modern",15))
    change_column_type = Button(frame, text="Change Table Name", bg ="slategrey", padx=51,pady=30,command = change_name)
    change_column_type.grid(row = 3, column = 0, padx= 10, pady=20)
    change_column_type.configure(font=("modern",15))
    l1=[]
    q=f"SELECT l.name FROM pragma_table_info('{tableentry.get()}') as l WHERE l.pk = 1;"
    l1=cur.execute(q).fetchall()
    if(l1 != []):
        delete_record = Button(frame, text="Delete Record",bg="slategrey",padx=74,pady=30,command=delete_rec)
        delete_record.grid(row = 4, column = 0, padx=10, pady=20)
        delete_record.configure(font=("Modern",15))
        get_record= Button(frame, text="Get Single Record",bg= "slategrey",padx=60,pady=30,command=lambda:get_records(l1[0][0]))
        get_record.grid(row=5, column =0, padx=10, pady=20)
        get_record.configure(font =("modern",15))
    view.resizable(False, False)
    
def add_column():
    if validation(cnentry) == 0:
        global tabname
        global primcheck
        global count
        count=count+1
        if (count==1):
            if(primcheck==0):
                res = messagebox.askyesno("Unique Column","Would you like to select this column as the Unique Column? (SELECTING 'YES' ALLOWS YOU TO DELETE RECORDS)")
                if res==1:
                    primcheck=1
                    query= f"CREATE table {tabname}({cnentry.get()} {result} PRIMARY KEY);"
                else:
                    query= f"CREATE table {tabname}({cnentry.get()} {result});"
            cur.execute(query)
        else:
            query1 = f"ALTER table {tabname} add {cnentry.get()} {result};"
            cur.execute(query1)
        con.commit()
        messagebox.showinfo('Success!',f"The Column {cnentry.get()} been added!")
    
def new_table_next():
    if validation(tablename) == 0:
        global result
        global cnentry
        global tabname
        tabname = tablename.get()
        newtableui.destroy()
        nextui = Toplevel()
        nextui.iconbitmap("favicon.ico")
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
    newtableui.iconbitmap("favicon.ico")
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
    global primcheck
    response = messagebox.askyesno("Error Finding Table",f"Did not find table {tableentry.get()} in {data.get()}. Do you want to create a new table?")
    if (response==1):
        primcheck=0
        sqlitepage.destroy()
        new_table()
        
def check_table():
    if validation(data) == 0 and validation(tableentry)==0:
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

def real_generator(exdata, extableentry,filename):
    if '.csv' not in filename:
        filename=filename+'.csv'
    fp = open(filename,'w',newline='')
    write = csv.writer(fp)
    exxcon = sqlite3.connect(exdata.get())
    exxcur = exxcon.cursor()
    query = f"select * from {extableentry.get()};"
    extemp=exxcur.execute(query)
    name = [description[0] for description in extemp.description]
    write.writerow(name)
    insertlist = extemp.fetchall()
    for i in insertlist:
        write.writerow(i)
    messagebox.showinfo('Success!', "The Excel CSV has been generated!")
    fp.close()
    exxcon.close()
    
def excel_generator(exdata, extableentry):
    exdesign = Toplevel()
    exdesign.iconbitmap("favicon.ico")
    exdesign.configure(bg="lightblue3")
    exdlabel = Label(exdesign,text="Enter File Name",bg="slategrey",padx=30,pady=20)
    exdlabel.configure(font=("modern",30))
    exdlabel.grid(row=0,column=1,pady=30)
    exinp = Entry(exdesign, width=60,borderwidth=5)
    exinp.grid(row=1, column = 1,pady=20,padx=50)
    exbut = Button(exdesign,text="Generate",bg="slategrey",padx=20,pady=10,command=lambda: real_generator(exdata,extableentry,exinp.get()))
    exbut.configure(font=("Modern",16))
    exbut.grid(row = 2, column=1,pady=20)

def excheck_table(exdata,extableentry):
    if validation(exdata) == 0 and validation(extableentry)==0:
        excon = sqlite3.connect(exdata.get())
        excur=excon.cursor()
        exquery = f"SELECT tbl_name FROM sqlite_master WHERE type='table' AND tbl_name='{extableentry.get()}';"
        exlist1=excur.execute(exquery).fetchall()
        excon.commit()
        if exlist1 == []:
            messagebox.showinfo('Error', "This table does not exist!")
        else:
            excel_generator(exdata,extableentry)
        excon.close()
    
def sqlitepage():
    global count
    count=0
    global sqlitepage
    sqlitepage= Toplevel() 
    sqlitepage.iconbitmap("favicon.ico")
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
    exsqlitepage= Toplevel() 
    exsqlitepage.iconbitmap("favicon.ico")
    exsqlitepage.title("Excel Initialization")
    exsqlitepage.configure(bg="lightblue3")
    exlabel2= Label(exsqlitepage,text="Excel Initialization",bg="slategrey",padx=10,pady=10)
    exlabel2.config(font=('Modern',30))
    exlabel2.grid(row=0,column=1)
    exframe2 = LabelFrame(exsqlitepage,bg="slategrey", padx=200,pady=200)
    exframe2.grid(row=1,column=1,padx=10,pady=10)
    exdata=Entry(exframe2,width=60,borderwidth=4);
    exdata.grid(row =1, column=0)
    exdatalabel = Label(exframe2,text="Enter Database Name",bg="lightblue3",padx=10,pady=10)
    exdatalabel.grid(row=0,column=0,pady=10)
    extablelabel = Label(exframe2,text="Enter Table Name",bg="lightblue3",padx=10,pady=10)
    extablelabel.grid(row=2,column=0,pady=10)
    exdatalabel.config(font=('Modern',20))
    extablelabel.config(font=('Modern',20))
    extableentry= Entry(exframe2,width=60,borderwidth=4)
    extableentry.grid(row=3,column=0)
    exbutton1 = Button(exframe2,text="Generate Excel",padx=10,pady=10,bg = "lightblue3",command = lambda: excheck_table(exdata,extableentry))
    exbutton1.grid(row=4,column=0,pady=10)
    exbutton1.configure(font=('Modern',15))
    exsqlitepage.resizable(False, False)
    

root = Tk()
root.title("The Blue Database")
root.iconbitmap("favicon.ico")
root.configure(bg="lightblue3")
label1 = Label(root,text="The Blue Database",bg="slategrey",padx=10,pady=10)
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