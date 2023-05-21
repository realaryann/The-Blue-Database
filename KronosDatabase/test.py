import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class DatabaseApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SQLite Database App")
        self.geometry("300x200")
        
        self.name_label = ttk.Label(self, text="Name:")
        self.name_label.pack()
        self.name_entry = ttk.Entry(self)
        self.name_entry.pack()
        
        self.age_label = ttk.Label(self, text="Age:")
        self.age_label.pack()
        self.age_entry = ttk.Entry(self)
        self.age_entry.pack()
        
        self.create_db_button = ttk.Button(self, text="Create Database", command=self.create_database)
        self.create_db_button.pack()
        
        self.create_table_button = ttk.Button(self, text="Create Table", command=self.create_table)
        self.create_table_button.pack()
        
        self.insert_data_button = ttk.Button(self, text="Insert Data", command=self.insert_data)
        self.insert_data_button.pack()
        
        self.conn = None
        
    def create_database(self):
        try:
            self.conn = sqlite3.connect('mydatabase.db')
            messagebox.showinfo("Success", "Database created successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        
    def create_table(self):
        if not self.conn:
            messagebox.showerror("Error", "Database not created!")
            return
        
        try:
            cursor = self.conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                              (id INTEGER PRIMARY KEY AUTOINCREMENT,
                               name TEXT NOT NULL,
                               age INTEGER NOT NULL);''')
            self.conn.commit()
            messagebox.showinfo("Success", "Table created successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        
    def insert_data(self):
        if not self.conn:
            messagebox.showerror("Error", "Database not created!")
            return
        
        name = self.name_entry.get()
        age = self.age_entry.get()
        
        if not name or not age:
            messagebox.showerror("Error", "Name and age are required!")
            return
        
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO employees (name, age) VALUES (?, ?)", (name, age))
            self.conn.commit()
            messagebox.showinfo("Success", "Data inserted successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    app = DatabaseApp()
    app.mainloop()
