import tkinter as tk
from tkinter import messagebox
from datetime import date
from Database import get_connection
ENTRY_WIDTH = 30
BG_COLOR = "#ecf0f1"
FG_COLOR = "#2c3e50"
BTN_BG = "#3498db"
BTN_FG = "white"
FRAME_BG = "#ffffff"

def style_button(btn):
    btn.config(bg=BTN_BG, fg=BTN_FG, font=("Arial", 11, "bold"), relief="raised", bd=2, width=20)
    btn.bind("<Enter>", lambda e: btn.config(bg="#2980b9"))
    btn.bind("<Leave>", lambda e: btn.config(bg=BTN_BG))

def style_label(label):
    label.config(bg=FRAME_BG, fg=FG_COLOR, font=("Arial", 11))

def create_window(title, size="400x500"):
    window = tk.Toplevel()
    window.title(title)
    window.geometry(size)
    window.configure(bg=BG_COLOR)
    frame = tk.Frame(window, bg=FRAME_BG, padx=20, pady=20, bd=2, relief="groove")
    frame.pack(expand=True, pady=20)
    return window, frame


def insertMember():
    def save_member():
        try:
            mno = entry_mno.get()
            mname = entry_mname.get()
            DD = int(entry_DD.get())
            MM = int(entry_MM.get())
            YY = int(entry_YY.get())
            addr = entry_addr.get()
            mob = entry_mob.get()
            dob = date(YY, MM, DD)

            cnx = get_connection()
            cursor = cnx.cursor()
            qry = "INSERT INTO Member VALUES(%s, %s, %s, %s, %s)"
            data = (mno, mname, dob, addr, mob)
            cursor.execute(qry, data)
            cnx.commit()
            cursor.close()
            cnx.close()
            messagebox.showinfo("Success", "Record Inserted Successfully!")
            window.destroy()
        except Exception as err:
            messagebox.showerror("Error", f"Failed to insert record:\n{err}")
            if 'cnx' in locals():
                cnx.close()

    window, frame = create_window("Add Member Record")

    fields = [
        ("Member Code", "mno"),
        ("Member Name", "mname"),
        ("Date - DD", "DD"),
        ("Month - MM", "MM"),
        ("Year - YYYY", "YY"),
        ("Address", "addr"),
        ("Mobile No", "mob")
    ]

    entries = {}
    for label_text, var in fields:
        label = tk.Label(frame, text=label_text)
        style_label(label)
        label.pack(pady=3)
        entry = tk.Entry(frame, width=ENTRY_WIDTH)
        entry.pack()
        entries[var] = entry

    entry_mno = entries["mno"]
    entry_mname = entries["mname"]
    entry_DD = entries["DD"]
    entry_MM = entries["MM"]
    entry_YY = entries["YY"]
    entry_addr = entries["addr"]
    entry_mob = entries["mob"]

    btn = tk.Button(frame, text="Save", command=save_member)
    style_button(btn)
    btn.pack(pady=15)


def deleteMember():
    def delete():
        try:
            mno = entry_mno.get()
            cnx = get_connection()
            cursor = cnx.cursor()
            qry = "DELETE FROM Member WHERE MNO = %s"
            cursor.execute(qry, (mno,))
            cnx.commit()
            count = cursor.rowcount
            cursor.close()
            cnx.close()
            messagebox.showinfo("Deleted", f"{count} record(s) deleted.")
            window.destroy()
        except Exception as err:
            messagebox.showerror("Error", f"Failed to delete record:\n{err}")
            if 'cnx' in locals():
                cnx.close()

    window, frame = create_window("Delete Member Record", size="350x200")

    label = tk.Label(frame, text="Enter Member Code to Delete")
    style_label(label)
    label.pack(pady=5)

    entry_mno = tk.Entry(frame, width=ENTRY_WIDTH)
    entry_mno.pack(pady=5)

    btn = tk.Button(frame, text="Delete", command=delete)
    style_button(btn)
    btn.pack(pady=15)


def SearchMember():
    def search():
        try:
            mno = entry_mno.get()
            cnx = get_connection()
            cursor = cnx.cursor()
            qry = "SELECT * FROM Member WHERE MNO = %s"
            cursor.execute(qry, (mno,))
            record = cursor.fetchone()
            cursor.close()
            cnx.close()
            if record:
                mno, mname, dom, addr, mob = record
                result = (
                    f"Member Code: {mno}\n"
                    f"Member Name: {mname}\n"
                    f"Date of Membership: {dom}\n"
                    f"Address: {addr}\n"
                    f"Mobile No: {mob}"
                )
                messagebox.showinfo("Member Found", result)
            else:
                messagebox.showinfo("No Record", "No member found with that code.")
        except Exception as err:
            messagebox.showerror("Error", f"Failed to search record:\n{err}")
            if 'cnx' in locals():
                cnx.close()

    window, frame = create_window("Search Member Record", size="350x200")

    label = tk.Label(frame, text="Enter Member Code to Search")
    style_label(label)
    label.pack(pady=5)

    entry_mno = tk.Entry(frame, width=ENTRY_WIDTH)
    entry_mno.pack(pady=5)

    btn = tk.Button(frame, text="Search", command=search)
    style_button(btn)
    btn.pack(pady=15)




def UpdateMember():
    def load_member():
        try:
            mno = entry_mno.get()
            cnx = get_connection()
            cursor = cnx.cursor()
            qry = "SELECT * FROM Member WHERE MNO = %s"
            cursor.execute(qry, (mno,))
            record = cursor.fetchone()
            cursor.close()
            cnx.close()

            if record:
                _, mname_val, dom_val, addr_val, mob_val = record
                entry_mname.delete(0, tk.END)
                entry_mname.insert(0, mname_val)
                entry_addr.delete(0, tk.END)
                entry_addr.insert(0, addr_val)
                entry_mob.delete(0, tk.END)
                entry_mob.insert(0, mob_val)
                entry_DD.delete(0, tk.END)
                entry_DD.insert(0, dom_val.day)
                entry_MM.delete(0, tk.END)
                entry_MM.insert(0, dom_val.month)
                entry_YY.delete(0, tk.END)
                entry_YY.insert(0, dom_val.year)
            else:
                messagebox.showinfo("No Record", "No member found with that code.")
        except Exception as err:
            messagebox.showerror("Error", f"Failed to load record:\n{err}")
            if 'cnx' in locals():
                cnx.close()

    def save_update():
        try:
            mno = entry_mno.get()
            mname = entry_mname.get()
            DD = int(entry_DD.get())
            MM = int(entry_MM.get())
            YY = int(entry_YY.get())
            addr = entry_addr.get()
            mob = entry_mob.get()
            dom = date(YY, MM, DD)

            cnx = get_connection()
            cursor = cnx.cursor()
            qry = "UPDATE Member SET mname=%s, Date_of_Membership=%s, addr=%s, mob=%s WHERE mno=%s"
            data = (mname, dom, addr, mob, mno)
            cursor.execute(qry, data)
            cnx.commit()
            cursor.close()
            cnx.close()
            messagebox.showinfo("Success", "Record updated successfully.")
            window.destroy()
        except Exception as err:
            messagebox.showerror("Error", f"Failed to update record:\n{err}")
            if 'cnx' in locals():
                cnx.close()

    window, frame = create_window("Update Member Record")

    label = tk.Label(frame, text="Enter Member Code")
    style_label(label)
    label.pack(pady=5)

    entry_mno = tk.Entry(frame, width=ENTRY_WIDTH)
    entry_mno.pack()

    btn_load = tk.Button(frame, text="Load Member Data", command=load_member)
    style_button(btn_load)
    btn_load.pack(pady=10)

    # Editable fields
    fields = [
        ("Member Name", "mname"),
        ("Date - DD", "DD"),
        ("Month - MM", "MM"),
        ("Year - YYYY", "YY"),
        ("Address", "addr"),
        ("Mobile No", "mob")
    ]

    entries = {}
    for label_text, var in fields:
        label = tk.Label(frame, text=label_text)
        style_label(label)
        label.pack(pady=3)
        entry = tk.Entry(frame, width=ENTRY_WIDTH)
        entry.pack()
        entries[var] = entry

    entry_mname = entries["mname"]
    entry_DD = entries["DD"]
    entry_MM = entries["MM"]
    entry_YY = entries["YY"]
    entry_addr = entries["addr"]
    entry_mob = entries["mob"]

    btn_save = tk.Button(frame, text="Save Update", command=save_update)
    style_button(btn_save)
    btn_save.pack(pady=20)
