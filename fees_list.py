import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from db_path import database_path


def open_fees_list(parent=None):

    if parent is not None:
        window = tk.Toplevel(parent)
    else:
        window = tk.Tk()

    window.title("Fees List")
    window.geometry("600x400")

    def load_fees():

        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM fees")

        fees = cursor.fetchall()

        connection.close()

        for fee in fees:
            table.insert("", tk.END, values=fee)

    def search_fees():

        admission = search_entry.get()

        for item in table.get_children():
            table.delete(item)

        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM fees WHERE admission_no = ?",
            (admission,)
        )

        fees = cursor.fetchall()

        connection.close()

        if not fees:
            messagebox.showerror(
                "Error",
                "Fee record not found!"
            )
            return

        for fee in fees:
            table.insert("", tk.END, values=fee)

    heading = tk.Label(
        window,
        text="Fees List",
        font=("Arial", 22)
    )

    heading.pack(pady=20)

    # Search Admission Number
    search_label = tk.Label(
        window,
        text="Admission Number"
    )

    search_label.pack()

    search_entry = tk.Entry(window)
    search_entry.pack(pady=5)

    search_button = tk.Button(
        window,
        text="Search",
        command=search_fees
    )

    search_button.pack(pady=10)

    # Table
    table = ttk.Treeview(
        window,
        columns=(
            "ID",
            "Admission",
            "Tuition",
            "Bus",
            "Total"
        ),
        show="headings"
    )

    table.heading("ID", text="ID")
    table.heading("Admission", text="Admission No.")
    table.heading("Tuition", text="Tuition Fee")
    table.heading("Bus", text="Bus Fee")
    table.heading("Total", text="Total Fee")

    table.pack(
        pady=20,
        fill="both",
        expand=True
    )

    load_fees()

    if parent is None:
        window.mainloop()

    return window


if __name__ == "__main__":
    open_fees_list()