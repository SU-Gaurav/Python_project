import tkinter as tk
from tkinter import messagebox
import sqlite3
import random
import string

# Database setup
def init_db():
    conn = sqlite3.connect('password_manager.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS passwords
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  website TEXT NOT NULL,
                  username TEXT NOT NULL,
                  password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Generate a random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Save password to the database
def save_password(website, username, password):
    conn = sqlite3.connect('password_manager.db')
    c = conn.cursor()
    c.execute("INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)", 
              (website, username, password))
    conn.commit()
    conn.close()

# Retrieve passwords from the database
def get_passwords():
    conn = sqlite3.connect('password_manager.db')
    c = conn.cursor()
    c.execute("SELECT * FROM passwords")
    records = c.fetchall()
    conn.close()
    return records

# GUI Application
class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator & Manager")
        
        # Initialize database
        init_db()

        # Website Label and Entry
        tk.Label(root, text="Website:").grid(row=0, column=0, padx=10, pady=5)
        self.website_entry = tk.Entry(root, width=30)
        self.website_entry.grid(row=0, column=1, padx=10, pady=5)

        # Username Label and Entry
        tk.Label(root, text="Username:").grid(row=1, column=0, padx=10, pady=5)
        self.username_entry = tk.Entry(root, width=30)
        self.username_entry.grid(row=1, column=1, padx=10, pady=5)

        # Password Label and Entry
        tk.Label(root, text="Password:").grid(row=2, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(root, width=30)
        self.password_entry.grid(row=2, column=1, padx=10, pady=5)

        # Generate Password Button
        tk.Button(root, text="Generate Password", command=self.generate_password).grid(row=3, column=0, columnspan=2, pady=10)

        # Save Password Button
        tk.Button(root, text="Save Password", command=self.save_password).grid(row=4, column=0, columnspan=2, pady=10)

        # View Passwords Button
        tk.Button(root, text="View Saved Passwords", command=self.view_passwords).grid(row=5, column=0, columnspan=2, pady=10)

    def generate_password(self):
        password = generate_password(12)
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

    def save_password(self):
        website = self.website_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not website or not username or not password:
            messagebox.showwarning("Input Error", "Please fill all fields.")
            return

        save_password(website, username, password)
        messagebox.showinfo("Success", "Password saved successfully!")
        self.clear_entries()

    def view_passwords(self):
        passwords_window = tk.Toplevel(self.root)
        passwords_window.title("Saved Passwords")

        passwords = get_passwords()
        if not passwords:
            tk.Label(passwords_window, text="No passwords saved yet.").pack(pady=10)
            return

        for record in passwords:
            tk.Label(passwords_window, text=f"Website: {record[1]} | Username: {record[2]} | Password: {record[3]}").pack(anchor='w')

    def clear_entries(self):
        self.website_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManagerApp(root)
    root.mainloop()