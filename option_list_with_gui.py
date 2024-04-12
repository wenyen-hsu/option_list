import tkinter as tk
from tkinter import messagebox
import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_table(conn):
    try:
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS commands (
                     name TEXT PRIMARY KEY,
                     description TEXT NOT NULL);""")
        conn.commit()
    except Error as e:
        print(e)

class CommandApp:
    def __init__(self, root):
        self.conn = create_connection('commands.db')
        create_table(self.conn)

        self.root = root
        root.title('Command Manager')

        tk.Label(root, text='Command Name:').grid(row=0, column=0)
        self.name_var = tk.StringVar()
        tk.Entry(root, textvariable=self.name_var).grid(row=0, column=1)

        tk.Label(root, text='Description:').grid(row=1, column=0)
        self.description_var = tk.StringVar()
        tk.Entry(root, textvariable=self.description_var).grid(row=1, column=1)

        tk.Button(root, text='Add Command', command=self.add_command).grid(row=2, column=0)
        tk.Button(root, text='Search Command', command=self.search_command).grid(row=2, column=1)
        tk.Button(root, text='Delete Command', command=self.delete_command).grid(row=3, column=0)
        tk.Button(root, text='Update Description', command=self.update_description).grid(row=3, column=1)

    def add_command(self):
        name = self.name_var.get()
        description = self.description_var.get()
        cursor = self.conn.cursor()
        try:
            cursor.execute('INSERT INTO commands (name, description) VALUES (?, ?)', (name, description))
            self.conn.commit()
            messagebox.showinfo("Success", "Command added successfully!")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Command already exists!")

    def search_command(self):
        name = self.name_var.get()
        cursor = self.conn.cursor()
        cursor.execute('SELECT description FROM commands WHERE name = ?', (name,))
        result = cursor.fetchone()
        if result:
            messagebox.showinfo("Result", f"Description: {result[0]}")
        else:
            messagebox.showerror("Error", "Command not found!")

    def delete_command(self):
        name = self.name_var.get()
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM commands WHERE name = ?', (name,))
        self.conn.commit()
        if cursor.rowcount > 0:
            messagebox.showinfo("Success", "Command deleted successfully!")
        else:
            messagebox.showerror("Error", "Command not found!")

    def update_description(self):
        name = self.name_var.get()
        description = self.description_var.get()
        cursor = self.conn.cursor()
        cursor.execute('UPDATE commands SET description = ? WHERE name = ?', (description, name))
        self.conn.commit()
        if cursor.rowcount > 0:
            messagebox.showinfo("Success", "Description updated successfully!")
        else:
            messagebox.showerror("Error", "Command not found!")

if __name__ == '__main__':
    root = tk.Tk()
    app = CommandApp(root)
    root.mainloop()
