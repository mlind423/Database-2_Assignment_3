import pandas as pd 
import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor();

# cursor.execute("""
#     CREATE TABLE Works_on (
#         employee_name TEXT,
#         project TEXT,
#         effort INTEGER,
#         PRIMARY KEY (employee_name, project),
#         FOREIGN KEY (project) REFERENCES Project(project)
#     );
#                """)
# dep = pd.read_csv('./Relations/department.csv')
# for index, row in dep.iterrows():
#     cursor.execute(f"INSERT INTO Department VALUES ('{row.EMPLOYEE_NAME}', '{row.DEPARTMENT}');")


cursor.execute("""
            CREATE TABLE Employee (
            employee_ID TEXT,
            DOB DATE,
            DOJ DATE,
            department_ID TEXT,
            PRIMARY KEY (employee_ID),
            FOREIGN KEY (department_ID) REFERENCES Department(department_ID)
        );
               """)

cursor.execute("""
            CREATE TABLE Department (
            department_ID TEXT,
            DOE DATE,
            department_name TEXT,
            PRIMARY KEY (department_ID)
        );
               """)
cursor.execute("""
            CREATE TABLE Student (
            student_ID TEXT,
            DOA DATE,
            DOB DATE,
            department_choice TEXT,
            department_admission TEXT,
            PRIMARY KEY (student_ID, DOA, department_choice)
            FOREIGN KEY (department_choice) REFERENCES Department(department_ID),
            FOREIGN KEY (department_admission) REFERENCES Department(department_ID)
        );
               """)
cursor.execute("""
            CREATE TABLE Performance (
            student_ID TEXT,
            paper_ID TEXT,
            semester_name TEXT,
            paper_name TEXT,
            marks REAL,
            effort_hours INTEGER,
            PRIMARY KEY (student_ID, paper_ID, semester_name)
            FOREIGN KEY (student_ID) REFERENCES Student(student_ID)
        );
               """)

emp = pd.read_csv('./Employee_Information.csv')
for index, row in emp.iterrows():
    cursor.execute(f"INSERT or REPLACE INTO Employee VALUES ('{row.Employee_ID}', '{row.DOB}', '{row.DOJ}', '{row.Department_ID}');")

dep = pd.read_csv('./Department_Information.csv')
for index, row in dep.iterrows():
    cursor.execute(f"INSERT or REPLACE INTO Department VALUES ('{row.Department_ID}', '{row.DOE}', '{row.Department_Name}');")

stuCoun = pd.read_csv('./Student_Counceling_Information.csv')
for index, row in stuCoun.iterrows():
    cursor.execute(f"INSERT or REPLACE INTO Student VALUES ('{row.Student_ID}', '{row.DOA}', '{row.DOB}', '{row.Department_Choices}', '{row.Department_Admission}');")

dep = pd.read_csv('./Updated_Performance.csv')
for index, row in dep.iterrows():
    cursor.execute(f"INSERT or REPLACE INTO Performance VALUES ('{row.Student_ID}', '{row.Paper_ID}', '{row.Semster_Name}', '{row.Paper_Name}', '{row.Marks}', '{row.Effort_Hours}');")


conn.commit()
cursor.close()