import tkinter as tk
import sqlite3
from openpyxl import Workbook
from tkinter import messagebox
from db_path import database_path


def open_report(parent=None):

    if parent is not None:
        window = tk.Toplevel(parent)
    else:
        window = tk.Tk()

    window.title("Report Card")
    window.geometry("500x550")

    def export_excel():

        admission = admission_entry.get()

        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        cursor.execute("""
        SELECT students.name, marks.maths, marks.science, marks.english
        FROM students
        JOIN marks
        ON students.admission_no = marks.admission_no
        WHERE students.admission_no = ?
        """, (admission,))

        report = cursor.fetchone()

        connection.close()

        if not report:
            messagebox.showerror(
                "Error",
                "Student report not found!"
            )
            return

        total = report[1] + report[2] + report[3]

        percentage = (total / 300) * 100

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

        workbook = Workbook()
        sheet = workbook.active

        sheet["A1"] = "Student Report Card"

        sheet["A3"] = "Admission Number"
        sheet["B3"] = admission

        sheet["A4"] = "Student Name"
        sheet["B4"] = report[0]

        sheet["A5"] = "Maths"
        sheet["B5"] = report[1]

        sheet["A6"] = "Science"
        sheet["B6"] = report[2]

        sheet["A7"] = "English"
        sheet["B7"] = report[3]

        sheet["A8"] = "Total Marks"
        sheet["B8"] = total

        sheet["A9"] = "Percentage"
        sheet["B9"] = percentage

        sheet["A10"] = "Grade"
        sheet["B10"] = grade

        workbook.save(f"Report_{admission}.xlsx")

        messagebox.showinfo(
            "Success",
            "Report exported successfully!"
        )

    def fetch_report():

        admission = admission_entry.get()

        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        cursor.execute("""
        SELECT students.name, marks.maths, marks.science, marks.english
        FROM students
        JOIN marks
        ON students.admission_no = marks.admission_no
        WHERE students.admission_no = ?
        """, (admission,))

        report = cursor.fetchone()

        connection.close()

        if report:

            name_result.config(
                text=f"Student Name: {report[0]}"
            )

            marks_result.config(
                text=f"Maths: {report[1]}\n"
                     f"Science: {report[2]}\n"
                     f"English: {report[3]}"
            )

            total = report[1] + report[2] + report[3]

            percentage = (total / 300) * 100

            if percentage >= 90:
                grade = "A+"
            elif percentage >= 80:
                grade = "A"
            elif percentage >= 70:
                grade = "B"
            elif percentage >= 60:
                grade = "C"
            elif percentage >= 50:
                grade = "D"
            else:
                grade = "F"

            total_result.config(
                text=f"Total Marks: {total} / 300\n"
                     f"Percentage: {percentage:.2f}%\n"
                     f"Grade: {grade}"
            )

        else:

            messagebox.showerror(
                "Error",
                "Student not Found"
            )

            name_result.config(
                text="Student not found!"
            )

            marks_result.config(
                text="Marks not found!"
            )

            total_result.config(
                text="Total and Percentage not available"
            )

    heading = tk.Label(
        window,
        text="Student Report Card",
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

    # Student Name
    name_label = tk.Label(
        window,
        text="Student Name"
    )

    name_label.pack()

    name_result = tk.Label(
        window,
        text="---"
    )

    name_result.pack(pady=5)

    # Marks
    marks_result = tk.Label(
        window,
        text="Marks will appear here",
        font=("Arial", 12)
    )

    marks_result.pack(pady=20)

    # Total and Percentage
    total_result = tk.Label(
        window,
        text="Total and Percentage will appear here",
        font=("Arial", 12)
    )

    total_result.pack(pady=10)

    # View Report Button
    fetch_button = tk.Button(
        window,
        text="View Report",
        command=fetch_report
    )

    fetch_button.pack(pady=15)

    # Excel Button
    export_button = tk.Button(
        window,
        text="Export to Excel",
        command=export_excel
    )

    export_button.pack(pady=10)

    if parent is None:
        window.mainloop()

    return window


if __name__ == "__main__":
    open_report()