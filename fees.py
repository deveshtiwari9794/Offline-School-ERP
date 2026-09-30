import sqlite3
import tkinter as tk
from tkinter import messagebox
from db_path import database_path


def open_fees(parent=None):

    if parent is not None:
        window = tk.Toplevel(parent)
    else:
        window = tk.Tk()

    window.title("Fees Management")
    window.geometry("500x450")

    def calculate_fee():

        tuition_text = tuition_entry.get()
        bus_text = bus_entry.get()

        if tuition_text == "" or bus_text == "":
            messagebox.showerror(
                "Error",
                "Please enter Tuition Fee and Bus Fee!"
            )
            return

        tuition = float(tuition_text)
        bus = float(bus_text)

        total = tuition + bus

        total_label.config(
            text=f"Total Fee: {total}"
        )

    def save_fee():

        admission = admission_entry.get()
        tuition_text = tuition_entry.get()
        bus_text = bus_entry.get()

        if admission == "":
            messagebox.showerror(
                "Error",
                "Please enter Admission Number!"
            )
            return

        if tuition_text == "" or bus_text == "":
            messagebox.showerror(
                "Error",
                "Please enter Tuition Fee and Bus Fee!"
            )
            return

        tuition = float(tuition_text)
        bus = float(bus_text)

        if tuition < 0 or bus < 0:
            messagebox.showerror(
                "Error",
                "Fee cannot be negative!"
            )
            return

        total = tuition + bus

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

        cursor.execute("""
        INSERT INTO fees
        (admission_no, tuition_fee, bus_fee, total_fee)
        VALUES (?, ?, ?, ?)
        """, (
            admission,
            tuition,
            bus,
            total
        ))

        connection.commit()
        connection.close()

        messagebox.showinfo(
            "Success",
            "Fee saved successfully!"
        )

    heading = tk.Label(
        window,
        text="Fees Management",
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

    # Tuition Fee
    tuition_label = tk.Label(
        window,
        text="Tuition Fee"
    )

    tuition_label.pack()

    tuition_entry = tk.Entry(window)
    tuition_entry.pack(pady=5)

    # Bus Fee
    bus_label = tk.Label(
        window,
        text="Bus Fee"
    )

    bus_label.pack()

    bus_entry = tk.Entry(window)
    bus_entry.pack(pady=5)

    # Calculate Button
    calculate_button = tk.Button(
        window,
        text="Calculate Total Fee",
        command=calculate_fee
    )

    calculate_button.pack(pady=20)

    save_button = tk.Button(
        window,
        text="Save Fee",
        command=save_fee
    )

    save_button.pack(pady=10)

    # Total
    total_label = tk.Label(
        window,
        text="Total Fee: 0",
        font=("Arial", 14)
    )

    total_label.pack(pady=20)

    if parent is None:
        window.mainloop()

    return window


if __name__ == "__main__":
    open_fees()