import sqlite3
import tkinter as tk
from db_path import database_path


def open_search(parent=None):

    if parent is not None:
        window = tk.Toplevel(parent)
    else:
        window = tk.Tk()

    window.title("Search Student")
    window.geometry("500x500")

    def search_student():

        admission = admission_entry.get()
        name = name_entry.get()

        if admission == "" and name == "":
            result_label.config(
                text="Please enter Admission Number or Student Name"
            )
            return

        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        if admission != "":
            cursor.execute(
                "SELECT * FROM students WHERE admission_no = ?",
                (admission,)
            )
        else:
            cursor.execute(
                "SELECT * FROM students WHERE name = ?",
                (name,)
            )

        student = cursor.fetchone()

        connection.close()

        if student:
            result_label.config(
                text=f"Name: {student[2]}\n"
                     f"Father Name: {student[3]}\n"
                     f"Class: {student[4]}\n"
                     f"Section: {student[5]}\n"
                     f"Phone: {student[6]}\n"
                     f"Address: {student[7]}"
            )
        else:
            result_label.config(
                text="Student not found!"
            )

    heading = tk.Label(
        window,
        text="Search Student",
        font=("Arial", 20)
    )

    heading.pack(pady=20)

    # Admission Number
    admission_label = tk.Label(
        window,
        text="Admission Number"
    )

    admission_label.pack()

    admission_entry = tk.Entry(window)
    admission_entry.pack(pady=5)

    # Student Name
    name_label = tk.Label(
        window,
        text="Student Name"
    )

    name_label.pack()

    name_entry = tk.Entry(window)
    name_entry.pack(pady=5)

    # Search Button
    search_button = tk.Button(
        window,
        text="Search Student",
        command=search_student
    )

    search_button.pack(pady=20)

    # Result
    result_label = tk.Label(
        window,
        text="",
        font=("Arial", 12)
    )

    result_label.pack(pady=20)

    if parent is None:
        window.mainloop()

    return window


if __name__ == "__main__":
    open_search()