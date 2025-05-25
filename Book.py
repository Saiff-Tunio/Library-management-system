import tkinter as tk
from tkinter import messagebox
from datetime import date
from Database import get_connection

def style_window(window, title, size):
    window.title(title)
    window.geometry(size)
    window.configure(bg="#f0f8ff")

def styled_label(master, text):
    return tk.Label(master, text=text, font=("Arial", 12), bg="#f0f8ff")

def styled_entry(master):
    return tk.Entry(master, font=("Arial", 12))

def styled_button(master, text, command):
    return tk.Button(master, text=text, command=command, bg="#4CAF50", fg="white", font=("Arial", 12), width=20)

def insertData():
    def insert():
        try:
            bno = entry_bno.get()
            bname = entry_bname.get()
            Auth = entry_auth.get()
            price = int(entry_price.get())
            publ = entry_publ.get()
            qty = int(entry_qty.get())
            DD = int(entry_DD.get())
            MM = int(entry_MM.get())
            YY = int(entry_YY.get())
            date_of_purchase = date(YY, MM, DD)

            cnx = get_connection()
            cursor = cnx.cursor()
            qry = "INSERT INTO BookRecord VALUES (%s, %s, %s, %s, %s, %s, %s)"
            data = (bno, bname, Auth, price, publ, qty, date_of_purchase)
            cursor.execute(qry, data)
            cnx.commit()
            cursor.close()
            cnx.close()

            messagebox.showinfo("Success", "Record Inserted.")
            window.destroy()
        except Exception as err:
            messagebox.showerror("Error", f"Failed to insert record:\n{err}")
            if 'cnx' in locals():
                cnx.close()

    window = tk.Toplevel()
    style_window(window, "Insert Book Data", "500x700")

    labels = ["Book Code", "Book Name", "Author", "Price", "Publisher", "Quantity",
              "Purchase Date - Day", "Purchase Date - Month", "Purchase Date - Year"]
    entries = []

    for label in labels:
        styled_label(window, label).pack(pady=5)
        entry = styled_entry(window)
        entry.pack(pady=5)
        entries.append(entry)

    (entry_bno, entry_bname, entry_auth, entry_price, entry_publ, entry_qty,
     entry_DD, entry_MM, entry_YY) = entries

    styled_button(window, "Insert", insert).pack(pady=20)

def deleteBook():
    def delete():
        try:
            bno = entry_bno.get()
            cnx = get_connection()
            cursor = cnx.cursor()
            qry = "DELETE FROM BookRecord WHERE BNO = %s"
            cursor.execute(qry, (bno,))
            cnx.commit()
            count = cursor.rowcount
            cursor.close()
            cnx.close()

            if count > 0:
                messagebox.showinfo("Success", f"{count} record(s) deleted successfully.")
            else:
                messagebox.showinfo("No Record", "No matching book found to delete.")
            window.destroy()
        except Exception as err:
            messagebox.showerror("Error", f"Failed to delete record:\n{err}")
            if 'cnx' in locals():
                cnx.close()

    window = tk.Toplevel()
    style_window(window, "Delete Book", "400x200")

    styled_label(window, "Enter Book Code to Delete").pack(pady=10)
    entry_bno = styled_entry(window)
    entry_bno.pack(pady=5)

    styled_button(window, "Delete", delete).pack(pady=20)

def SearchBookRec():
    def search():
        try:
            bno = entry_bno.get()
            cnx = get_connection()
            cursor = cnx.cursor()
            qry = "SELECT * FROM BookRecord WHERE BNo = %s"
            cursor.execute(qry, (bno,))
            records = cursor.fetchall()
            cursor.close()
            cnx.close()

            if records:
                result_text = ""
                for (Bno, Bname, Author, price, publ, qty, Date_of_Purchase) in records:
                    result_text += (
                        f"Book Code: {Bno}\n"
                        f"Book Name: {Bname}\n"
                        f"Author: {Author}\n"
                        f"Price: {price}\n"
                        f"Publisher: {publ}\n"
                        f"Quantity: {qty}\n"
                        f"Date of Purchase: {Date_of_Purchase}\n"
                        "-----------------------------\n"
                    )
                messagebox.showinfo("Search Result", result_text)
            else:
                messagebox.showinfo("No Records", "No book record found.")
        except Exception as err:
            messagebox.showerror("Error", f"Failed to search records:\n{err}")
            if 'cnx' in locals():
                cnx.close()

    window = tk.Toplevel()
    style_window(window, "Search Book Record", "400x200")

    styled_label(window, "Enter Book Code to Search").pack(pady=10)
    entry_bno = styled_entry(window)
    entry_bno.pack(pady=5)

    styled_button(window, "Search", search).pack(pady=20)

def UpdateBook():
    def update():
        try:
            bno = entry_bno.get()
            bname = entry_bname.get()
            Auth = entry_auth.get()
            price = int(entry_price.get())
            publ = entry_publ.get()
            qty = int(entry_qty.get())
            DD = int(entry_DD.get())
            MM = int(entry_MM.get())
            YY = int(entry_YY.get())
            date_of_purchase = date(YY, MM, DD)

            cnx = get_connection()
            cursor = cnx.cursor()
            qry = """UPDATE BookRecord 
                     SET bname=%s, Auth=%s, price=%s, publ=%s, qty=%s, Date_of_Purchase=%s 
                     WHERE Bno=%s"""
            data = (bname, Auth, price, publ, qty, date_of_purchase, bno)
            cursor.execute(qry, data)
            cnx.commit()
            count = cursor.rowcount
            cursor.close()
            cnx.close()

            if count > 0:
                messagebox.showinfo("Success", f"{count} record(s) updated successfully.")
            else:
                messagebox.showinfo("No Record", "No matching book found to update.")
            window.destroy()
        except Exception as err:
            messagebox.showerror("Error", f"Failed to update record:\n{err}")
            if 'cnx' in locals():
                cnx.close()

    window = tk.Toplevel()
    style_window(window, "Update Book Record", "500x700")

    labels = ["Book Code", "Book Name", "Author", "Price", "Publisher", "Quantity",
              "Purchase Date - Day", "Purchase Date - Month", "Purchase Date - Year"]
    entries = []

    for label in labels:
        styled_label(window, label).pack(pady=5)
        entry = styled_entry(window)
        entry.pack(pady=5)
        entries.append(entry)

    (entry_bno, entry_bname, entry_auth, entry_price, entry_publ, entry_qty,
     entry_DD, entry_MM, entry_YY) = entries

    styled_button(window, "Update", update).pack(pady=20)