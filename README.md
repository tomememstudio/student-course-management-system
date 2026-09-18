Student Course Management System

Overview

The Student Course Management System is a Python application that uses a SQLite relational database to manage students, courses, and course enrollments. The program provides a simple menu for adding, viewing, updating, deleting, and querying data.

Features

Create a SQLite database with students, courses, and enrollments tables.

Add and view students.

Update and delete students.

Add and view courses.

Enroll students in courses.

View enrollment information using SQL JOIN operations across related tables.

Store enrollment dates.

Use SQL commands from the Python program and use returned database results in the application.

Technologies Used

Python

SQLite

VS Code

Git and GitHub

Database Structure

Students

student_id - Primary key

name - Student name

email - Student email address

Courses

course_id - Primary key

course_code - Course code

course_name - Course name

Enrollments

enrollment_id - Primary key

student_id - Foreign key connected to students

course_id - Foreign key connected to courses

enrollment_date - Date the enrollment was created

How to Run

Make sure Python 3 is installed.

Open the project folder in VS Code or another Python editor.

Open a terminal in the project folder.

Run:

python main.py

The program creates the SQLite database file automatically when it starts.

How the Program Works

The program begins by creating the database tables if they do not already exist. The main menu then lets the user choose an operation. Each operation connects to the database, executes an SQL command, receives database results when appropriate, and uses those results to display or update information.

The enrollment feature demonstrates the relational database requirement by joining the enrollments table with the students and courses tables to display meaningful enrollment information.

Project Files

main.py - Main Python program.

student_courses.db - SQLite database file created by the program after it runs.

README.md - Project documentation.

Video

Student video: [PASTE YOUTUBE VIDEO LINK HERE]

GitHub Repository

[PASTE PUBLIC GITHUB REPOSITORY LINK HERE]