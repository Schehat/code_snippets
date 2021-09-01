class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@email.com"
        self.pay = pay

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # display meant for other developers and returning a string that could
    # recreate this instance
    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    # display meant for users
    def __str__(self):
        return f"{self.fullname()}, {self.email}"

    # non logical example how to implement the __add__ method
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "Employee", 60000)

# uses __str__ first and if it not exists then __repr__
print(emp_1)

print(f"repr: {repr(emp_1)}")  # equals emp_1.__repr__()
print(f"str: {str(emp_1)}\n")

# now this is possible
print(f"emp_1 + emp_2: {emp_1 + emp_2}\n")

print(f"len of emp_1: {len(emp_1)}\n")
