import tkinter as tk
from tkinter import messagebox
import Book
import Member
import Issue

def style_window(window, title, height):
    window.title(title)
    window.geometry(f"450x{height}")
    window.configure(bg="#f0f8ff")

def style_label(parent, text):
    return tk.Label(parent, text=text, font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#333").pack(pady=15)

def style_button(parent, text, command):
    return tk.Button(parent, text=text, width=35, height=2, font=("Helvetica", 10), bg="#4682b4", fg="white", activebackground="#5f9ea0", command=command).pack(pady=7)

def Menubook():
    window = tk.Toplevel()
    style_window(window, "Book Record Management", 400)
    style_label(window, "Book Record Management")

    style_button(window, "1. Add Book Record", Book.insertData)
    style_button(window, "2. Search Book Record", Book.SearchBookRec)
    style_button(window, "3. Delete Book Record", Book.deleteBook)
    style_button(window, "4. Update Book Record", Book.UpdateBook)
    style_button(window, "5. Return to Main Menu", window.destroy)

def MenuMember():
    window = tk.Toplevel()
    style_window(window, "Member Record Management", 400)
    style_label(window, "Member Record Management")

    style_button(window, "1. Add Member Record", Member.insertMember)
    style_button(window, "2. Search Member Record", Member.SearchMember)
    style_button(window, "3. Delete Member Record", Member.deleteMember)
    style_button(window, "4. Update Member Record", Member.UpdateMember)
    style_button(window, "5. Return to Main Menu", window.destroy)

def MenuIssueReturn():
    window = tk.Toplevel()
    style_window(window, "Issue/Return Book Management", 350)
    style_label(window, "Issue/Return Book Management")

    style_button(window, "1. Issue Book", Issue.issueBook)
    style_button(window, "2. Search Issued Book Record", Issue.SearchIssuedBooks)
    style_button(window, "3. Return Issued Book", Issue.returnBook)
    style_button(window, "4. Return to Main Menu", window.destroy)
