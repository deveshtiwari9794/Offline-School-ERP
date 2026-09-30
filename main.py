import tkinter as tk
import sys
import os
from tkinter import filedialog, messagebox
import shutil
from db_path import database_path
from PIL import Image, ImageTk


def open_admission():
    import admission
    admission.open_admission(window)


def open_search():
    import search_student
    search_student.open_search(window)


def open_student_list():
    import student_list
    student_list.open_student_list(window)


def open_fees():
    import fees
    fees.open_fees(window)


def open_fees_list():
    import fees_list
    fees_list.open_fees_list(window)


def open_marks():
    import marks
    marks.open_marks(window)


def open_marks_list():
    import marks_list
    marks_list.open_marks_list(window)


def open_report():
    import report
    report.open_report(window)


def backup_database():

    backup_file = filedialog.asksaveasfilename(
        title="Save Database Backup",
        defaultextension=".db",
        filetypes=[("Database Files", "*.db")]
    )

    if backup_file == "":
        return

    shutil.copy(database_path, backup_file)

    messagebox.showinfo(
        "Success",
        "Database backup created successfully!"
    )


def restore_database():

    backup_file = filedialog.askopenfilename(
        title="Select Database Backup",
        filetypes=[("Database Files", "*.db")]
    )

    if backup_file == "":
        return

    confirm = messagebox.askyesno(
        "Confirm Restore",
        "Restore this backup? Current data will be replaced."
    )

    if not confirm:
        return

    shutil.copy(backup_file, database_path)

    messagebox.showinfo(
        "Success",
        "Database restored successfully!"
    )

def logout():

    confirm = messagebox.askyesno(
        "Logout",
        "Do you want to logout?"
    )

    if not confirm:
        return

    window.destroy()

    import login
    login.open_login()


def open_dashboard():

    global window

    window = tk.Tk()

    window.title("School Management System")
    window.state("zoomed")
    window.configure(bg="white")

    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    image_path = os.path.join(
        base_path,
        "assets",
        "school_bg.jpg"
    )

    background_image = Image.open(image_path)

    window.update()

    screen_width = window.winfo_width()
    screen_height = window.winfo_height()

    background_image = background_image.resize(
        (screen_width, screen_height)
    )

    background_photo = ImageTk.PhotoImage(background_image)

    background_label = tk.Label(
        window,
        image=background_photo
    )

    background_label.place(
        x=0,
        y=0,
        relwidth=1,
        relheight=1
    )

    heading = tk.Label(
        window,
        text="School Management System",
        font=("Arial", 30, "bold"),
        bg="light gray"
    )

    heading.pack(pady=15)
    heading.lift()

    button_frame = tk.Frame(
        window,
        bg="light gray",
        padx=15,
        pady=10
    )

    button_frame.pack(pady=10)
    button_frame.lift()

    admission_button = tk.Button(
        button_frame,
        text="Student Admission",
        width=25,
        height=2,
        font=("Arial", 11, "bold"),
        bg="light gray",
        fg="black",
        command=open_admission
    )

    admission_button.grid(
        row=0,
        column=0,
        padx=12,
        pady=12
    )

    search_button = tk.Button(
        button_frame,
        text="Search Student",
        width=25,
        height=2,
        font=("Arial", 11, "bold"),
        bg="light gray",
        fg="black",
        command=open_search
    )

    search_button.grid(
        row=0,
        column=1,
        padx=12,
        pady=12
    )

    list_button = tk.Button(
        button_frame,
        text="Student List",
        width=25,
        height=2,
        font=("Arial", 11, "bold"),
        bg="light gray",
        fg="black",
        command=open_student_list
    )

    list_button.grid(
        row=1,
        column=0,
        padx=12,
        pady=12
    )

    fees_button = tk.Button(
        button_frame,
        text="Fees Management",
        width=25,
        height=2,
        font=("Arial", 11, "bold"),
        bg="light gray",
        fg="black",
        command=open_fees
    )

    fees_button.grid(
        row=1,
        column=1,
        padx=12,
        pady=12
    )

    fees_list_button = tk.Button(
        button_frame,
        text="Fees List",
        width=25,
        height=2,
        font=("Arial", 11, "bold"),
        bg="light gray",
        fg="black",
        command=open_fees_list
    )

    fees_list_button.grid(
        row=2,
        column=0,
        padx=12,
        pady=12
    )

    marks_button = tk.Button(
        button_frame,
        text="Exam Marks",
        width=25,
        height=2,
        font=("Arial", 11, "bold"),
        bg="light gray",
        fg="black",
        command=open_marks
    )

    marks_button.grid(
        row=2,
        column=1,
        padx=12,
        pady=12
    )

    marks_list_button = tk.Button(
        button_frame,
        text="Marks List",
        width=25,
        height=2,
        font=("Arial", 11, "bold"),
        bg="light gray",
        fg="black",
        command=open_marks_list
    )

    marks_list_button.grid(
        row=3,
        column=0,
        padx=12,
        pady=12
    )

    report_button = tk.Button(
        button_frame,
        text="Report Card",
        width=25,
        height=2,
        font=("Arial", 11, "bold"),
        bg="light gray",
        fg="black",
        command=open_report
    )

    report_button.grid(
        row=3,
        column=1,
        padx=12,
        pady=12
    )

    backup_heading = tk.Label(
        button_frame,
        text="Database Backup & Restore",
        font=("Arial", 14, "bold"),
        bg="light gray"
    )

    backup_heading.grid(
        row=4,
        column=0,
        columnspan=2,
        pady=15
    )

    backup_button = tk.Button(
        button_frame,
        text="Backup Database",
        width=25,
        height=2,
        font=("Arial", 11, "bold"),
        bg="light gray",
        fg="black",
        command=backup_database
    )

    backup_button.grid(
        row=5,
        column=0,
        columnspan=2,
        padx=12,
        pady=8
    )

    restore_button = tk.Button(
        button_frame,
        text="Restore Database",
        width=25,
        height=2,
        font=("Arial", 11, "bold"),
        bg="light gray",
        fg="black",
        command=restore_database
    )

    restore_button.grid(
        row=6,
        column=0,
        columnspan=2,
        padx=12,
        pady=8
    )

    logout_button = tk.Button(
    button_frame,
    text="Logout",
    width=25,
    height=2,
    font=("Arial", 11, "bold"),
    bg="light gray",
    fg="black",
    command=logout
    )

    logout_button.grid(
    row=7,
    column=0,
    columnspan=2,
    padx=12,
    pady=8
    )

    window.mainloop()


if __name__ == "__main__":
    open_dashboard()