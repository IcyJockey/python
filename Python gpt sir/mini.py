import sqlite3
import tkinter as tk
from tkinter import messagebox

# Function to create a database and table for storing student data
def create_database():
    conn = sqlite3.connect('student_results.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        roll_number TEXT NOT NULL,
        name TEXT NOT NULL,
        subject TEXT NOT NULL,
        marks INTEGER NOT NULL
    )
    ''')

    conn.commit()  # Save the changes to the database
    return conn, cursor

# Function to add a student to the database
def add_student(conn, cursor, roll_number, name, subject, marks):
    try:
        cursor.execute('INSERT INTO students (roll_number, name, subject, marks) VALUES (?, ?, ?, ?)', 
                       (roll_number, name, subject, marks))
        conn.commit()
        messagebox.showinfo("Success", "Student added successfully!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Roll number must be unique.")
    except ValueError:
        messagebox.showerror("Error", "Marks must be a number.")

# Function to display all students from the database
def view_all_students(cursor):
    cursor.execute('SELECT * FROM students')
    rows = cursor.fetchall()
    return rows

# Function to search for a student by roll number
def search_student(cursor, roll_number):
    cursor.execute('SELECT * FROM students WHERE roll_number = ?', (roll_number,))
    student = cursor.fetchone()
    return student

# Function to update student marks
def update_marks(conn, cursor, roll_number, marks):
    cursor.execute('UPDATE students SET marks = ? WHERE roll_number = ?', (marks, roll_number))
    conn.commit()

# Function to delete a student's record
def delete_student(conn, cursor, roll_number):
    cursor.execute('DELETE FROM students WHERE roll_number = ?', (roll_number,))
    conn.commit()

# Create the main window (login)
def create_login_screen():
    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("300x200")

    tk.Label(login_window, text="Username:").pack(pady=10)
    username_entry = tk.Entry(login_window)
    username_entry.pack(pady=5)

    tk.Label(login_window, text="Password:").pack(pady=10)
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack(pady=5)

    def login_action():
        username = username_entry.get()
        password = password_entry.get()

        if username == "teacher" and password == "password123":
            login_window.destroy()
            create_teacher_interface()
        elif username == "student" and password == "password123":
            login_window.destroy()
            create_student_interface()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    login_button = tk.Button(login_window, text="Login", command=login_action)
    login_button.pack(pady=20)

    login_window.mainloop()

# Create the teacher interface
def create_teacher_interface():
    teacher_window = tk.Tk()
    teacher_window.title("Teacher Dashboard")
    teacher_window.geometry("400x400")

    tk.Label(teacher_window, text="Roll Number:").pack(pady=5)
    roll_entry = tk.Entry(teacher_window)
    roll_entry.pack(pady=5)

    tk.Label(teacher_window, text="Name:").pack(pady=5)
    name_entry = tk.Entry(teacher_window)
    name_entry.pack(pady=5)

    tk.Label(teacher_window, text="Subject:").pack(pady=5)
    subject_entry = tk.Entry(teacher_window)
    subject_entry.pack(pady=5)

    tk.Label(teacher_window, text="Marks:").pack(pady=5)
    marks_entry = tk.Entry(teacher_window)
    marks_entry.pack(pady=5)

    def add_result():
        roll_number = roll_entry.get()
        name = name_entry.get()
        subject = subject_entry.get()
        marks = marks_entry.get()

        if roll_number and name and subject and marks:
            try:
                marks = int(marks)
                add_student(conn, cursor, roll_number, name, subject, marks)
            except ValueError:
                messagebox.showerror("Error", "Marks must be a number.")
        else:
            messagebox.showerror("Error", "All fields must be filled.")

    def view_results():
        rows = view_all_students(cursor)
        results = "\n".join([f"Roll No: {row[1]}, Name: {row[2]}, Subject: {row[3]}, Marks: {row[4]}" for row in rows])
        messagebox.showinfo("All Results", results)

    def search_result():
        roll_number = roll_entry.get()
        student = search_student(cursor, roll_number)
        if student:
            messagebox.showinfo("Student Found", f"Roll No: {student[1]}, Name: {student[2]}, Subject: {student[3]}, Marks: {student[4]}")
        else:
            messagebox.showerror("Error", "Student not found.")

    def update_result():
        roll_number = roll_entry.get()
        new_marks = marks_entry.get()
        try:
            new_marks = int(new_marks)
            update_marks(conn, cursor, roll_number, new_marks)
            messagebox.showinfo("Success", "Marks updated successfully.")
        except ValueError:
            messagebox.showerror("Error", "Marks must be a number.")

    def delete_result():
        roll_number = roll_entry.get()
        delete_student(conn, cursor, roll_number)
        messagebox.showinfo("Success", "Student record deleted.")

    # Buttons for actions
    tk.Button(teacher_window, text="Add Result", command=add_result).pack(pady=5)
    tk.Button(teacher_window, text="View Results", command=view_results).pack(pady=5)
    tk.Button(teacher_window, text="Search Result", command=search_result).pack(pady=5)
    tk.Button(teacher_window, text="Update Marks", command=update_result).pack(pady=5)
    tk.Button(teacher_window, text="Delete Record", command=delete_result).pack(pady=5)

    teacher_window.mainloop()

# student interface
def create_student_interface():
    student_window = tk.Tk()
    student_window.title("Student Dashboard")
    student_window.geometry("400x200")

    tk.Label(student_window, text="Enter Roll Number:").pack(pady=10)
    roll_entry = tk.Entry(student_window)
    roll_entry.pack(pady=10)

    def search_student_result():
        roll_number = roll_entry.get()
        student = search_student(cursor, roll_number)
        if student:
            messagebox.showinfo("Student Found", f"Roll No: {student[1]}, Name: {student[2]}, Subject: {student[3]}, Marks: {student[4]}")
        else:
            messagebox.showerror("Error", "Student not found.")

    tk.Button(student_window, text="Search Result", command=search_student_result).pack(pady=20)

    student_window.mainloop()

# Start the application
if __name__ == "__main__":
    conn, cursor = create_database()
    create_login_screen()
    close_db(conn)

