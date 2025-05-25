import tkinter as tk
from tkinter import ttk
import Database
import Menulib

def on_enter(e):
    e.widget['background'] = '#4CAF50'
    e.widget['foreground'] = 'white'

def on_leave(e):
    e.widget['background'] = '#e0e0e0'
    e.widget['foreground'] = 'black'

def main():
    # Initialize the database
    Database.DatabaseCreate()
    Database.TablesCreate()

    # Create the main window
    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("600x400")
    root.configure(bg="#dfe6e9")

    # Style configuration
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 12), padding=10)
    style.configure("TLabel", font=("Arial", 20, "bold"))

    # Central frame
    frame = tk.Frame(root, bg="#ffffff", bd=2, relief=tk.RIDGE)
    frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=300)

    heading = tk.Label(frame, text="Library Management", font=("Arial", 20, "bold"), bg="#ffffff", fg="#2d3436")
    heading.pack(pady=20)

    # Create buttons
    button_specs = [
        ("📚 Book Management", Menulib.Menubook),
        ("👥 Members Management", Menulib.MenuMember),
        ("📖 Issue/Return Book", Menulib.MenuIssueReturn),
        ("❌ Exit", root.destroy)
    ]

    for text, command in button_specs:
        btn = tk.Button(frame, text=text, width=25, font=("Arial", 12), bg="#e0e0e0", fg="black", relief="raised", command=command)
        btn.pack(pady=5)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

    # Start the GUI loop
    root.mainloop()

if __name__ == "__main__":
    main()
