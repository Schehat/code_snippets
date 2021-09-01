import os
import sqlite3
from employee import Employee

os.chdir(os.path.dirname(__file__))

# :memory: possible which runs on RAM, good for testing
conn = sqlite3.connect("employees.db")

# with the cursor sql commands can be executed
c = conn.cursor()

# c.execute(
#     """Create Table employees(
#     first text,
#     last text,
#     pay integer
# )"""
# )

# c.execute("INSERT INTO employees VALUES('Schehat', 'Abdel Kader', 0)")

emp_1 = Employee("John", "Doe", 60000)
emp_2 = Employee("Arthur", "Doe", 70000)

# if only 1 argument tuple still required and a comma like: (<arg>,)
# c.execute("INSERT INTO employees VALUES(?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))

# # another option
# c.execute(
#     "INSERT INTO employees VALUES(:first, :last, :pay)",
#     {"first": emp_2.first, "last": emp_2.last, "pay": emp_2.pay},
# )

# conn.commit()

c.execute("SELECT * FROM employees")

# c.fetchone(), c.fetchmany(<insert how many>) returns list, c.fetchall()
print(c.fetchall())

# commits current transaction
conn.commit()


def insert_emp(emp):
    with conn:
        c.execute(
            "INSERT INTO employees VALUES(:first, :last, :pay)",
            {"first": emp.first, "last": emp.last, "pay": emp.pay},
        )


def get_emps_by_lastname(last):
    c.execute("SELECT * FROM employees WHERE last = :last", {"last": last})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute(
            """
            UPDATE employees SET pay = :pay WHERE first = :first AND last = :last""",
            {"first": emp.first, "last": emp.last, "pay": pay},
        )


def remove_emp(emp):
    with conn:
        c.execute(
            """
            DELETE FROM employees WHERE first = :first AND last = :last""",
            {"first": emp.first, "last": emp.last},
        )


emp_3 = Employee("Maria", "Doe", 40000)
# insert_emp(emp_3)
# print(get_emps_by_lastname(emp_3.last))

update_pay(emp_1, 90000)
remove_emp(emp_2)

c.execute("SELECT * FROM employees")
print(c.fetchall())

conn.close()
