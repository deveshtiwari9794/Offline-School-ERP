import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from db_path import database_path


def open_marks_list(parent=None):

    if parent is not None:
        window = tk.Toplevel(parent)
    else:
        window = tk.Tk()

    window.title("Marks List")
    window.geometry("650x400")

    def load_marks():

        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM marks")

        marks = cursor.fetchall()

        connection.close()

        for mark in marks:
            table.insert("", tk.END, values=mark)

    def search_marks():

        admission = search_entry.get()

        for item in table.get_children():
            table.delete(item)

        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM marks WHERE admission_no = ?",
            (admission,)
        )

        marks = cursor.fetchall()

        connection.close()

        if not marks:
            messagebox.showerror(
                "Error",
                "Marks record not found!"
            )
            return

        for mark in marks:
            table.insert("", tk.END, values=mark)

    heading = tk.Label(
        window,
        text="Marks List",
        font=("Arial", 22)
    )

    heading.pack(pady=20)

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
        command=search_marks
    )

    search_button.pack(pady=10)

    table = ttk.Treeview(
        window,
        columns=(
            "ID",
            "Admission",
            "Maths",
            "Science",
            "English"
        ),
        show="headings"
    )

    table.heading("ID", text="ID")
    table.heading("Admission", text="Admission No.")
    table.heading("Maths", text="Maths")
    table.heading("Science", text="Science")
    table.heading("English", text="English")

    table.pack(
        pady=20,
        fill="both",
        expand=True
    )

    load_marks()

    if parent is None:
        window.mainloop()

    return window


if __name__ == "__main__":
    open_marks_list()