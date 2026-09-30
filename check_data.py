import sqlite3

connection = sqlite3.connect("school_erp.db")
cursor = connection.cursor()

print("STUDENTS:")

cursor.execute("SELECT admission_no, name FROM students")
students = cursor.fetchall()

for student in students:
    print(student)


print("\nMARKS:")

cursor.execute("SELECT admission_no, maths, science, english FROM marks")
marks = cursor.fetchall()

for mark in marks:
    print(mark)

connection.close()