import datetime


class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = f"{first_name}.{last_name}@outlook.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # convetion class as given as cls
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # convention method name starts with from
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        # int(pay) important otherwise rnt error multiplay by string
        return cls(first, last, int(pay))

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee("Schehat", "Abdel_Kader", 100)
emp2 = Employee("John", "Miller", 50000)

Employee.set_raise_amount(1.05)
emp1.set_raise_amount(1.05)  # also possible but not good practice

print("raise over all instances")
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

# parse a string to create class
emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Jane-Doe-90000"

new_emp1 = Employee.from_string(emp_str_1)
print(f"\nparsed string first name: {new_emp1.first_name}")

new_emp1.apply_raise()
print(f"\n pay after raise: {new_emp1.pay}")

my_day = datetime.date.today() + datetime.timedelta(days=1)
print(f"\nis tomorrow work day: {Employee.is_workday(my_day)}")
