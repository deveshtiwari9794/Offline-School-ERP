import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from db_path import database_path


def open_student_list(parent=None):

    if parent is not None:
        window = tk.Toplevel(parent)
    else:
        window = tk.Tk()

    window.title("Student List")
    window.geometry("900x500")

    def load_students():

        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM students")

        students = cursor.fetchall()

        connection.close()

        for student in students:
            table.insert("", tk.END, values=student)

    def search_students():

        search_text = search_entry.get()
        selected_class = class_combo.get()

        for item in table.get_children():
            table.delete(item)

        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        if search_text != "" and selected_class != "All":

            cursor.execute(
                """SELECT * FROM students
                   WHERE name LIKE ? AND class_name = ?""",
                ("%" + search_text + "%", selected_class)
            )

        elif search_text != "" and selected_class == "All":

            cursor.execute(
                "SELECT * FROM students WHERE name LIKE ?",
                ("%" + search_text + "%",)
            )

        elif search_text == "" and selected_class != "All":

            cursor.execute(
                "SELECT * FROM students WHERE class_name = ?",
                (selected_class,)
            )

        else:

            cursor.execute("SELECT * FROM students")

        students = cursor.fetchall()

        connection.close()

        for student in students:
            table.insert("", tk.END, values=student)

    def show_class_students():

        selected_class = class_combo.get()

        for item in table.get_children():
            table.delete(item)

        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        if selected_class == "All":
            cursor.execute("SELECT * FROM students")
        else:
            cursor.execute(
                "SELECT * FROM students WHERE class_name = ?",
                (selected_class,)
            )

        students = cursor.fetchall()

        connection.close()

        for student in students:
            table.insert("", tk.END, values=student)

    def delete_student():

        selected = table.selection()

        if not selected:
            messagebox.showerror(
                "Error",
                "Please select a student!"
            )
            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this student?"
        )

        if not confirm:
            return

        student = table.item(selected[0])

        student_id = student["values"][0]

        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM students WHERE id = ?",
            (student_id,)
        )

        connection.commit()
        connection.close()

        table.delete(selected[0])

        messagebox.showinfo(
            "Success",
            "Student deleted successfully!"
        )

    heading = tk.Label(
        window,
        text="Student List",
        font=("Arial", 20)
    )

    heading.pack(pady=20)

    # Search Student
    search_label = tk.Label(
        window,
        text="Search Student"
    )

    search_label.pack()

    search_entry = tk.Entry(window)
    search_entry.pack(pady=5)

    # Class Selection
    class_label = tk.Label(
        window,
        text="Select Class"
    )

    class_label.pack()

    class_combo = ttk.Combobox(
        window,
        values=[
            "All", "1", "2", "3", "4", "5",
            "6", "7", "8", "9", "10", "11", "12"
        ],
        state="readonly"
    )

    class_combo.pack(pady=5)

    class_combo.set("All")

    class_button = tk.Button(
        window,
        text="Show Class Students",
        command=show_class_students
    )

    class_button.pack(pady=10)

    search_button = tk.Button(
        window,
        text="Search",
        command=search_students
    )

    search_button.pack(pady=10)

    # Student Table
    table = ttk.Treeview(
        window,
        columns=(
            "ID",
            "Admission",
            "Name",
            "Father",
            "Class",
            "Section",
            "Phone",
            "Address"
        ),
        show="headings"
    )

    table.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=10
    )

    # Column headings
    table.heading("ID", text="ID")
    table.heading("Admission", text="Admission No.")
    table.heading("Name", text="Student Name")
    table.heading("Father", text="Father Name")
    table.heading("Class", text="Class")
    table.heading("Section", text="Section")
    table.heading("Phone", text="Phone")
    table.heading("Address", text="Address")

    load_students()

    delete_button = tk.Button(
        window,
        text="Delete Student",
        command=delete_student
    )

    delete_button.pack(pady=10)

    if parent is None:
        window.mainloop()

    return window


if __name__ == "__main__":
    open_student_list()