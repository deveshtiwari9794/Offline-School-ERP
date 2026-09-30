import sqlite3
import tkinter as tk
from tkinter import messagebox
from db_path import database_path


def open_admission(parent=None):

    if parent is not None:
        window = tk.Toplevel(parent)
    else:
        window = tk.Tk()

    window.title("Student Admission")
    window.geometry("500x650")

    def save_student():

        name = name_entry.get()
        father = father_entry.get()
        admission = admission_entry.get()
        class_name = class_entry.get()
        section = section_entry.get()
        phone = phone_entry.get()
        address = address_entry.get()

        # Check required fields
        if name == "" or admission == "":
            messagebox.showerror(
                "Error",
                "Student Name and Admission Number are required!"
            )
            return

        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM students WHERE admission_no = ?",
            (admission,)
        )

        existing_student = cursor.fetchone()

        if existing_student:
            messagebox.showerror(
                "Error",
                "Admission Number already exists!"
            )
            connection.close()
            return

        cursor.execute("""
        INSERT INTO students
        (admission_no, name, father_name, class_name, section, phone, address)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            admission,
            name,
            father,
            class_name,
            section,
            phone,
            address
        ))

        connection.commit()
        connection.close()

        messagebox.showinfo(
            "Success",
            "Student saved successfully!"
        )

    heading = tk.Label(
        window,
        text="Student Admission",
        font=("Arial", 20)
    )

    heading.pack(pady=20)

    # Student Name
    name_label = tk.Label(
        window,
        text="Student Name"
    )
    name_label.pack()

    name_entry = tk.Entry(window)
    name_entry.pack(pady=5)

    # Father Name
    father_label = tk.Label(
        window,
        text="Father Name"
    )
    father_label.pack()

    father_entry = tk.Entry(window)
    father_entry.pack(pady=5)

    # Admission Number
    admission_label = tk.Label(
        window,
        text="Admission Number"
    )
    admission_label.pack()

    admission_entry = tk.Entry(window)
    admission_entry.pack(pady=5)

    # Class
    class_label = tk.Label(
        window,
        text="Class"
    )
    class_label.pack()

    class_entry = tk.Entry(window)
    class_entry.pack(pady=5)

    # Section
    section_label = tk.Label(
        window,
        text="Section"
    )
    section_label.pack()

    section_entry = tk.Entry(window)
    section_entry.pack(pady=5)

    # Phone
    phone_label = tk.Label(
        window,
        text="Phone"
    )
    phone_label.pack()

    phone_entry = tk.Entry(window)
    phone_entry.pack(pady=5)

    # Address
    address_label = tk.Label(
        window,
        text="Address"
    )
    address_label.pack()

    address_entry = tk.Entry(window)
    address_entry.pack(pady=5)

    # Save Button
    save_button = tk.Button(
        window,
        text="Save Student",
        command=save_student
    )

    save_button.pack(pady=20)

    if parent is None:
        window.mainloop()

    return window
if __name__ == "__main__":
    open_admission()