import tkinter as tk
from tkinter import messagebox
from datetime import date
from Database import get_connection

def SearchIssuedBooks():
    def search():
        try:
            mno = entry_mno.get()
            cnx = get_connection()
            cursor = cnx.cursor()
            qry = "SELECT * FROM issue WHERE mno = %s"
            cursor.execute(qry, (mno,))
            records = cursor.fetchall()
            cursor.close()
            cnx.close()

            if records:
                result_text = ""
                for idx, (bno, Mno, d_o_issue, d_o_ret) in enumerate(records, 1):
                    result_text += (
                        f"Record {idx}:\n"
                        f"  Book Code: {bno}\n"
                        f"  Member Code: {Mno}\n"
                        f"  Date of Issue: {d_o_issue}\n"
                        f"  Date of Return: {d_o_ret}\n"
                        "---------------------------\n"
                    )
                messagebox.showinfo("Issued Books Found", result_text)
            else:
                messagebox.showinfo("No Records", "No issued books found for that member.")
        except Exception as err:
            messagebox.showerror("Error", f"Failed to search issued books:\n{err}")
            if 'cnx' in locals():
                cnx.close()

    window = tk.Toplevel(bg="#f0f8ff")
    window.title("Search Issued Books")
    window.geometry("400x200")

    tk.Label(window, text="Enter Member Code", bg="#f0f8ff", font=("Arial", 12, "bold")).pack(pady=10)
    entry_mno = tk.Entry(window, width=30)
    entry_mno.pack(pady=5)

    tk.Button(window, text="Search", bg="#4682b4", fg="white", font=("Arial", 10, "bold"), command=search).pack(pady=20)

def issueBook():
    def issue():
        try:
            bno = entry_bno.get()
            mno = entry_mno.get()
            DD = int(entry_DD.get())
            MM = int(entry_MM.get())
            YY = int(entry_YY.get())
            d_o_issue = date(YY, MM, DD)

            cnx = get_connection()
            cursor = cnx.cursor()
            qry = "INSERT INTO issue (bno, mno, d_o_issue) VALUES (%s, %s, %s)"
            cursor.execute(qry, (bno, mno, d_o_issue))
            cnx.commit()
            cursor.close()
            cnx.close()

            messagebox.showinfo("Success", "Book issued successfully!")
            window.destroy()
        except Exception as err:
            messagebox.showerror("Error", f"Failed to issue book:\n{err}")
            if 'cnx' in locals():
                cnx.close()

    window = tk.Toplevel(bg="#e6f2ff")
    window.title("Issue Book")
    window.geometry("400x400")

    tk.Label(window, text="Enter Book Code", bg="#e6f2ff", font=("Arial", 12)).pack(pady=5)
    entry_bno = tk.Entry(window, width=30)
    entry_bno.pack(pady=5)

    tk.Label(window, text="Enter Member Code", bg="#e6f2ff", font=("Arial", 12)).pack(pady=5)
    entry_mno = tk.Entry(window, width=30)
    entry_mno.pack(pady=5)

    tk.Label(window, text="Date of Issue - Day", bg="#e6f2ff", font=("Arial", 12)).pack(pady=5)
    entry_DD = tk.Entry(window, width=30)
    entry_DD.pack(pady=5)

    tk.Label(window, text="Date of Issue - Month", bg="#e6f2ff", font=("Arial", 12)).pack(pady=5)
    entry_MM = tk.Entry(window, width=30)
    entry_MM.pack(pady=5)

    tk.Label(window, text="Date of Issue - Year", bg="#e6f2ff", font=("Arial", 12)).pack(pady=5)
    entry_YY = tk.Entry(window, width=30)
    entry_YY.pack(pady=5)

    tk.Button(window, text="Issue Book", bg="#4caf50", fg="white", font=("Arial", 10, "bold"), command=issue).pack(pady=20)

def returnBook():
    def return_book():
        try:
            bno = entry_bno.get()
            mno = entry_mno.get()
            retDate = date.today()

            cnx = get_connection()
            cursor = cnx.cursor()
            qry = "UPDATE issue SET d_o_ret = %s WHERE bno = %s AND mno = %s"
            cursor.execute(qry, (retDate, bno, mno))
            cnx.commit()
            count = cursor.rowcount
            cursor.close()
            cnx.close()

            if count > 0:
                messagebox.showinfo("Success", f"{count} record(s) updated successfully.")
            else:
                messagebox.showinfo("No Match", "No matching issued book record found.")
            window.destroy()
        except Exception as err:
            messagebox.showerror("Error", f"Failed to return book:\n{err}")
            if 'cnx' in locals():
                cnx.close()

    window = tk.Toplevel(bg="#f9f9f9")
    window.title("Return Book")
    window.geometry("400x250")

    tk.Label(window, text="Enter Book Code", bg="#f9f9f9", font=("Arial", 12)).pack(pady=10)
    entry_bno = tk.Entry(window, width=30)
    entry_bno.pack(pady=5)

    tk.Label(window, text="Enter Member Code", bg="#f9f9f9", font=("Arial", 12)).pack(pady=10)
    entry_mno = tk.Entry(window, width=30)
    entry_mno.pack(pady=5)

    tk.Button(window, text="Return Book", bg="#ff9800", fg="white", font=("Arial", 10, "bold"), command=return_book).pack(pady=20)