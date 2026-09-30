import tkinter as tk
import sqlite3
from tkinter import messagebox
from db_path import database_path


def open_marks(parent=None):

    if parent is not None:
        window = tk.Toplevel(parent)
    else:
        window = tk.Tk()

    window.title("Exam Marks")
    window.geometry("500x450")

    def save_marks():

        admission = admission_entry.get()

        maths_text = maths_entry.get()
        science_text = science_entry.get()
        english_text = english_entry.get()

        if admission == "":
            messagebox.showerror(
                "Error",
                "Please enter Admission Number!"
            )
            return

        if maths_text == "" or science_text == "" or english_text == "":
            messagebox.showerror(
                "Error",
                "Please enter marks for all subjects!"
            )
            return

        maths = float(maths_text)
        science = float(science_text)
        english = float(english_text)

        if maths < 0 or maths > 100:
            messagebox.showerror(
                "Error",
                "Maths marks must be between 0 and 100!"
            )
            return

        if science < 0 or science > 100:
            messagebox.showerror(
                "Error",
                "Science marks must be between 0 and 100!"
            )
            return

        if english < 0 or english > 100:
            messagebox.showerror(
                "Error",
                "English marks must be between 0 and 100!"
            )
            return

        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        # Check student
        cursor.execute(
            "SELECT * FROM students WHERE admission_no = ?",
            (admission,)
        )

        student = cursor.fetchone()

        if not student:
            messagebox.showerror(
                "Error",
                "Student not found!"
            )
            connection.close()
            return

        # Save marks
        cursor.execute("""
        INSERT INTO marks
        (admission_no, maths, science, english)
        VALUES (?, ?, ?, ?)
        """, (
            admission,
            maths,
            science,
            english
        ))

        connection.commit()
        connection.close()

        messagebox.showinfo(
            "Success",
            "Marks saved successfully!"
        )

    heading = tk.Label(
        window,
        text="Exam Marks",
        font=("Arial", 22)
    )

    heading.pack(pady=25)

    # Admission Number
    admission_label = tk.Label(
        window,
        text="Admission Number"
    )

    admission_label.pack()

    admission_entry = tk.Entry(window)
    admission_entry.pack(pady=5)

    # Maths
    maths_label = tk.Label(
        window,
        text="Maths Marks"
    )

    maths_label.pack()

    maths_entry = tk.Entry(window)
    maths_entry.pack(pady=5)

    # Science
    science_label = tk.Label(
        window,
        text="Science Marks"
    )

    science_label.pack()

    science_entry = tk.Entry(window)
    science_entry.pack(pady=5)

    # English
    english_label = tk.Label(
        window,
        text="English Marks"
    )

    english_label.pack()

    english_entry = tk.Entry(window)
    english_entry.pack(pady=5)

    save_button = tk.Button(
        window,
        text="Save Marks",
        command=save_marks
    )

    save_button.pack(pady=20)

    if parent is None:
        window.mainloop()

    return window


if __name__ == "__main__":
    open_marks()