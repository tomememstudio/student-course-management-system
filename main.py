import sqlite3


def create_database():
    """Create the database and required tables."""
    connection = sqlite3.connect("student_courses.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            course_id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_code TEXT NOT NULL UNIQUE,
            course_name TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS enrollments (
            enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            course_id INTEGER NOT NULL,
            enrollment_date TEXT NOT NULL,
            FOREIGN KEY (student_id) REFERENCES students(student_id),
            FOREIGN KEY (course_id) REFERENCES courses(course_id)
        )
    """)

    connection.commit()
    connection.close()

def add_student():
    """Add a new student to the database."""
    name = input("Enter student name: ")
    email = input("Enter student email: ")

    connection = sqlite3.connect("student_courses.db")
    cursor = connection.cursor()

    try:
        cursor.execute(
            "INSERT INTO students (name, email) VALUES (?, ?)",
            (name, email)
        )
        connection.commit()
        print("Student added successfully!")
    except sqlite3.IntegrityError:
        print("A student with that email already exists.")
    finally:
        connection.close()

def view_students():
    """Display all students stored in the database."""
    connection = sqlite3.connect("student_courses.db")
    cursor = connection.cursor()

    cursor.execute("SELECT student_id, name, email FROM students")
    students = cursor.fetchall()

    connection.close()

    if not students:
        print("No students found.")
        return

    print("\n===== Students =====")

    for student in students:
        print(f"ID: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Email: {student[2]}")
        print("--------------------")

def add_course():
    """Add a new course to the database."""
    course_code = input("Enter course code: ")
    course_name = input("Enter course name: ")

    connection = sqlite3.connect("student_courses.db")
    cursor = connection.cursor()

    try:
        cursor.execute(
            "INSERT INTO courses (course_code, course_name) VALUES (?, ?)",
            (course_code, course_name)
        )
        connection.commit()
        print("Course added successfully!")
    except sqlite3.IntegrityError:
        print("A course with that code already exists.")
    finally:
        connection.close()


def view_courses():
    """Display all courses stored in the database."""
    connection = sqlite3.connect("student_courses.db")
    cursor = connection.cursor()

    cursor.execute("SELECT course_id, course_code, course_name FROM courses")
    courses = cursor.fetchall()

    connection.close()

    if not courses:
        print("No courses found.")
        return

    print("\n===== Courses =====")

    for course in courses:
        print(f"ID: {course[0]}")
        print(f"Code: {course[1]}")
        print(f"Name: {course[2]}")
        print("--------------------")
def enroll_student():
    """Enroll a student in a selected course."""
    view_students()
    student_id = input("Enter the student ID: ")

    view_courses()
    course_id = input("Enter the course ID: ")

    enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")

    connection = sqlite3.connect("student_courses.db")
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO enrollments (student_id, course_id, enrollment_date)
            VALUES (?, ?, ?)
            """,
            (student_id, course_id, enrollment_date)
        )
        connection.commit()
        print("Student enrolled successfully!")
    except sqlite3.IntegrityError:
        print("Could not create enrollment. Check the student and course IDs.")
    finally:
        connection.close()
def view_enrollments():
    """Display enrollment information using a JOIN between three tables."""
    connection = sqlite3.connect("student_courses.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            enrollments.enrollment_id,
            students.name,
            courses.course_code,
            courses.course_name,
            enrollments.enrollment_date
        FROM enrollments
        JOIN students
            ON enrollments.student_id = students.student_id
        JOIN courses
            ON enrollments.course_id = courses.course_id
    """)

    enrollments = cursor.fetchall()
    connection.close()

    if not enrollments:
        print("No enrollments found.")
        return

    print("\n===== Enrollments =====")

    for enrollment in enrollments:
        print(f"Enrollment ID: {enrollment[0]}")
        print(f"Student: {enrollment[1]}")
        print(f"Course: {enrollment[2]} - {enrollment[3]}")
        print(f"Date: {enrollment[4]}")
        print("--------------------")
def update_student():
    """Update an existing student's name or email."""
    view_students()

    student_id = input("Enter the student ID to update: ")
    new_name = input("Enter the new student name: ")
    new_email = input("Enter the new student email: ")

    connection = sqlite3.connect("student_courses.db")
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            UPDATE students
            SET name = ?, email = ?
            WHERE student_id = ?
            """,
            (new_name, new_email, student_id)
        )

        if cursor.rowcount == 0:
            print("Student not found.")
        else:
            connection.commit()
            print("Student updated successfully!")
    except sqlite3.IntegrityError:
        print("That email is already being used.")
    finally:
        connection.close()
def delete_student():
    """Delete an existing student from the database."""
    view_students()

    student_id = input("Enter the student ID to delete: ")

    connection = sqlite3.connect("student_courses.db")
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM students WHERE student_id = ?",
        (student_id,)
    )

    if cursor.rowcount == 0:
        print("Student not found.")
    else:
        connection.commit()
        print("Student deleted successfully!")

    connection.close()
def main_menu():
    """Display the main menu and process user selections."""
    while True:
        print("\n===== Student Course Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Add Course")
        print("4. View Courses")
        print("5. Enroll Student")
        print("6. View Enrollments")
        print("7. Update Student")
        print("8. Delete Student")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            add_course()
        elif choice == "4":
            view_courses()
        elif choice == "5":
            enroll_student()
        elif choice == "6":
            view_enrollments()
        elif choice == "7":
            update_student()
        elif choice == "8":
            delete_student()
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

create_database()
main_menu()

print("Student Course Management System")
print("Database created successfully!")