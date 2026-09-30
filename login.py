import tkinter as tk
from tkinter import messagebox
import sqlite3
from db_path import database_path

def open_login():

    global window
    global username_entry
    global password_entry


    window = tk.Tk()
    conn = sqlite3.connect(database_path)

    cursor = conn.cursor()

    cursor.execute("""
       CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    cursor.execute("""
    INSERT OR IGNORE INTO users (username, password)
    VALUES ('admin', '1234')
    """)

    conn.commit()
    conn.close()

    window.title("School ERP Login")

    window.update()

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    window_width = 400
    window_height = 350

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    window.geometry(
        f"{window_width}x{window_height}+{x}+{y}"
    )


    def clear_fields():

        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)


    def login():

        username = username_entry.get()
        password = password_entry.get()

        conn = sqlite3.connect(database_path)

        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()

        conn.close()


        if user:

         window.destroy()

         import main
         main.open_dashboard()

        else:

         messagebox.showerror(
          "Error",
          "Invalid username or password!"
        )


    heading = tk.Label(
        window,
        text="SCHOOL ERP LOGIN",
        font=("Arial", 20)
    )

    heading.pack(pady=30)


    username_label = tk.Label(
        window,
        text="Username"
    )

    username_label.pack()


    username_entry = tk.Entry(window)

    username_entry.pack(pady=5)


    password_label = tk.Label(
        window,
        text="Password"
    )

    password_label.pack()


    password_entry = tk.Entry(
        window,
        show="*"
    )

    password_entry.pack(pady=5)


    def show_password():

        if password_entry.cget("show") == "*":
            password_entry.config(show="")
        else:
            password_entry.config(show="*")


    show_password_button = tk.Checkbutton(
        window,
        text="Show Password",
        command=show_password
    )

    show_password_button.pack()


    clear_button = tk.Button(
        window,
        text="CLEAR",
        width=10,
        height=1,
        font=("Arial", 11, "bold"),
        bg="light gray",
        fg="black",
        command=clear_fields
    )

    clear_button.pack(pady=5)


    login_button = tk.Button(
        window,
        text="LOGIN",
        width=18,
        height=2,
        font=("Arial", 11, "bold"),
        bg="light gray",
        fg="black",
        command=login
    )

    login_button.pack(pady=20)


    window.bind(
        "<Return>",
        lambda event: login()
    )


    window.mainloop()


if __name__ == "__main__":
    open_login()