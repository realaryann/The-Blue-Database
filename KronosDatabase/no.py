import sqlite3
import tkinter as tk
from tkinter import messagebox

# Function to create a new SQLite database
def create_database():
    conn = sqlite3.connect('mydatabase.db')
    messagebox.showinfo("Success", "Database created successfully!")

# Function to create a table in the database
def create_table():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       age INTEGER NOT NULL);''')
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Table created successfully!")

# Function to insert data into the table
def insert_data():
    name = name_entry.get()
    age = age_entry.get()
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employees (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Data inserted successfully!")

# Create the main application window
window = tk.Tk()
window.title("SQLite Database App")

# Create a label and entry for name
name_label = tk.Label(window, text="Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

# Create a label and entry for age
age_label = tk.Label(window, text="Age:")
age_label.pack()
age_entry = tk.Entry(window)
age_entry.pack()

# Create buttons for database and table creation, and data insertion
create_db_button = tk.Button(window, text="Create Database", command=create_database)
create_db_button.pack()

create_table_button = tk.Button(window, text="Create Table", command=create_table)
create_table_button.pack()

insert_data_button = tk.Button(window, text="Insert Data", command=insert_data)
insert_data_button.pack()

# Start the main event loop
window.mainloop()