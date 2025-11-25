GradeBook Analyzer – Python Mini Project

A simple CLI-based tool that helps teachers and students analyze marks, calculate statistics, assign grades, and generate results in a clean table format.
This project also includes a CSV Creator Tool to easily generate sample CSV files.

📌 Project Overview

The GradeBook Analyzer allows you to:

Enter student marks manually or load them from a CSV file

Calculate statistical values:

Average

Median

Highest marks

Lowest marks

Assign letter grades (A, B, C, D, F)

Count grade distribution

Identify pass/fail students using list comprehension

Display a formatted result table

Create CSV files interactively

Loop analysis until the user exits

This project is written in beginner-friendly Python and follows the requirements of the Programming for Problem Solving using Python course.

📁 Folder Structure
gradebook_analyzer/
│
├── gradebook.py       # Main Python program
├── students.csv       # Sample CSV file (optional)
└── README.md          # Project documentation

🚀 Features
✔ Manual Input

Enter student names and marks directly in the console.

✔ CSV File Input

Load student data from any .csv file.

✔ CSV Creator Tool

Generate a CSV file by entering names and marks through Python input.

✔ Automatic Statistics

The program calculates:

Average

Median

Minimum

Maximum

✔ Grade Assignment

Grades are assigned using:

Marks	Grade
90+	A
80–89	B
70–79	C
60–69	D
<60	F
✔ Pass / Fail Filter

Using Python list comprehension:

Passed: Score ≥ 40

Failed: Score < 40

✔ Tabular Output

Results displayed in a neat, readable table.

✔ Loop Menu

You can repeat the analysis without restarting the program.
